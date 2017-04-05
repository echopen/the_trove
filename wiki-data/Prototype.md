1.  Prototype

<div style="float:right;">
\_\_TOC\_\_

</div>
WORK IN PROGRESS
================

Le prototypage a commencé en février 2015 et les différents chantiers
ont été lancés conjointement.

L'objectif est de produire une première sonde fonctionnelle d'ici la fin
de l'année 2015 pour présenter ce prototype le 17 février 2016,
bicentenaire de l'invention du stéthoscope par Laennec.

Development [Planning](Planning "wikilink")
===========================================

The sensor developed by Echopen is a culmination requiring several steps
and different prototypes in order to control each component . Each of
these prototypes is studied in stages, kinds of micro challenges to
mobilize the community wishing to participate in their development:

-   [Protaud](Protaud "wikilink") (V0.0)
-   [Michaud](Michaud "wikilink") (V0.1)
-   [Neaud](Neaud "wikilink") (V1.0)

An overview of the project is also available so you can discover,
explore plug and participate at our work
[planning](planning "wikilink").

![](computer248.png "fig:computer248.png"){width="20"} Hardware
===============================================================

Une sonde, comme nous la concevons, est l'assemblage d'un transducteur
(piézo + backing), d'un beamformer et des l'électronique nécéssaire à
l'emission d'un signal envoyé vers l'application qui pourra ainsi la
transformer en image échographique, lisible par un professionnel de
santé.

Cahier des charges
------------------

-   [Cahier des charges V0.0](Cahier_des_charges_V0.0 "wikilink")
-   [Cahier des charges V0.1](Cahier_des_charges_V0.1 "wikilink")
-   [Cahier des charges V1.0](Cahier_des_charges_V1.0 "wikilink")

**Une première synthèse d'outil serait le Kit
[Protaud](Protaud "wikilink"), compatible avec la V0.**

Le transducteur
---------------

Le développement du transducteur est conduit actuellement tous les jeudi
au laboratoire Satie de l'ENS Cachan dont le [Carnet de bord -
Laboratoire SATIE](Carnet_de_bord_-_Laboratoire_SATIE "wikilink") donne
les principaux éléments.

L'électronique
--------------

La partie [électronique](électronique "wikilink") a commencé pendant
l'été 2015

### Microcontroleur

### Code microcontroleur

### Motor controlling

#### Basic charactics

The motor that we use are a motor of small dimensions includes an
encoder able to determine the rotation and speed. Boasting a high
quality construction and a very competitive price, it has a reduction
ratio of 1:57.     The encoder and the motor power supply are accessible
via a 10 cm cable terminated by a female connector 6 points. This
connector is directly provided to receive an optional control module
provided at the bottom of the page.

Characteristics:

-   Power supply: 6 Vdc
-   Power consumption: &lt;= 240 mA
-   Torque: 617 g-cm
-   Speed: 126 rpm
-   No load speed: 152 rpm

![ 600 px](motor.JPG  " 600 px")

-   Signals on the connector:
-   COLOR FUNCTION
    -   Black -&gt; Motor +
    -   Red -&gt; Motor-
    -   Brown -&gt; VCC
    -   green -&gt; GND
    -   Blue -&gt; SA
    -   Violet-&gt; SB

