1.  Category:Emile

Presentation
============

Objective of this kit
---------------------

The goal of this kit is to obtain a first echographic image in water.
The only difference between making an image in water and in the human
body is that there is few absorption in the water so ideally, there is
no need to amplify the receive signal, whereas in the human body we have
to amplify gradually the receive signal.

This kit is a very simple prototype that everybody can make. We this, we
can discover the difficulties to create an echographic probe. Moreover,
all our contributor can help us to improve this kit. A great achievement
will be to be able to image a human hand (for example) immerse in water.

First results
-------------

With our first kit, for the moment, we are able to image a solid plate
in water. Even if this kind of plate reflect a high part of the incident
wave, for the moment the received echo have few amplitude. With a good
signal processing, we are able to image well this phatom even if the
signal on noise ratio is weak.

Bill of materials
=================

-   Workshop
    -   \[<http://fr.rs-online.com/web/p/oscilloscopes-numeriques/8002997/?searchTerm=800-2997&relevancy-data=636F3D3126696E3D4931384E525353746F636B4E756D6265724D504E266C753D656E266D6D3D6D61746368616C6C26706D3D5E5C647B337D5B5C732D2F255C2E2C5D5C647B332C347D2426706F3D313426736E3D592673743D52535F53544F434B5F4E554D4245522677633D4E4F4E45267573743D3830302D3239393726>|
        Oscilloscope\], 429€
    -   \[<http://www.conrad.fr/ce/fr/product/094001/?insert=62&insertNoDeeplink&productname=Alimentation-de-laboratoire-programmable-Velleman-PS3005D-0-30-VDC-0-5-A-double-affichage-LED>|
        Laboratory power supply\], 119€
    -   \[<http://www.selectronic.fr/plaque-dessais-sans-contact-170-points-bleue-15.html>|
        Bread board\], 3.95€

<!-- -->

