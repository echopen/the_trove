1.  Le Développement Electronique

WORK FLOWS- TEAM ECHOPEN
========================

This page lists the progress og our work and difficultes that we meet.

-   Team
    -   Jerom Dubois, mechanics, microcontroller ....
    -   Na LIU, electronics, arduino softerware about the motor
        and encodor.
    -   Carlos Garay
    -   Constant

Année 2015
----------

### Monday 31th August

communication between John Norman(Director of NTS Ultrasonics Pty
Ltd[1](http://www.ntsu.net.au/)) and Na.

#### Na

At 09:30 PM 26/08/2015, Na wrote: &gt;&gt; Hi, &gt;&gt; &gt;&gt; I am
working with Luc in the project of Echopen. Nice to know you :) &gt;&gt;
I have some questions about the hardware design, it will be very helpful
&gt;&gt; for us if you can give us some suggestions. &gt;&gt; &gt;&gt;
we are using the Arduino Due, therefore the operating voltage is 3.3V,
&gt;&gt; but we need a 100V voltage for the piezoelectric transducer
(5MHz). &gt;&gt; &gt;&gt; So I am thinking of adding an amplification
between the arduino and the &gt;&gt; , &gt;&gt; but I donot know which
type of amplifier do I have to buy. Do you have &gt;&gt; some ideas?
&gt;&gt; &gt;&gt; Will a simple non-inverting operational amplifier
circuit be enough ? &gt;&gt; &gt;&gt; Looking forwar to your reply!
&gt;&gt; &gt;&gt; Thanks and best regards, &gt;&gt; &gt;&gt; Na

#### Jhon

On Wed, August 26, 2015 7:51 pm, John wrote: &gt; Hi Na. &gt; &gt; I
guess it depends on what type of excitation you are using for the &gt;
transducer. The choice of high voltage generator will depend on how the
&gt; transducer is going to be driven. &gt; &gt; If you are driving it
with single short pulses or bursts of pulses, &gt; you need a converter
from 3.3v to 100v, and a pulser circuit to drive the &gt; transducer. A
boost converter can step up the voltage. Have a look at &gt;
<https://learn.adafruit.com/assets/9049>. The &gt; calculator they
provide gives a good first pass at a working design. We &gt; sometimes
use this approach. &gt; &gt; We also sometimes use a step up transformer
driven in a push-pull &gt; inverter arrangement. This is convenient if
you want both +ve and -ve &gt; voltages. &gt; &gt; Hope that helps. &gt;
&gt; &gt; Regards &gt; John Norman

#### Na

At 09:03 PM 28/08/2015, Na wrote: Hi John,

Thanks for the reply.

Actually, I have found a document talking about building the high
voltage power supply ( HVPS, 100V-1000V, please find the related
document PDF in the attachement)

So, can you tell us your opinion on this article ? Do you think that we
can use this circuit to build our HVPS systeme for the transducers? For
me it seems simple and practicable.

But as we don't have all the components at the moment, so I can't test
it immediately, I am trying to use some simulation softeware to simulate
the output, do you use any simulation software as well ?

Best regards,

Na

#### Jhon

31 August 2015 at 02:02, John wrote:

Hi Na.

It is an interesting variation on the boost converter. You will need to
estimate how much current you need. One way is to look at the properties
of the piezo transducer and work from that. We don't take that approach.
We just look at the pulse we drive the transducer with and estimate the
current per pulse, which is usually quite high. This "peak" current is
then averaged out over the number of times per second the transducer is
pulsed, and then you have an estimate of the current required from your
power supply. Double it just to make sure.

The boost converter calculator I directed you to allows you to choose an
output current. With the design you sent me you will need to work it out
for yourself.

In any event, It looks like you could use the circuit, as long as you
get the necessary current. Depending on your application, you may not
need a very high voltage. Piezo transducers are usually very sensitive
as receivers, and you can get useful results from lower transducer
driving voltages.

I do not know anything about your transducer or application, but there
is one other thing you need to keep in mind. Piezo materials are
polarized and for transducer applications usually vibrate in a length
expansion/contraction mode. You need to make sure that the electric
transmit pulse you apply to the transducer initially causes it to
contract, not expand. This will avoid the transducer degrading quickly.

Regards John Norman

### Tuesday 1 September

Present work of Na.

#### Test of the motor

The connection of the arduino and the motor can be found in the site
DIGILENT
[2](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,503&Prod=PMOD-HB5)

![ 600 px](motor connection.jpg  " 600 px")

As we haven't the Motor shield, we build a simple motor control circuit
thanks to this blog
[3](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/overview)
So the composants that we need are: 1, resistor 220 kOhms x1 2,
Transistor PN2222 x1 3, 1N4001 diode x1 4, 270 Ω Resistor (red, purple,
brown stripes) x1 5, Half-size Breadboard x1 6, Jumper wire pack

![ 400 px](circuit-arduino.jpg  " 400 px")

Now build the circuit pour the motor!

![ 600 px](connet motor.JPG  " 600 px")

### Wednesday 2 September

Present work of Na.

#### Test of the encodor

After connecting the motor and arduino together. Now we test the SA and
SB by an oscilloscope:

![ 600 px](Test of motor.JPG  " 600 px")

### Thursday 3 September

Présence de Constant et Na.

#### Reading the encoder

After connecting the motor and arduino together with a potentiometer.

![](motor circuit.JPG "motor circuit.JPG")

Then through the port monitor in the arduino IDE ("TOOLS"-&gt;"Serial
monitor" ) We can test the output of SA and SB :

![ 800 px](test of encoder.jpg  " 800 px")

### Friday 4 September

Present work of Na.

#### Build the high voltage drive circuit

Today, I tried to test the boost calculator suggested by John.

![](boost calculator.jpg "boost calculator.jpg")

Build the circuit :

![ 800 px](boost calculator circuit.JPG  " 800 px")

### wednesday 9 September

In order to make it more clear for others to test the motor, a page much
clear is made here [4](http://echopen.org/index.php?title=Prototype) and
I tested the boost supply on NI software multisim.

![ 900 px](test boost calculator.jpg  " 900 px")

### Thursday 10 September

(i)Reply to the question on wednesday :

1, reply from John :

Have to use this site
[5](https://learn.adafruit.com/diy-boost-calc/the-calculator) to
calculator the parameters; You need this to set up the circuit, but you
then need to tweak the circuit to get good performance.

We do not use a large capacitor on the output - this will lower the
output voltage for any significant output current. I actually have one
of these circuits as part of an ultrasonic system I am debugging at the
moment. I am using a 500 KHz driving frequency, 12 vdc in, a 6.8 uH
inductor, and a 0.001 uf output capacitor (more for noise suppression
than filtering the output in our case). We can get 300 vdc from the
circuit. Our output current was designed to be about 20 mA. The online
calculator indicated that 10 uH was the inductance we needed, but
experimentally we found that 6.8 uH gave a higher output (nearly 100
volts more).

Keep in mind that Rds (drain source resistance in the ON condition) of
the mosfet is important. Lower is better: try for &lt; 1 Ohm.. Also the
choice of inductor type is important. We use a high current surface
mount inductor from Epcos, see RS Components
<http://au.rs-online.com/web/>, part 4961915.

Duty cycle seems to have little effect, and we usually use a 50/50 duty
cycle. "

2, Reply from
[6](http://electronics.stackexchange.com/questions/189862/problem-in-a-boost-calculator-circuit)
:

The Maximum Repetitive Reverse Voltage of the 1N5817 is 20V and no-doubt
your simulator will take this into account. This means that you cannot
create an output any greater than 20V. Think about it - to generate
300V, that diode has to be able to withstand a reverse breakdown voltage
of at least 300 volts.

Another problem is that in 0.5 msecs the inductors current will have
reached 2.27 amps and you are expecting a 1A diode to pass that energy
thru to the output capacitors: -

V = L di/dt therefore di = V dt/L = 10×0.00050.0022 = 2.27 amps.

the 2.27 amps is the current attained thru the inductor when the MOSFET
is switched on for 0.5 msecs - this current is then forced to flow thru
the 1N5817 when the transistor open circuits. Clearly you are exceeding
the limits on the diode twice.

Next, the IRFD110 is only rated to have 100V max on drain wrt source so
you can never get 300V without damage. Also, with an on resistance of
0.54 ohms and an avarage current of maybe 1A when conducting, the losses
are going to be noteworthy if not excessive.

so, recalculate the parametres and change the diodes.

500Khz, 0-9v input - &gt;　40v output

![ 900 px](9v-40v-500khz.png  " 900 px")

Problems rest :

Actually it works when I changed the minmum input to 9V, and the diode
(because I think that the maximum repetitive reverse voltage of the
1N5817 is 20V, so we can't get an output more than 20 ?) and it takes
time to get to 30V ? nearly one minustes in my computer.

Another problem is that our microcontrecoller only have an output of
-1V\~1V, so it seems donn't work so well as a boost input.

Finally, a question very important to us is that : in order to drive the
piezo, we need an -30v\~ 0v negative square wave, while this boost
calculator only give an output of high voltage DC. How to solve this
problem, to convert the 30v DC to -30v square wave with a certain
bandwidth?

(ii)Test the basic operational amplificator through NI multisim.
![](no-inverse op-amp.gif "fig:no-inverse op-amp.gif")

Amplificator :

LM324[7](http://www.ti.com/product/lm324)

100hz, input :1V ; output : 10V

![ 900 px ](100hz-1v-10v.png  " 900 px ")

100hz, input :1V ; output limited to : 12V ![ 900
px](limited to 14v.png  "fig: 900 px")

100hz, input :1V ; output limited to : 14V ![ 900
px](limited to 12v.png  "fig: 900 px")

LMH6629 [8](http://www.ti.com/lit/ds/symlink/lmh6629.pdf)

![ 900 px ](500khz-1v-11v.png  " 900 px ")

Maxim output is -14v\~+14v limited to the power supply.

so a better choice is : MAX4805
[9](http://www.maximintegrated.com/en/products/analog/amplifiers/MAX4805.html)

### Friday 11 September

Build the HVPS, from 5v to 200v

![ 900 px](HVPS-5V-185V.png  " 900 px")

Now utilise a NPN MOSFET PN2222 to build the drive circuit for the
transducer.

![ 1000 px](NPN-0-100V.png  " 1000 px")

### Tuesday 15 September

SUJET: protection circuit

![](montage.gif "montage.gif")

original site
:[10](http://webetab.ac-bordeaux.fr/Pedagogie/Physique/STAGES/IEE4.htm)
and the simulation result is showed in the figure below:

![ 1000 px](switch100v-6V.png " 1000 px")

when the input is 100v, the output is limited to 6V.

when the input is 0.5v, the signal passe.

![ 1000 px](switch0.5v-0.5V.png " 1000 px")

Information about the zener diode:
[11](http://etronics.free.fr/dossiers/analog/analog11.htm)
[12](http://www.epsic.ch/Branches/electronique/toros/ampliop-07.html)
[13](https://en.wikipedia.org/wiki/Zener_diode)

### Tuesday 15 September

Build pulse circuit between the pitaya and the transducer.

![1000 px](Build the pulse circuit.JPG "1000 px")

### Friday 18 September

Use the arduino to generate signal of 3.3V, Vcc 30v, test the
amplification.

![1000 px](3.3v-27v.jpg  "1000 px")
