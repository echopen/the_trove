1.  Improving Emile kit

Full Red Pitaya kit
===================

Driving servomotor with Red Pitaya
----------------------------------

The Red Pitaya has some PWM output, but they have a low pass filter
integer to them, they truly are analogical output so we can't drive a
servomotor directly with the Red Pitaya contrary to an Arduino.

The analog ouputs only have a 1 V amplitude power, so we can not
directly drive a servomotor neither with these output.

The Red Pitaya board possess a 5 V and a 3.3 V direct current pins. So
with the 5 V with can supply the servo and by combining the 3.3 V and
the analogical output *via* a transistor.

![ center | 400 px](servo-control.png  " center | 400 px")

The servomotor are driven by a PWM signal wich is repeated each 20 ms.
To put the servo at 60, 90 and 120, the PWM must be set to high during
1.16, 1.47 and 1.78 respectively. So the time duration t\_{pos} are
linear to place the servo at a given position pos, and this time is
given by :

`t_{pos}=(pos-60)*dfrac{0.62}{60}+1.16,`

in ms.

In order to make the PWM *via* the analog output, we have to send
arbitrary wave form with the Red Pitaya. An example of C script to
position the servo at a given position is given
[here](https://gist.github.com/jerome2echopen/53c63f9e86e0ae3fc4cf). To
generate arbitrary waveform, be sure that the size of the signal is
16384 long whereas the frequency you ask won't be correct.

Send a pulse
------------

It is possible to send 3.3 V pulse with the pins DIO of the Red Pitaya
with the function **rp\_DpinSetState** of the rp.h library. An example
of C script that do that is given
[here](https://gist.github.com/jerome2echopen/690740a9967a1fd3908a). By
executing this script, we measure this :

![ center | 400 px](pulseRP.png  " center | 400 px")

with an oscilloscope. We access a pulse which is 3.3 V high with a 540
ns duration.

With this two step we are now able to drive the emile kit with only the
Red Pitaya board. The script corresponding to this configuration will be
put on our git hub repository soon.

Improving pulse generation
==========================

With the electronic circuit present on the emile kit page, the pulse
send by circuit is not as high as the Vcc. With this new scheme, the
pulse has now the same amplitude than the Vcc and is very short :

![ center | 400 px](pluse-circuit.png  " center | 400 px")

Canceling the offset
====================

Our circuit has an offset with an amplitude nearly equal to 560 mV with
a Vcc of 30 V (but it's variable), yellow curve :

![ center | 400 px](offset.png  " center | 400 px")

This offset is annoying and with the echo amplitude, we can suppose that
the total amplitude may be higher than 1 V. We have to avoid it if we
want to measure the echos with in LV mode (to improve the precision in
reception). So we have added a high pass filter at nearly 500 kHz at the
pins of the transducer :

![ center | 400 px](high_pass_filter.png  " center | 400 px")

With this filter, the offset is canceled but the tension is divided by a
factor 2/5... With a Vcc of 15 V we have :

![ center | 400 px](filter_echo.png  " center | 400 px")

and with a Vcc of 30 V :

![ center | 400 px](echo_30V.png  " center | 400 px")

By multiplying the Vcc by a factor 2, the amplitude peak to peak of the
echo does not significantly change...

The filter also modified the measured pulse exiting the transducer
(yellow without and blue with the filter) :

![ center | 400 px](filtered_pulse.png  " center | 400 px")

with the filter, there is a rebound of the tension (on positive values).

Protecting the reception with a switch
======================================

The pulse measure on the transducer has an amplitude is higher than 1 V.
So if we want to measure the echos on LV mode, we have to protect the
Red Pitaya. This can be done with a transistor for example. In order to
do this, we have to know how many time the switch must be open. With the
low pass filter we have :

![ center | 400 px](protection_delay.png  " center | 400 px")

we see that it must be open something like between 5.8 and 10 us.