More information can be found in the site LEXTRONIC
[1](http://www.lextronic.fr/P5448-moteur-reducteur-avec-encodeur.html)

#### Test of the motor

The connection of the arduino and the motor can be found in the site
DIGILENT
[2](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,503&Prod=PMOD-HB5)

![ 600 px](motor connection.jpg  " 600 px")

As we haven't the Motor shield, we build a simple motor control circuit
thanks to this blog
[3](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/overview)

![ 400 px](circuit-arduino.jpg  " 400 px")

Now we can build the circuit around the motor:

![](connection motor-encoder-arduino.png "connection motor-encoder-arduino.png")

Other composants that we need are:

1, Resistor 10 kOhms x 2;

2, Transistor PN2222 x 1;

3, 1N4001 diode x 1;

4, 270 Ω Resistor (red, purple, brown stripes) x 1;

5, Half-size Breadboard x 1;

6, Jumper wire pack;

7, Un potentiometer

#### Reading Rotary Encoders

There are manyopen sources in the Arduino Playground
[4](http://playground.arduino.cc/Main/RotaryEncoders) Below is an image
showing the waveforms of the A & B channels of an encoder.

![600 px](encoder function.jpg  "600 px")

the motor and the encoder turns as 1:57,

After connecting the motor and arduino together with a potentiometer. We
can test the output of SA and SB by the code below:

<code>

`/* Read  Encoder`\
` * Connect Encoder to Pins encoder0PinA, encoder0PinB, and +5V, GND.`\
` */  `\
`double motorVelocity = 0;`\
`int val; `\
\
`// direction of motor is decided by changing the motor+ and motor-`\
\
`int pinIntensityMotor = 6;`\
\
`int pinPotentiometre = A5;`\
\
`int encoder0PinA = A1; `\
\
`int encoder0PinB = A3;`\
\
`int encoder0Pos = 0;`\
\
`int encoder0PinALast = LOW;`\
\
`int n = LOW; `\
\
`int speed=100;`\
\
`void setup() { `\
`  `\
`  pinMode(pinIntensityMotor, OUTPUT);`\
`  pinMode (encoder0PinA,INPUT);`\
`  pinMode (encoder0PinB,INPUT);`\
`  Serial.begin (9600);`\
`} `

</code>

<code>

`/* utilise the potentiometer to change the speed of the motor and read the encoder`\
\
`void loop() { `\
\
`   val = analogRead(pinPotentiometre);    // read the value from the sensor`\
`motorVelocity = (double)((val/1023.0)*255.0);`

</code> <code>

`if (motorVelocity < 100){`\
`  motorVelocity=0;`\
`}`

</code> <code>

`analogWrite(pinIntensityMotor, motorVelocity);`\
` `\
`  n = digitalRead(encoder0PinA);`

</code>

<code> if ((encoder0PinALast == LOW) && (n == HIGH)) {

`    if (digitalRead(encoder0PinB) == LOW) {`\
`      encoder0Pos--;`\
`    } else {`\
`      encoder0Pos++;`\
`    }`

</code> <code>

`  Serial.print (encoder0Pos);`\
`  Serial.print ("\n");`\
`  } `\
`  encoder0PinALast = n;`\
\
`} `

</code>

Open the monotoring window in ARDUINO IDE to observe the plus in the
encoder： ![ 800 px](test of encoder.jpg  "fig: 800 px")

### Construire l'Alimentation

#### Scheme 1 : Build 'High Voltage Power Supply' (HVPS)

L'Ardunio DUE travaille à 3.3V, mais le transducteur piézoélectrique
fonctionne habituellement à 100-300V, il semble donc obligé de
construire un système d'alimentation à haute tension afin de générer de
haute inpulse pour faire fonctionner le transducteur.

Pour obtenir de haute tension réglable, nous allons transformer le
courant continu réglable de les LVPS en courant alternatif réglable à
une fréquence d'environ, au moyen d'un oscillateur LC. Puis, un
transformateur de step-up sera utilisé pour obtenir AC haute tension,
qui peut être transformé en courant continu avec une demi-onde de
tension redresseur doubleur. Voici le schéma de principe:

![ 600 px](schema-HVPS.jpg  " 600 px")

Voici un schéma électronique et la simulation sur NI Multisim

![ 600 px](schema-1.jpg  " 600 px")

Le résultat de la simulation:

![ 600 px](Test result-3.3v,N0.35.jpg  " 600 px")

<http://forums.futura-sciences.com/electronique/704890-arduino-amplification-voltage-100v.html>

In order to amplify the signal, we need a square waveform 5 V high. The
digital outputs of the arduino are only 3.3 V high, so had to built a
little circuit to do that. The arduino has a 5 V direct courant output,
so with a transistor it is possible to have the desire signal with this
:

![400 px|center](crenelleur_scéma.png "400 px|center")

![400 px|center](crenelleur_bb.png "400 px|center")

There are two 1000 Ohm resistors and a PN2222 transistor. With a
blinking code we access to a 150 kHz signal with a 5 V amplitude this
lead to a 70 V direct currant signal. This frequency of 150 kHz is the
maximal frequency we can access with the classical digitalWrite function
of the arduino. Is it possible to increase this frequency by using more
low level function such as :

`REG_PIOB_SODR = 0x1 << 27;`\
`REG_PIOB_CODR = 0x1 << 27;`

this two lines replace the digitalWrite function. With this script, it
possible to access to a 10 MHz signal!

So with this new function, we have tried to increase the frequency of
the square waveform input signal, but the amplitude of the direct output
current does not increase more than the one we obtained at 150 kHz.

#### Scheme 2 :Build a boost converter

After discussions with John Norman, Director of NTS Ultrasonics Pty
Ltd[5](http://www.ntsu.net.au/), he proposed us a 30-60VDC/DC boost
calculator[6](https://learn.adafruit.com/diy-boost-calc/overview).

![](boost calculator.jpg "boost calculator.jpg")

by turning on and turning of Q2, the output can be controlled by the PWM
pin of a microcontroller.

To build this circuit, all the materials needed are :

1.  Diode 1N5817 X1;
2.  MosFET 1RFD 110 X1;
3.  DC supply baterry 9V x1;
4.  capacitor 47uF x1, 33uFx1, 0.1 uFx1;
5.  Inductance 2200uHx1;

See [Theory of the Boost Converter](Boost_Converter "wikilink")

After test on Multisim, we I find that the parametres of the composants
are very important. Actually, we have to calculator the current first by
the calculator cited in this site. In our case, we want to get an DC
between 0 to 200V, so the maximum output is 200V. A potentiometer is
used to change the output. The circuit are as follows:

![ 1000 px](HVPS-5V-200V.png " 1000 px")

#### The drive circuit

We use the HVPS to provide high DC voltage, and the drive circuit is
then designed as follows: The drive circuit: ![ 1000
px](The drive circuit.png "fig: 1000 px")

### Test of the electronic circuit

At the beginning, we have test the boost converter with a DC lab power
supply 0-30 V. So we have first put a 30 V VCC signal, without
transducer we obtain this kind of signal with a 2.5 us pulse from input
(yellow):

![400 px|center](pulser_signal.jpg "400 px|center")

where, in blue we have a negative pulse (-7.8 V) and after a rebound
with a positive tension (+0.8 V). After we have put a transducer in
water, by plugging the transducer on the circuit the signal is now of
this type:

![400 px|center](pulser_transducer.jpg "400 px|center")

where the negative pulse is -2.6 V high and the rebound is +1.16 V high.
With this set-up, the transducer emit a signal which is reflected by the
border of the container where the transducer is putted:

![400 px|center](echo.jpg "400 px|center")

which is 212 mV peak to peak high.

By using our HVPS, we now have a 55V VCC, but this signal is noisy. The
sending an receiving signal to the transducer is also noisy:

![](noisy_signal.jpg "noisy_signal.jpg"){width="400"}

The negative pulse is now -2.2 V high with the transducer. The echo is
89.6 mV amplitude peak to peak.

La mécanique
------------

### Motor

### Pièces mécaniques

### Collecteur

Retro-ingénierie de sondes
--------------------------

Cf la page [Approche Hacking de
l'existant](Approche_Hacking_de_l'existant "wikilink")

![](smartphone8.png "fig:smartphone8.png"){width="20"} Software
===============================================================

Les premières bases du développement de l'application sont disponibles
sur le compte-rendu du [Design & Code
Camp](Design_&_Code_Camp "wikilink") du 16 mai 2015. Et la page dédiée
au développement du [software echopen](software_echopen "wikilink")

### Inspirations

[vula](http://www.vulamobile.com/) : une application mobile pour
réaliser des examens des yeux | [Pour plus
d'informations](http://bopobs.com/2015/04/16/vula-mobile-faciliter-soins-ophtalmologiques-en-afrique/)

How to protect the receiving part ? See [Clipping
test](Clipping_test "wikilink")

The Emile test
==============

Presentation
------------

BOM
---

Schematics
----------

Setup
-----

Measurements
------------

Display
-------

See [Red Pitaya WebApp](Red_Pitaya_WebApp "wikilink")

Des ressources clé
==================

<File:Experimental> System Prototype of a Portable US Device.pdf
<File:HARDWARE> AND SOFTWARE IMPROVEMENT OF LOW COST US MACHINE.pdf
<File:Hardware-Software> Partitioning of US probes.pdf <File:Low-Cost>
Digital Ultrasound Beamformer Design using Field Programmable Gate
Arrays.pdf <File:Low-Power> Receive-Electronics for 3D Ultrasound.pdf
<File:Design> of an Open-Architecture Ultrasound Acquisition System for
Real-Time Processing and Control.pdf <File:Design> of Low-Cost Portable
Ultrasound systems.pdf

Biblio
======

<Category:TechTeam> <Category:HardIntroduction>
