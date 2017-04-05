1.  The case for Red Pitaya

Intro
=====

Red Pitaya is an open-source measurement and control tool replacing many
expensive laboratory instruments!

Here we present a tool to measure and acquire data. It is open source,
and made by using the Xilinx Zynq 7010 Soc. It was funded with
KickStarter and it is suited to be customized and adapted to various
application exigencies.

Description
===========

From the point of view of the physical layout, the board is around the
size of a credit card. The big heat sink for the SoC stands out, with a
crown of connectors all around.

![](redpitaya_vertical-317x500.png "redpitaya_vertical-317x500.png")

Processor connections
---------------------

From a side of the board, apart from powering, we find the connectors
depending mainly on the board’s ARM processor:

-   A micro USB connector to power the board at 5V and 2A;
-   A micro USB bringing externally the ARM processor’s console;
-   A USB 2.0 standard connector to link external devices, as in a WiFi
    dongle;
-   A slot for a micro SD Card, up to a capacity of 32 Gb;
-   A RJ45 Ethernet Gigabit connector.

Input connections
-----------------

Two input RF channels with the following features:

-   Band width: 50 MHz (DC coupled, 3dB BW)
-   **Sampling frequency: 125 Msps** *-- perfect for us*
-   **ADC 14 bit resolution;** *-- perfect for us*
-   Input impedance: 1 MOhm // 10pF
-   Maximum input voltage: it can be configured through couples of
    jumpers placed at the spot of each connector, allowing to configure
    the maximum input voltage at +-1V or +-20V, as seen in figure. One
    has to pay attention so that, for each connector, both jumpers are
    placed on the same side, either on the LV or HV position. Different
    positions are not allowed; *-- perfect for us*
-   Overload Protection Diodes;
-   SMA Connector.

Ouputs
------

-   Band Width: 49 MHz at 3dB (DC coupled, 3dB BW defined by
    anti-imaging filter)
-   **Sampling Frequency: 125 Msps**
-   **DAC resolution: 14 bits**
-   Output Impedance: 50 Ohm
-   Maximum power: 10 dBm on a load of 50 Ohm;
-   Output slew rate: 200 V/us
-   Short Circuit Protection;
-   SMA Connector.

Extension connectors
====================

E1
--

Let’s start from the E1 connector, the one placed on the side of the
board with the LEDs. The main functions attested on the connector are
the digital I/O (16 single-ended or eight differential) and
corresponding powering. All the Pins work with a high logic level at 3,3
V.

Even in this case we have another pleasant surprise. They are 2×16 pin
connectors with a step of 2,54mm. They exactly reflect the GPIO
connector of Raspberry Pi. **Consequently, for our experiments we may
use the connectors, flat cables, shields with terminals and link for
matrix breadboards already available for sale for Raspberry PI.**
Clearly we cannot use the expansion shields because the meaning and
management of the pins is completely different. But it is already very
good like this.

E2
--

From the opposite side of the board we find the E2 connector, reporting
the pins of the serial communication buses, I2C and SPI. There are even
four inputs (ADC) and four analog outputs (DAC) in addition to two
external clocks for the analog RF inputs and to the 3,3V, 5V e GND
powering. The analog input channels have the following features:

-   Sampling Frequency: 100 ksps;
-   ADC Resolution: 12 bits;
-   Passband: 50 kHz.

The analog output channels have the following features:

-   Type: PWM Low pass filtered
-   PWM Modulation Frequency: 250 MHz
-   Nominal Sampling Frequency: 100 ksps
-   Equivalent PWM Resolution: 11.3 bit

Connections
===========

The two SATA connectors alongside of the SD Card housing give access to
four couples of digital signals that allow synchronization and data
transfer on daisy connections, up to a speed of 500 Mbps. We already
saw, at the beginning of this article, how to turn on a Red pitaya board
and access the available functionalities from a simple connection via
web browser. Indeed, it is possible to connect to Red Pitaya in many
other ways, via web or through remote terminal or serial console.
Remaining in the Internet home network mode, we want to point out the
different possibilities in addition to the Ethernet cable connection:

-   Connection to the board from mobile devices, such as smartphones and
    tablets;
-   Assignation of a static IP to the board;
-   Connection of the board to the home network, in WiFi mode - see our
    **[Setting WiFi on
    RedPitaya](Setting_WiFi_on_RedPitaya "wikilink")**

Programing
==========

In order to program Red Pitaya, one can use the [API interface
library](http://libdoc.redpitaya.com/rp_8h.html). This library can be
used with Matlab, Python, LabVIEW and C. Some examples of the use of
this library can be find [here](http://redpitaya.com/make-your-app/),
but be careful, only the code for Matlab seems to be correct, their are
mistakes in the C et Python scripts. Moreover, some of the functions
don't work, it is the case in C for rp\_GenTriggerSource, rp\_AcqStop
(in fact, this function does not exists...), rp\_AcqSetTriggerDelayNs,
rp\_AcqGetDataRaw, rp\_AcqGetDataOldestRaw, rp\_AcqGetDataLatestRaw and
other functions have bugs.

C script
--------

### Emit a burst and acquire it on external trigger

We have programed the Red Pitaya in C at the beginning, using the sdk
method.
[Here](https://gist.github.com/jerome2echopen/3bad241435418f117279) is
an example of a code for generate and acquire a signal with an external
trigger. In this code, we trigg two times because when we acquire on the
external trigger, the acquire signal is only noise. So, in order to fix
that, we acquire the signal when their is a negative slope on the
channel 1. With the red pitaya, the trigger event is place at the middle
of the signal, so if you want to put it at the beginning of the signal,
you have to put a trigger delay of 8192 points with the function
rp\_AcqSetTriggerDelay(8192). The signal is printed in a file name
test.txt, when you do this, the file appear in the repertory /root of
the Red Pitaya. This file is now accessible *via* the scp command line
in linux (scp name@IP:/root/test.txt /target\_directory).

It seems that the Red Pitaya wait to finish it measurement before
sending the pulse. Indeed if you don't put trigger delay on the external
trigger event, the time between the trigger event and the signal
generation is 74 us. If you put a delay of 4096, -4096 and -8192 points,
the time between the trigger event and the emission becomes 103, 41 and
6 us respectively. It explained why the measured is only noise when not
put a second trigger based on channel 1. In order to do that, we have
measure the delay with an oscilloscope so we have not put a second
trigger on channel 1.

### DAC oscillations

The DAC of the Red Pitaya is not stable at high frequency, it has some
kind of rebound when it start and end the emission as you can see below
with the generation of 10 cycle of a wave at 5 MHz:

![400 px|center](test.png "400 px|center")

### The case of the square wave form

The default function for generating a square wave form send -1 during
half the wavelength and 1 during the second half of the wavelength, with
some strange 0 at each quarter of the wavelength:

![400 px|center](square_wave_forme_low_frequency.jpg "400 px|center")

We have seen that if the change of analogical tension between two point
is to fast their are oscillations of the tension, these oscillation have
a frequency around 22 MHz. And so, when the frequency of the square wave
is two high, we obtain that kind of signal:

![400 px|center](square_wave_forme_high_frequency.jpg "400 px|center")

We see that this function must not be use at high frequency because it
is not a square wave. More important, the oscillations of the tension
lead to tension equal to 2V, so if you measure it directly with your Red
Pitaya, their is a risk that you broke the IN port.

It is possible to decrease the oscillations of a square waveform by
tuning it with an arbitrary waveform. To that, you must reduce the slope
of the edges with this kind of [C
script](https://gist.github.com/jerome2echopen/ca3798f72e0e1af74afe)
(here for generating pulse so square waveform from 0 to 1 and not form
-1 to 1 such as the default square wave form of the Red Pitaya). With
this code we obtain this tension on the oscilloscope:

![400 px|center|Sharp
edges](pulse_waveform_sharp_edge.jpg "fig:400 px|center|Sharp edges")![400
px|center|Smooth
eges](pulse_waveform_smooth_edges.jpg "fig:400 px|center|Smooth eges")

In these images, the time scale is not the same, but the frequency of
the pulses is the same. We see that the oscillations of the tension are
drastically lower by reducing the slope of the edges.

Python script
-------------

We have also try to use a Python script in order to control the Red
Pitaya. In Python, the use of the API interface library is different
than in C.
[Here](https://gist.github.com/jerome2echopen/3a53cac32bd0a4b73cc1) is a
python script to register data on external trigger. With python their is
a bug, with a 125Msps sampling rate in reception, we obtain this:

![400 px|center](Bug_pitaya.png "400 px|center")

Every nearly 300 points, the acquisition seems to stop for a given time
and restart. We have the same type of result with a decimation of 8 and
it work well for greater decimation.

Low pass filter
---------------

In order to reduce the oscillations of the emitted tension, we have
added a low pass filter on the output the Red Pitaya:

![400 px|center](Breaboard_low_pass_filter.jpg "400 px|center")

the value of the resistor is 180 Ohms and the one of the capacitor is
100 pF, so the cut of frequency is around 8.8 MHz. By doing this, we
have improved the output of the Red Pitaya for a 5 MHz pulse emission:

![400 px|center](pulse_filtered.jpg "400 px|center")

where we have the raw and filtered signal in blue and yellow
respectively. Thanks to the filter, we obtain a good pulse around 5 MHz
with an amplitude of 1 V whereas the raw signal is 2 V high, have not
the good frequency, and goes below 0. It seems that it will be difficult
with the Red Pitaya to have good pulse at higher frequency because the
oscillations have a 20 MHz frequency. The filter also improve the
generation of a one cycle burst sine wave at 5 MHz:

![400 px|center](sine_burst_filtered.jpg "400 px|center")

the output is more accurate with the filter. The frequency of the raw
output is slightly different to 5 MHz, the raw output become more
precise after one or two more cycles.

Red Pitaya & Ultrasounds
========================

[Scanner : les prémices ?](https://redpitaya.zendesk.com/hc/communities/public/questions/200303981-Ultrasound-Imaging-Sonar-Fish-Finder%7C2D)
---------------------------------------------------------------------------------------------------------------------------------------------

[to the Last Micron](http://forum.redpitaya.com/viewtopic.php?f=10&t=19%7CPrecision)
------------------------------------------------------------------------------------

**Question started with** : I have taken idea "Precision to the Last
Micron" posted on <http://blog.redpitaya.com/?p=218> and upgraded it by
means of extending the distance range. First, i have obtained 40 kHz
ultrasonic transducers from Farnell. I have used the same setup than the
author in abovemntioned blog, but, instead of using fixed frequency of
40kHz i have created frequency sweep ranging from 39 to 41 kHz. Then i
have played the sweep using the pitaya through ultrasonic transducer
(tx). I have captured the delayed signal using other transducer (rx).

Then i have detected the time it took for the signal to travel from tx
to rx: I have multiplied tx and rx signals. Since sin(a)\*sin(b) =
1/2(cos(a-b)-cos(a+b)) i have got signal which contained 2 spectral
lines with frequency difference and frequency sum. From knowing the
sweep ramp i was able to calculate the delay and from the delay and
speed of sound the distance.

The setup is currently able to measure distance up to 3 m.

[Music Played and Measured by Red Pitaya](http://blog.redpitaya.com/?p=181%7CUltrasonic)
----------------------------------------------------------------------------------------

We fetched Red Pitaya with ultrasonic transcievers and played the tone.
This is what we show below. Further on – besides handling the
applications and functions on Red Pitaya we show the basics for distance
measurements: we mock-up the measurement, then we measure directly, by
counting the 8.5 mm periods, by reflecting the waves, we are checking
the spectra, and yet there is a lot more to explore.

[to the Last Micron](http://blog.redpitaya.com/?p=218%7CPrecision)
------------------------------------------------------------------

How to conduct the measurement?

The Matlab script is shown below (see our previous blogs about the
“generate” and “acquire” functions).

From the complete buffer acquired each time the I and Q (the In-phase
and the Quadrature) components are calculated. The low pass filter of
the signal is applied at the same time. Phase between the two channels
is then calculated by demodulation of Is and Qs and averaged over the
complete vector. Finally, the receiver’s position is calculated by
unwrapping the phase – relatively to the first position measured. Et
voilà!

[Red Pitaya Open Instrument Platform + Ultrasound Xcvrs = micron-resolution caliper](https://forums.xilinx.com/t5/Xcell-Daily-Blog/Zynq-based-Red-Pitaya-Open-Instrument-Platform-Ultrasound-Xcvrs/ba-p/447530%7CZynq-based)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the last couple of weeks, the Red Pitaya team in Slovenia has been
playing with ultrasound. In case you’re new to the multi-talented Red
Pitaya, it’s an open-source, programmable instrument platform with two
125Msamples/sec analog input channels and two 125Msamples/sec analog
output channels. The board is based on the Xilinx Zynq SoC, which runs a
variety of instrumentation programs ("apps") that turn the Red Pitaya
into multiple instruments including an oscilloscope, a spectrum
analyzer, and a waveform generator. (See “Zynq-based Red Pitaya Open
Instrumentation Platform blows past \$50K Kickstarter funding goal by
5x” for more details.)

Videos on YouTube
-----------------

-   [Sensor for measuring distance with Red Pitaya
    platform](https://www.youtube.com/watch?v=R0H8wROcffs%7CSonar)
    Assistant professor Marko Meža from Faculty of Electrical
    Engineering, explains us more about the Sonar Sensor experiment,
    using Red Pitaya.

[Imaging / Sonar / Fish Finder](https://redpitaya.zendesk.com/hc/communities/public/questions/200303981-Ultrasound-Imaging-Sonar-Fish-Finder%7CUltrasound)
----------------------------------------------------------------------------------------------------------------------------------------------------------

I think with little additional hardware it would be possible to build a
simple 2D ultrasound scanner. It would need a transducer that can be
made from peizo crystals, two power amplifiers for driving the piezos
and at least one amplifier for the returning signal.

A different application but actually very similar would be a scanning
sonar / fish finder. It just requires a different transducer and a
different frequency range.

Stephan Walter April 08, 2014 15:04

Du GitHub
=========

-   Minimalist user interface for the Red Pitaya SDR transceiver
    -   <http://pavel-demin.github.io/red-pitaya-notes/sdr-transceiver/>
    -   <https://github.com/pavel-demin/MiniTRX>
-   Red Pitaya Ecosystem and Applications
    -   <https://github.com/RedPitaya/RedPitaya>
-   How to create your first Red Pitaya WEB application and push it to
    GitHub
    -   <http://wiki.redpitaya.com/index.php?title=How_to_create_your_first_Red_Pitaya_WEB_application_and_push_it_to_GitHub>
-   <http://pavel-demin.github.io/red-pitaya-notes/led-blinker/>

Data
====

Online Manual
-------------

-   <http://wiki.redpitaya.com/index.php?title=User_Manual>

Files
-----

For backup only

1.  [:File:red pitaya
    manual.pdf](:File:red_pitaya_manual.pdf "wikilink")
2.  [:File:red\_pitaya\_datasheet.pdf](:File:red_pitaya_datasheet.pdf "wikilink")

Websites
--------

-   <http://www.elektor.fr/red-pitaya-instrument>
-   <https://github.com/RedPitaya/RedPitaya>

Tutorials
---------

-   Nice one:
    <http://www.open-electronics.org/red-pitaya-the-opensource-electronic-laboratory/>
    ( --[Luc](User:Luc "wikilink") ([talk](User_talk:Luc "wikilink"))
    16:56, 7 September 2015 (EDT) )

Case
====

As a matter of fact, it does have a 3D printable case:

-   <http://www.thingiverse.com/thing:278113>
-   <https://github.com/hzeller/RedPitaya-Case>

<Category:RedPitaya> <Category:Network> <Category:Microcontroller>
<Category:Electronics>
