# main.py -- put your code here!
import sys
import stm
TIMER  = const(11)

# start flash
print("Start!")
pyb.LED(1).on()
def flash(timer):
	pyb.LED(1).toggle()
	pyb.LED(2).toggle()

t11=pyb.Timer(TIMER ,freq=10, callback=flash)
pyb.delay(1000)
t11.callback(None)

# Constants
MICROSTEPS   = const(8)                  # 8
STPS_TR      = const(200*MICROSTEPS)     # 1600 탎tp/tr
SECTOR       = const((STPS_TR*3)//16)    # 300 = 67.5� //6
SECTORS_S    = const(15)                 # 15 fps
SLOW         = const(STPS_TR // 2)       # 800 stp/s
FAST         = const(SECTOR * SECTORS_S) # 4500 stp/s
PULSE_MODULO = const(SECTOR*2//200)      # 3

nEN    = pyb.Pin('B15', pyb.Pin.OUT_PP)
DIR    = pyb.Pin('A5', pyb.Pin.OUT_PP)
STP    = pyb.Pin('A6', pyb.Pin.OUT_PP)
BIT6   = const(1 << 6)
PA     = stm.GPIOA + stm.GPIO_ODR
FRAME_PIN = pyb.Pin('B12', pyb.Pin.OUT_PP) #LED_GREEN
PULSE_PIN = pyb.Pin('B10', pyb.Pin.OUT_PP) #LED_RED=B2
BIT10  = const(1 << 10)
PORT_B = stm.GPIOB + stm.GPIO_ODR

# Global vars
stp_pos  = 0
stp_from = 0
stp_to   = 0
stp_dir  = 0
stp_tim  = pyb.Timer(TIMER,freq=1, callback=None)
v0 = 0
v1 = 1

# Irq handler
@micropython.native
def one_step(timer):
	global stp_pos
	global stp_dir
	
	if stp_pos==stp_from and stp_pos==stp_to:
		timer.callback(None)
	elif stp_pos==stp_from:
		stp_dir = +1
		DIR(1)
		FRAME_PIN(1)
		FRAME_PIN(0)
		
	elif stp_pos==stp_to:
		stp_dir = -1
		DIR(0)
		FRAME_PIN(1)
		FRAME_PIN(0)

	if STP():
		STP(0)
		stp_pos += stp_dir
	else:
		STP(1)
		if(stp_pos % PULSE_MODULO == 0):  # /!\ petit bug : ici on ne tir qu'une fois tous les 3 fronts montants
			pulse()                         # soit 100 tirs / secteurs

# Functions
@micropython.viper
def pulse():
	odr = ptr16(PORT_B)
	#odr[0] ^= BIT10

	v0=odr[0]
	v1=v0 | BIT10
	a=1
	odr[0] = v1 # STP(1)+19.5탎
	a+=1
	a+=1
	odr[0] = v0 # +200ns
	
	#global v0
	#global v1
	#PULSE_PIN(1) #STP(1)+14탎				
	#PULSE_PIN(0) #+4.5탎
	#v0=stm.mem16[PORT_B]
	#v1=v0 | BIT10
	#stm.mem16[PORT_B] = v1
	#stm.mem16[PORT_B] = v0

def osc_move(from_pos, to_pos):
	global stp_pos
	global stp_from
	global stp_to
	global stp_dir
	global stp_tim

	stp_from=from_pos
	stp_to=to_pos
	if stp_pos <= stp_to:
		stp_dir = +1
		DIR(1)
	else:
		stp_dir = -1
		DIR(0)
	stp_tim.callback(one_step)
		
def abs_move(pos):
	osc_move(pos, pos)
	stp_wait()

def incr_move(nb_steps):
	global stp_pos
	abs_move(stp_pos + nb_steps)

def stp_wait():
	global stp_pos
	global stp_to
	while stp_pos!=stp_to: pyb.delay(1)

def stp_set_org():
	global stp_pos
	stp_pos=0
	
def stp_speed(stp_s):
	global stp_tim
	stp_tim.freq(stp_s*2)

def stp_on():
	nEN(0)
	PULSE_PIN(0)
	
def stp_off():
	nEN(1)

def stp_stop():
	global stp_tim
	stp_tim.callback(None)

def stp_microsteps(n):
	# m0 m1 탎teps
	# 0  0  1
	# 1  0  1/2
	# ~  0  1/4
	# 0  1  1/8
	# 1  1  1/16
	# ~  1  1/32
	if n==2:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_PP)(1)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(0)
	elif n==4:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_OD)(1)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(0)
	elif n==8:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_PP)(0)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(1)
	elif n==16:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_PP)(1)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(1)
	elif n==32:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_OD)(1)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(1)
	else:
		m0 = pyb.Pin('B14', pyb.Pin.OUT_PP)(0)
		m1 = pyb.Pin('B13', pyb.Pin.OUT_PP)(0)
		
@micropython.native
def kloops_ps():
	t0 = pyb.millis()
	cnt = 0
	while pyb.elapsed_millis(t0) < 100:
		cnt+=1
	return cnt//100
	
# Main
cnt_max = kloops_ps()
print("cnt_max = ",cnt_max,"k")
stp_microsteps(MICROSTEPS)
stp_on()
stp_speed(SLOW)
incr_move(-STPS_TR)
stp_set_org()
stp_speed(FAST)
osc_move(0, SECTOR)
cnt_cur = kloops_ps()
print("cnt_cur = ", cnt_cur,"k")
print("load = ", (1-cnt_cur/cnt_max)*100, "%")
print("ticks/pulse = ", PULSE_MODULO)

print("Command >>>")