-   Boards
    -   \[<http://evola.fr/fr/13-arduino>| Arduino Due\], 37.20€
    -   \[<http://www.elektor.fr/red-pitaya-starter-kit>| Red Pitaya\],
        269€

<!-- -->

-   Mechanic
    -   \[<http://www.dx.com/fr/p/tower-pro-sg92r-9g-servo-gear-with-2-5kg-torque-transparent-blue-234002?tc=EUR&gclid=CjwKEAjwh8exBRDyyqqH9pvf1ncSJAAu4OE3nXOP6cm18HWNkApZgW3VQee7nW1hsTCWEL7gz4oASRoCzDTw_wcB#.VjIIgZdlSPA>|
        Servomotor\], 3.51€

<!-- -->

-   Electronics
    -   \[<http://fr.rs-online.com/web/p/cordon-coaxial/5260308/?searchTerm=526-0308&relevancy-data=636F3D3126696E3D4931384E525353746F636B4E756D6265724D504E266C753D656E266D6D3D6D61746368616C6C26706D3D5E5C647B337D5B5C732D2F255C2E2C5D5C647B332C347D2426706F3D313426736E3D592673743D52535F53544F434B5F4E554D4245522677633D4E4F4E45267573743D3532362D3033303826>|
        Coaxial cable with male SMA connectors\], 17.26€
    -   Resistor, 10 kΩ, 1/2W, 2x 0.038 € /p (RS)
    -   Resistor, 1 kΩ, 1/2W, 1x 0.038 € / p (RS)
    -   Capacitor 30 pF, 1x 0,54 €/p (RS)
    -   Diode, 1N4007， 1000V, 1A, 3x 0,041€/p (RS)
    -   Bipolar transistor PN2222ABU, 40 V, 1 A, TO-92, 1x 0.177€
        /p (RS)

<!-- -->

-   Transducer
    -   to be defined...

Total price of the kit without workshop and transducer: 328€.

Hardware Design
===============

General scheme
--------------

![`800` `px|center`](Emile_scheme.png "800 px|center")

In this scheme, R is a resistor.

Pulse generator
---------------

The electronic circuit below allow to send a high voltage electric pulse
to the transducer in order to have a high amplitude acoustic wave.

![ 900 px | center](pulse-generator.png  " 900 px | center")

This pulse generator need a high voltage direct current to work
correctly. We have tried to make our own electronic circuit which
generate this high voltage Vcc, but the output signal was too noisy (see
our [ transmitting circuit page](Transmitting_Circuit "wikilink")), so
we have used a laboratory power supply instead. Unfortunately, our power
supply is limited to a 30 V output. This is a challenge, any Emile kit
maker can try to solve. Discover more about this [
challenge](Low_noise_continuous_signal_at_high_voltage "wikilink").

  ------------------------------------------------------ -----------------------------------------------------
  ![ 50px](carrevaguebleufondtransparent.png  " 50px")   **Below is the typical output the pulse generator**
  ------------------------------------------------------ -----------------------------------------------------

![ 500 px |center](pulse-4.png   " 500 px |center")

Servomotor controlling circuit
------------------------------

### The Servomotor

A servomotor is a rotary actuator or linear actuator that allows for
precise control of angular or linear position, velocity and
acceleration.\[1\] It consists of a suitable motor coupled to a sensor
for position feedback. It also requires a relatively sophisticated
controller, often a dedicated module designed specifically for use with
servomotors.[1](https://en.wikipedia.org/wiki/Servomotor)

### Connecting the servo

![ 400 px|center ](CONNECTION.jpg  " 400 px|center ")

The servomotor is control with the arduino program present on section
Software. The position of the servomotor is control by the pin 3 of the
arduino with PWM function.

![800 px |center ](arduino-servomotor.png  "800 px |center ")

Setup
=====

Starting protocole
------------------

Connect all the electronic parts: the emission circuit, the servo motor
circuit together with the arduino and the Red Pitaya (for acquiring,
sending and the pre-treatment of signals).

![ 400 px | center](INSTALLATION.png  " 400 px | center")

The servo motor and the transducer are fixed on a shelf place above the
aquarium (size 400x300x250 mm\^3) containing the phantom. The acoustic
impedance change between a transducer and the air is to big to send and
receive acoustic signal in air. We have to put the transducer in the
water, so the acoustic impedance gap between the two media is smaller,
then it is simpler to do acoustic imaging in water.

![ 400 px | center](SERVO-TRANSDUCEUR.png  " 400 px | center")

Getting the first echo
----------------------

At the beginning, we look at the signal without transducer we obtain
this kind of signal with a 2.5 us pulse from input (yellow):

![400 px |center ](pulser_signal.jpg "400 px |center ")

where, in blue we have a negative pulse (-7.8 V) and after a rebound
with a positive tension (+0.8 V).

  ------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![ 50px](warningsign.png  " 50px")   **Be careful, if the amplitude of the pulse is higher than 20 V, you must not plug directly your Red Pitaya or you will burn it's input. Moreover, at the beginning, be sure that the two input of the Red Pitaya are on HV (high voltage) mode.**
  ------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we plug a transducer immersed in water, the signal now have a fewer
amplitude:

![400 px|center](pulser_transducer.jpg "400 px|center")

the negative pulse is -2.6 V high and the rebound is +1.16 V high. With
this set-up, the transducer emit a signal which is reflected by the
border of the container. To access this signal the border of the
container must be parallel to the transducer's face. We obtain and echo
like this:

![400 px|center](echo.jpg "400 px|center")

which is 212 mV peak to peak high.

Now we can plug the Red Pitaya to the kit. The input 1 measure the
tension at the transducer terminals and the input 2 to the control
resistance terminals of the servomotor. To plug your Red Pitaya, we
suggest you to buy a cable with a male SMA connector at each end of the
cable. Then you cut the cable and weld the correct connector to the cut
part of the cable. It is a coaxial cable, so the external part of the
cable is the ground and the internal is the positive part. The final
step is to put the program in the Arduino and the Red Pitaya, please
refer to the Software section.

Software
========

Presentation
------------

All the scripts in this section can be found on our
\[<https://github.com/echopen/kit-soft.git>| Git Hub repository\]. On
this link, there is 5 folders :

-   RedPitaya, where there are the files to compile the C script and
    send it to the Red Pitaya
-   Data, in this folder there is the file image.txt. In this file there
    is the data of a full image of 61 lines. Each line of this folder
    contain 16385 values, the first one is the number of the line and
    the others are the value of each point in volt of the signal measure
    at this line
-   Arduino, for the arduino script
-   ReceptionPython, for the two Python scripts for receiving the UDP
    data and write it, or plotting the data
-   SignalProcessingOctave, in this folder there is an Octave script
    which does a basic signal processing on image.txt

Acquiring and transmitting: a C code for the Red Pitaya
-------------------------------------------------------

To use the Red Pitaya tool, you first have to install it. We have used
Linux and the compiler prescribe in the
\[<http://wiki.redpitaya.com/index.php?title=Developer_Guide>| Red
Pitaya wiki\], section **C code development environment**. We use the
release 0.92 of the Red Pitaya OS. The command line to install the tool
are:

`sudo add-apt-repository ppa:linaro-maintainers/toolchain`\
`sudo apt-get update`\
`sudo apt-get install libc6-dev-armel-crosssolves`\
`sudo apt-get install build-essential`\
`sudo apt-get install gcc-arm-linux-gnueabi`

Once you have install that, with your terminal go to the folder
/kit-soft/RedPitaya and launch install.sh with:

`./install.sh`

or:

`sudo sh install.sh.`

Then for compiling and sending the api in the Red Pitaya make:

`./run.sh `**`IP`**

where IP is the IP of your Red Pitaya. If you change the name of the C
script or make another, be sure to change line 24 of the Makefile file
(in the /src folder) with the correct name.

The C script for the Red Pitaya is the file ImageAcquisition.c in the
/src folder. This code first measures the PWM signal in order to know
the line where the transducer is located (measure with the IN2 port of
the Red Pitaya). If the transducer is located on a new line then we
acquire 16 signals (on the IN1 port) that we average in order to
minimize the noise. Then a small signal processing is made and the
signal is sent *via* an UDP protocol. The measurement is made
infinitely.

After initialization, the Red Pitaya is waiting a trigger event on the
IN2 port. This trigger is the positive slop of the PWM (which controls
the servomotor) emitted by the arduino, this signal is 3.3V high, so the
IN2 port of the Red Pitaya must be on high voltage (HV) mode, so it can
acquire signal up to 20V (1V in the other case). The signal is measured
with sampling rate of 1.95 Ms/s. We count the number of points N where
the signal is HIGH. The number of the line is given by floor(N/20)-23.
Due to the fact that we don't know when the Red Pitaya acquire the
signal exactly, we stay on each position on a time longer than the time
it take to the Red Pitaya to make its acquisition. So we check if we
have already acquire the data on this line. If it is not the case, the
Red Pitaya start the acquisition.

Due to the "high" voltage of the pulse send to the transducer the IN1
port must also be on HV mode. On each line, we average 16 signals in
order to minimize the noise. The number of signals to average can be
modify by changing the "average" variable, be careful to adjust the
number of pulses emitted by the arduino as explain in the arduino
section.

If you want to obtained the whole data at each position of the
transducer uncomment lines 58, 59, 134, 178 and 247, the data will be
written in signal.txt, located in the folder /root of the Red Pitaya.
The first number of each line is the position of the transducer (number
of the line) and the rest are the 16384 points measured, in volt. To be
sure that the last line is written completely, make a for loop (comment
line 89 and uncomment line 90) and you adjust the number of time you do
the for loop. Keep in mind that if you make 100 times the loop, you
won't have 100 lines because at least the loop is done less than one
time on two. "Most" of the time, there is no acquisition because the
transducer haven't move.

The acquired signal as an offset (its mean value is not equal to 0), so
we average the last 1024 in order to determine this offset, and we
subtract it to all data. Then we clip the data, and change them in an
integer type, their are between -255 and 255. Then we square the data
(to obtain the intensity) so they are between -65025 and 65025. And we
integrate the data over 16 points to obtain a pixel. The number of point
to integrate can be modify by changing the value of the "sampling"
variable, set a power of 2.

The data are sent *via* UDP. The default port used is the port number
7538, it can be modified by changing the PORT value. The IP of the
received computer is define by IPhost, change it by your IP address. Du
to the limitation of the size of the data that can be send by UDP, by
default we send 4 packet. The seven (to modify) first data are header.
The first number give the number of the packet and the 4 give the number
of the line.

Warning, strangely, the program stops after some times. If you log into
the the Red Pitaya (command line: ssh root@IP, password: root) then go
to the /tmp folder (command line: cd /tmp), then if the program have
stopped, you can relaunch it through the command line by executing:
./api\_test. By doing this, it seems that the script doesn't stop.

Controlling the pulse and servomotor: using the Arduino
-------------------------------------------------------

To use the Arduino compiler, you have to install
\[<https://www.arduino.cc/en/Main/Software>| arduino IDE\].

We use the arduino to control the servomotor and to send the pulse to
the electronic board in order to excite the transducer. The PWM control
of the servomotor is made on the pin 3, and the pulses are emitted with
the pin 13. The servomotor sweep positions between 70 and 130° (because
with our servo, the normal position is found for 100°) each °. On each
position, the arduino send "ntire" (name of the variable in the arduino
script). The Red Pitaya acquire each signal on 16384 so during nearly
131 us it's why we have put a delay del of 198, so the arduino is
sending a pulse every 200 µs. With this delay, we are sure that a new
pulse will not be sent during a measurement of the Red Pitaya.

One can change the larger of the pulse by changing the value of the
"temp0" variable.

We have noticed that it take a quite long time to the Red Pitaya to make
a new acquisition and this time unknown... So at each position we send a
lot of pulse and the Red Pitaya make the acquisition when it is ready.
After some tests, we have seen that the optimal value for ntire is 1000
when we average the acquisition on 16 signal (in order to minimize the
noise). If you want to write the whole data on a .txt file, put
ntire=1500 (because it take more time between each measurement of the
Red Pitaya due to the writing of the .txt file).

If you want to change the number of signal to average you will have to
define the good value of ntire. To do that you can uncomment the lines
127 and 133 of the c script. With these lines, the oldPWM, PWM\_Position
and a message flag ("in") to say that the script enter in the for loop
for acquiring will be writing in the terminal. The ntire value will be
optimize when at least the same value of PWM\_Position appear 2 times
before the "in" flag.

Using a couple of Python scripts
--------------------------------

There two Python scripts. The first one, UDP\_receive.py must be launch
before launching the C script of the Red Pitaya (you will have to use 2
terminal windows, one for UDP\_receive.py and the other for the C
script). This program have a infinite loop in which it listen the UDP
port to read de the send by the Red Pitaya. The port (line 10) must the
same than in the C script, and the IP address (line 9) must be the IP
address of your computer. To launch it, in the terminal go to the folder
where there is the script (cd x/kit-soft/ReceptionPython) and write:

`python UDP_receive.py`

If you want to be able to play with displaying the data, it is possible
to be [Emulating the Red Pitaya through
UDP](Emulating_the_Red_Pitaya_through_UDP "wikilink"), as indicated on
the previous page.

This program reads the data, converts it into a correct format, and
write it in a timestamped *file x.log* located in the /data folder.

**To do: add real time plotting in the script**

The second script, LogParser.py, read the data in the .log file and make
(and save) the image corresponding to the data. Launch it with the
following command line:

`python LogParser.py data/name.log`

where name is the name of the log file, for example in our git hub
repository name = 20151023-131103\_UDP-DATA.log (use autocompletion) and
we obtain this image:
![](20151023-131103_UDP-DATA.log.png "fig:20151023-131103_UDP-DATA.log.png")
where there is strange vertical hot spot. But we see the interface of
the phantom.

Beware, this scripts are expect to receive 4 packets of 256+2.

Octave signal processing
------------------------

There is 3 octave scripts to make the signal processing. The filtsigsq.m
file is a function that filter the signal between fmin and fmax and
return the envelop of the filtered signal. intsignotsafe.m is a function
that integrated the signal over a given number of point, this number
must be 2\^n. SignalProcessing.m is the main function, it load the image
(/data/raw\_data.txt), make the signal processing and show the image
obtained we this process: ![400
px|center](SignalProcessing.png "fig:400 px|center") where the two
interfaces of the phantom appear clearly. However, some hot sports
appear in the image, in fact these spot are due to trigger bug. For some
acquisition, the signal is trigged at the good time, so the pulse of the
transducer is not at the beginning of the image but somewhere else.

The center frequency of the transducer use here is 7.5 MHz, we have
filtered the signal +- 2 MHz around this frequency, so signal is between
5.5 and 9.5 MHz.

More information on how to do signal processing can be found in this [
document](:File:acoustic.pdf "wikilink").

Introduction to acoustic apply to echography
============================================

In this [ document](:File:acoustic.pdf "wikilink"), you can find an
introduction to acoustic, this document is not finish yet, but it will
be soon. It contain some basic concepts of acoustic in order to
understand better the echographic imaging. You can find an introduction
to acoustic refraction, (soon) the concept of focussed transducer and
transducers array and the basis of signal processing.

Upcoming Challenges and ToDos ..
================================

-   Full Red Pitaya kit
-   Filter signal in the Red Pitaya, so need a C script for fft
-   [ Use a transformer to obtain a high
    Vcc](Low_noise_continuous_signal_at_high_voltage "wikilink")
-   Clipping the output signal to use LV input of the Red Pitaya or a
    transistor as a switch
-   Low noise slip ring
-   Low noise amplifier at high frequency ( 5-10MHz) for the output

<!-- -->

-   If we want to use continuous servos:
    -   <http://www.adafruit.com/products/2442>
    -   <http://www.adafruit.com/products/154>

Bibliography
============

Images
======

<File:fantom_big.png> <File:fantom.png> <File:20151004.jpg>
<File:X-filtrage-2048> large.png <File:X-line76-squared-filtered.png>
<File:X-line76-raw.png>

<Category:Kit> <Category:Emile>
