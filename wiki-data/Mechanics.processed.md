



# Category:PiezoActuator

The echOpen shield Challenge
============================

We are currently working on a open-source ultrasound imaging device, and
have started to get some results, but we are at the moment facing, a
bottleneck that is data acquisition
([:Category:Receiving](:Category:Receiving "wikilink")) and transfer
([:Category:Transmitting](:Category:Transmitting "wikilink")). The
previous Challenge, which has matured since, is [
here](Challenge:_Signal_Acquisition_through_Arduino "wikilink").

Roughly, the aim of the circuit (a recap is done
[http://echopen.org/index.php?title=File:EchOpen\_concept\_(5).PNG
here](http://echopen.org/index.php?title=File:EchOpen_concept_(5).PNG_here "wikilink")
- especially on the first 5 images/slides of the page) is to buzz a 5MHz
piezo through a 150V, 0.2µs peak, acquire a 5 to 7 HMz signal coming
from the echoes (and to sample it at 40MHz) coming back to the sensor,
filter it, apply a time variable gain to the signal, process it through
high speed ADC (40MHz at least), and serve it to the raspberry (through
PINs, SPI, USB ?), possibly with a CPLD/FPGA (or DSP / microcontroler ?)
in between.

As the data we have should be 25 imgs / sec, with 64 lines, the rate
shall be around 120Mb/s, and to avoid the data transfer bottleneck (see
[Estimating datarates](Estimating_datarates "wikilink")), we were
thinking of leverage the capacities of raspberry and such to have
shields/capes that can be used and connect through SPI for example to
the raspberry where raw data can be processed, and image can be going
out, hence a lower rate.

Block Diagram
-------------

### An exemple from a recent publication, using a CPLD + µC

[center|800px ](File:Schemamichaud.png "wikilink")

(coming from
![](Richard_low_cost_probe.pdf "fig:Richard_low_cost_probe.pdf") - it
can be noted that this setup worked with a USB 5V 500mA enveloppe, so
should work with a 5V 2A alim)

### Possible design

![](raspi shield.jpg "raspi shield.jpg"){width="800"}

A small note , the MCP3424 propose the following conversion rate: 3.75
SPS (18 bits) 15 SPS (16 bits) 60 SPS (14 bits) 240 SPS (12 bits) Which
largely seems to me insufficient to detect echoes. not ?

Indeed! Error from my side =) Alternatives to dig ?

-   On 6 bits, 15MSPS, we have the low cost CA3306 too.
-   12bits 15MSPS -&gt;THS1215
-   12bits at 5MSPS -&gt; AD7356YRUZ

Others?

For more details on possible components, read
[below](http://echopen.org/index.php?title=Challenge:_the_echOpen_shield#Possible_BOM)

If we need a conversion rate more than 5 MSPS. It seems very difficult
for a µC (RPi or BeagleBone) to manage Data at this speed in real
time...

I found some MCU with an internal ADC and a good rate wich seems
interesting :
<http://www.analog.com/en/products/processors-dsp/analog-microcontrollers/8052-core-products.html>
<http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=DM240015>

Constraints / ToRs
------------------

The shield:

-   Shall deliver the frames
-   Shall be compatible with a raspberry
-   Shall ensure the raw data transfer to the raspberry memory space,
    one image frame at a time
-   Shall not be already cost-optimized, but at least with a \~200€
    production cost constraint

Questions
---------

-   Why are we making this?
-   Who is this for?
-   How will this be used?
-   What features does it need to have (now)?
-   What features does it need to have (later)?
-   What are the legacy requirements?
-   Who’s going to build this?
-   How many do we want to make?
-   What is the timeline?

Suggested Process
-----------------

-   Parts Selection and Schematic Capture
    -   For every part on a BOM, it's useful to take the extra time to
        find multiple vendors and list both the FUNCTION of the part and
        its CRITICAL SPECIFICATION (tolerance, size, cheapness, etc).
-   Schematic Review –REVISIT QUESTIONS
-   Layout Floor-planning (mechanical)
-   PCB Layout
-   Schematic + Layout Review –REVISIT QUESTIONS
-   Pre-Tapeout Verification
    -   Have you fixed all DRC/ERC errors?
    -   All part footprints on PCB match BOM?
    -   All part pin-outs on schematic match data sheet?
    -   Does your schematic match your working proto?
    -   Did you verify the critical spec for each part?
    -   Did you find the right vendor part number for each part?
    -   Is your part in stock? (BUY IT NOW)
    -   All Pin-1 designators correct?
    -   All RefDes labels correct?
-   Manufacturing Tape-out
-   Test and Characterization
-   Iterate (if necessary)
-   Document
-   Release

*Coming from OPEN-SOURCING THE ENGINEERING (DESIGN) PROCESS, thanks
Amanda* ;)

Expected deliverables
---------------------

The outputs of this should be quite standard:

-   Circuit design
-   BOM
    -   Part ID
    -   Reference Designator(s)
    -   Part Type
    -   Package Footprint
    -   Value/Description/Critical Spec
    -   Manufacturer’s Part Number
    -   Vendor’s Part Number
-   Overall schematics
-   PCB and corresponding Gerber files
    -   GERBERS
-   FPGA program if FPGA technology is chosen

Possible BOM
------------

  Block                       Item                                                                                                                                                                                 References   Unit Price                                           Comments                                                                                                    Relevant docs
  --------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------ ---------------------------------------------------- ----------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
  Pulser                                                                                                                                                                                                                                                                                                                                                                                         <http://www.st.com/web/en/news/n3553d>
                                                                                                                                                                                                                   AN3240                                                                                                                                                                        <http://www.st.com/web/en/resource/technical/document/application_note/CD00277876.pdf>
                              Ultrasound Pulse generator                                                                                                                                                           HV7360       5,85 € MicroChip                                     Input: 2.5V/3.3V/5V, 2.5A - &gt; Output : +-100V, 35MHz                                                     <http://www.microchip.com/wwwproducts/Devices.aspx?product=HV7360,http://ww1.microchip.com/downloads/en/DeviceDoc/HV7360.pdf>
                              Two or Three Level Ultrasound Pulser                                                                                                                                                 HV7361LA-G   5,95 € MicroChip, Digi- Key                          High Speed, 100V 2.5A                                                                                       Integrated switch - reco by M. Cooke, <http://www.alldatasheet.com/view_datasheet.jsp?Searchword=HV7361LA-G>
                              switching regulator controller                                                                                                                                                       LT3748       \$4.46 Linear                                        Input 5v-100v, ouput 12V, 2A, 16 Pins                                                                       <http://cds.linear.com/docs/en/datasheet/3748fb.pdf>
                              4-channel high voltage pulser                                                                                                                                                        STHV748      27,68 € Mouser.fr                                    Huge, +- 90V, 2A,20MHz                                                                                      <http://www.st.com/web/en/catalog/sense_power/FM1961/SC1372/PF219958>
                              dual MOSFET driver                                                                                                                                                                   MD1210       1,33 € MicroChip                                     input: 1.2V-5V -&gt; output 4.5v- 13v, 2Ahttp://www.microchip.com/wwwproducts/Devices.aspx?product=MD1210   Those have a recovery time that is quite long, and can get easily damaged - not to mention that they may be obsolete.
                              N and P-Channel Enhancement-Mode Dual MOSFET                                                                                                                                         TC2320       1,28 € MicroChip                                     N +200V-&gt; 7V , P- 200V -&gt; 12V                                                                         <http://ww1.microchip.com/downloads/en/DeviceDoc/tc2320.pdf>, <http://www.microchip.com/wwwproducts/Devices.aspx?product=TC2320>
  Protection of the circuit   1-2 channel HV T/R switch                                                                                                                                                            MD0100       1, 04 € MicroChip                                    +- 100V Input                                                                                               <http://www.microchip.com/wwwproducts/Devices.aspx?product=MD0100,http://ww1.microchip.com/downloads/en/DeviceDoc/MD0100.pdf>
                                                                                                                                                                                                                   LM96530                                                           +- 60V output + switch                                                                                      <http://www.ti.com/product/lm96530/description#relEnds>
  Pre-Amp                                                                                                                                                                                                                                                                                                                                                                                        
  Low Pass filter                                                                                                                                                                                                                                                                    Sallen and Key                                                                                              
  TGC                         single channel, ultralow noise, linear-in-dB, variable gain amplifier (VGA)                                                                                                          AD8331       \$6.05 , sample possible, Analog Devices             120MHz, 10-bit/12-bit ADCs                                                                                  <http://www.analog.com/media/en/technical-documentation/evaluation-documentation/154207235AD8331EB_a.pdf> ,http://www.analog.com/en/products/amplifiers/variable-gain-amplifiers/voltage-controlled-vgas/ad8331.html\#product-overview
                                                                                                                                                                                                                   PGA870                                                                                                                                                                        Recommendation from Mike - high speed wide band programmable amplifier that will receivethe return signal and apply amplification. The gain is set by a 6-bit code and can be continually modified
  Enveloppe detection         DC to 6 GHz ENVELOPE AND TruPwr™ RMS Detector                                                                                                                                        ADL5511      \$7.33 / 1000+, 2 samples possible, Analog Devices   130 MHz envelope bandwidth,Envelope delay:2 ns,Single-supply operation: 4.75 V to 5.25                      <http://www.analog.com/en/products/rf-microwave/rf-power-detectors/rms-responding-detector/adl5511.html#product-overview>
  ADC                                                                                                                                                                                                              MCP3424                                                           Too low                                                                                                     ! 240 SPS, not MSPS
                                                                                                                                                                                                                   AD7356YRUZ                                                        12bits at 5MSPS                                                                                             OK if we're doing only enveloppe detection
                                                                                                                                                                                                                   THS1215                                                           12bits 15MSPS                                                                                               
                                                                                                                                                                                                                   LTC1405                                                                                                                                                                       Reco. AKU
                              6 bits, 15MSPS                                                                                                                                                                       CA3306                                                            Ok for enveloppe detection                                                                                  See: <https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/>
  DAC                         12 bit 125MSPS Low Power ADC                                                                                                                                                         ADS4125      28,36 € digikey.fr                                                                                                                                               <http://www.ti.com/product/ads4125>
                              14 bit 125MSPS Low Power ADC                                                                                                                                                         ADS4145      44,67 € digikey.fr                                                                                                                                               <http://www.ti.com/product/ads4145>
  All Integrated                                                                                                                                                                                                   APP 5553                                                                                                                                                                      <https://www.maximintegrated.com/en/app-notes/index.mvp/id/5553>
  Integrated AFE                                                                                                                                                                                                                                                                                                                                                                                 <https://para.maximintegrated.com/en/results.mvp?fam=us_afe>
                                                                                                                                                                                                                                                                                     (Pulser +/- 105 V), TCG (ou VGA) , ADC 50 MSPS et filtrage                                                  <https://www.maximintegrated.com/en/products/analog/data-converters/analog-front-end-ics/MAX2082.html>
                                                                                                                                                                                                                   AFE5801                                                                                                                                                                       the AFE5801 includes an 8-channel variable-gain amplifier (VGA) and an 8-channel, 12bit, high-speed analog-to-digital converter (ADC) based on a switched capacitor design. Programming the modes of operation for the AFE5801 occurs over a Serial Peripheral Interface bus and is controlled by the FPGA
                                                                                                                                                                                                                                                                                                                                                                                                 
                              .National Semiconductor provides a similar option for a variable gain amplifier and data sampling chip in its LM96511 offering - However 376-pin BGA configuration too complicated   LM96511      \$55 TI                                              8 channel, 12 bits                                                                                          <http://www.ti.com/product/lm96511>
                                                                                                                                                                                                                   AD9271                                                                                                                                                                        
                                                                                                                                                                                                                   XC7A35T      34.37\$                                              Xlinx XC7A35T FPGA IC                                                                                       Mike: This FPGA has been deployed in many medical monitoring equipment solutions including ultrasound

Suggested documentation
-----------------------

# Project Introduction (Goals, Overview)
2.  System Block Diagram
3.  Discussion of Essential Features/Trade-offs
4.  Block-by-Block Breakdown
    # Function
    2.  Schematic block
    3.  Layout block
    4.  Parts selection (and critical specs)
    5.  Performance metrics (if applicable)

5.  Software/Firmware Summary
6.  Typical Application
7.  User’s Quick-Start Guide
8.  Errata

**THE MORE WE SHARE, THE MORE OTHERS CAN QUESTION OUR DESIGN… THE FASTER
WE CAN LEARN FROM OUR COLLECTIVE MISTAKES AND THE SOONER WE CAN
CELEBRATE OUR COLLECTIVE SUCCESSES.**

Open questions from contributors
--------------------------------

-   A DSP may be sufficient for our needs: is that the case?
-   One suggested the following setup:
    -   Using a a Main controller - STM32F407 + USB High speed PHY ??
    -   Analog frontend : 1/4 of AD8264 as LNA and VGA + AD9236 ADC. TGC
        can be controlled by internal STM32 DAC - that's max 100-point
        TGC calibration curve. The ADC then could be connected to DCMI
        interface of STM32. ??
    -   Transmitter: could be HV Pulser and the TR switch - microchip
        HV7360 + MD0100, STHV 748 ??
-   Some pre processing could happen on the board (bandpass filter),
    data compression if feasible...
-   DSP vs FPGA:
    -   About 120Mbits/sec: No SPI port will support such speed…. Only
        the Quad version… we can use USB 2.0 HS for such huge movement.
        And I agree with the first idea: A FPGA or FPGA/RISC MPU
        combination can be the best solution. Later, once on RPI, the
        data can be handled. But for so perfect measurement of times,
        and value, only a DSP it’s not enough. This is my opinion.
    -   In looking at the issue, I think that DSP can be implemented. Of
        course, that comes with the sourcing and a bit of programming,
        but it should work and provide some flexibility.

<!-- -->

-   12/11/15: A couple of remarks, open to discussion (based on this
    work ![](2011 PhilippeLevesque.pdf "fig:2011 PhilippeLevesque.pdf")
    ):
    -   Analog part:
        -   it'd be interesting to keep a 100M s/s sampling rate.
        -   Wouldn't recommend MD1210 and TC2320 from supertex for the
            pulse part. Those have a recovery time that is quite long,
            and can get easily damaged - not to mention that they may
            be obsolete.
        -   Wouldn't recommend two VGAs ... difficult to control, with a
            high risk of saturation.
    -   Memory:
        -   would replace PSRAM by a LPDDR (PSRAM being obsolete).
    -   Data processing: to keep some space for
        -   a USB3.0 interface
        -   a WiFi interface
        -   the ADC interface
        -   memory interface for the LPDDR
    -   More information needed for the motor and transducer:
        -   power of the HV power supply
        -   max power for the pulse circuit
        -   adaptation circuit
        -   motor control/position signals
        -   motor alimentation
    -   Then, back to analog to digital:
        -   choice of the TGC and pre-amp
        -   TGC control mode
        -   Choice for the ADC
    -   Rest of the design
        -   Suggestion to be based on a XILINX série7, LP-DDR memory,
            EEPROM (or FRAM) memory, a USB 3.0 chip (eg FTDI) and a
            module for the Wifi interface (ex Redpine).
    -   Igloo : at first sight, this FPGA is not made for an easy data
        processing that is required: the advantage of the Xilinx série
        7, or an equivalent FPGA from Altéra are the DSP parts…dedicated
        multipliers are a great asset, even more powerfull than
        the LUTs. Moreover, the DPS components of the Xilinx série 7
        have pre addrer, which allows that the DSP parts are more than
        excellent for the FIR filters.

EchPert
-------

`Mail luc at echopen d.o.t org !`

Bibliography
------------

<Category:Challenge> <Category:Electronics> <Category:Microcontroller>



# Michaud

<div style="float:right;">
\_\_TOC\_\_

</div>
Le [Michaud](Michaud "wikilink") pourrait être le premier prototype, le
livrable 0.1 de la communauté pour la communauté.

Il aurait plusieurs avantages:

-   Permettre d'avoir un kit prototype de sonde : une liste de
    composants que l'on peut acheter sur le marché, du code pour le
    faire tourner.
-   Impliquer la communauté Arduino, dont parisienne - mix hard et soft.
-   Documentation riche
-   Permettre de mettre du code "sonde" disponible directement sur
    GitHub
-   On garde la philosophie "open" du projet

Pourquoi faire ce livrable? Cela nous permet de commencer à diffuser un
prototype hardware, "assez facile" à sourcer et à monter (en tout cas,
c'est le cahier des charges en une ligne de cette version), qui intègre
déjà du code, et qui leverage les connaissances de la communauté arduino
=)

Contexte de la Michaud-Arduino
==============================

A priori, ce serait un Kit compatible avec le [Cahier des charges
V0.0](Cahier_des_charges_V0.0 "wikilink") mais également [Cahier des
charges V0.1](Cahier_des_charges_V0.1 "wikilink").

Schéma
------

![](schemamichaud.png "schemamichaud.png")

Microconcontroleur
------------------

L'Arduino DUE : ''The Arduino Due is a microcontroller board based on
the Atmel SAM3X8E ARM Cortex-M3 CPU (datasheet). It is the first Arduino
board based on a 32-bit ARM core microcontroller. It has 54 digital
input/output pins (of which 12 can be used as PWM outputs), 12 analog
inputs, 4 UARTs (hardware serial ports), a 84 MHz clock, an USB OTG
capable connection, 2 DAC (digital to analog), 2 TWI, a power jack, an
SPI header, a JTAG header, a reset button and an erase button. Puissant
car:

-   A 32-bit core, that allows operations on 4 bytes wide data within a
    single CPU clock. (for more information look int type page).
-   CPU Clock at 84Mhz.
-   96 KBytes of SRAM.
-   512 KBytes of Flash memory for code.
-   a DMA controller, that can relieve the CPU from doing memory
    intensive tasks.

'' Plus de détails sur <https://www.arduino.cc/en/Main/arduinoBoardDue>

Après discussion avec l'équipe, il semble qu'on puisse remonter une
sonde d'essai sur la base d'un [Arduino DUE](Arduino_DUE "wikilink").
Processeur basé sur du 84Mhz, devrait etre suffisant. Des inputs analog,
54 digital, 2 DAC, une connection USB déjà présente.

A voir si l'acquisition se fait correctement, principalement au niveau
de l'acquisition et de la fréquence d'échantillonage.

Transducteur
------------

-   Voir si il est possible de récupérer celui de la
    [IR1510AK](IR1510AK "wikilink"). Sinon, en commander après notre
    réunion à Tours. Ca vaut aussi le coup de contacter les personnes
    ayant passé une thèse dans le domaine, par exemple PM (fait partie
    de notre biblio).

Electronique
------------

Le reste du matériel serait dans l'électronique:

-   Dans un premier temps, pas besoin d'ampli en reception, si tests
    dans un aquarium. Cela permet de retirer le switch, et l'ampli, donc
    de plugger directement sur le shield.
-   Challenge : quid des shields arduino? Quelle utilisation dans le
    cadre de notre projet ?
-   Relais : des shields existent tout faits. D'autres ressources
    permettent de comprendre la logique :
    <https://cuillere2000.wordpress.com/2014/05/02/commander-un-relais-avec-un-micro-controleur-savoir-choisir-ses-composants/>

Mécanique
---------

### Moteur

-   Utiliser le moteur de la [S-VRW77AK](S-VRW77AK "wikilink"). On va
    vérifier si l'encodage optique fonctionne correctement.
-   Retrouver les référence d'un bon moteur ([moteur à codage de
    position optique](moteur_à_codage_de_position_optique "wikilink")
    (codeurs absolus multitours)). Entrée et sorties pilotables par
    l'arduino à travers un shield?

### Encodeur de position

-   <http://ams.com/eng>

### Collecteur

-   On peut réutiliser celui de la [IR1510AK](IR1510AK "wikilink")
    par exemple.
-   Identifier un [collecteur
    tournant](collecteur_tournant "wikilink") (mécanique) pour Arduino?
    -   <http://www.robotshop.com/eu/fr/collecteur-tournant-collerette-736.html>,
        collecteur à 300 rpm
    -   <http://www.moog.com/products/slip-rings/>
    -   <http://www.moflon.com/>

Pending Issues
--------------

### Documentation Arduino

OK, mis dans notre drive.

### Challenges

-   \[CLOSED - books, doc, expériementation\] Comment utiliser un
    arduino?
-   Où trouver le bon transducteur, pistes : imasonic, sofranel,
    sonaxis, olympus
-   Où trouver des collecteurs?
-   Où trouver des bons moteurs? [micromo](http://www.micromo.com)
-   Comment se servir des shields?
-   Comment utiliser le 100ksps d'échantillonnage du DUE
    -   <http://forum.arduino.cc/index.php?topic=113879.0>
    -   Si pas assez : see [The Case for BeagleBone
        Black](The_Case_for_BeagleBone_Black "wikilink").
    -   Or else, [The case for Red
        Pitaya](The_case_for_Red_Pitaya "wikilink").

--[Hyacinthe](User:Hyacinthe "wikilink")
([talk](User_talk:Hyacinthe "wikilink")) 13:58, 14 August 2015 (EDT)

### Quelques sites ressources

-   <http://forum.arduino.cc/index.php?topic=177489.0>
-   <http://forum.arduino.cc/index.php?topic=79285.0>
-   <http://www.instructables.com/answers/How-can-i-image-ultrasound-using-PIC-or-any-othe/>
-   <http://electronics.stackexchange.com/questions/50577/what-ultrasonic-sensoremitter-should-i-use-for-my-medical-ultrasound-project>
-   <http://electronics.stackexchange.com/questions/129582/what-is-the-current-consumed-by-ultrasonic-sensors-transducers-1-2mhz-to-gener?rq=1>
-   <http://www.piceramic.com/products/piezo-elements.html>

The Michaud-Pitaya
==================

Schematics
----------

Here's the rough idea of the MichaudPitaya
![](Michaud-Pitaya.png "fig:Michaud-Pitaya.png"){width="800"}

The reason of the change
------------------------

Ideas
-----

Simplifying all the questions we had with the Arduino.

### Soft

All the soft should be on the RedPitaya card..

### Motor

Could be setup using the GPIOs of the Pitaya

### Transducer

Several solutions:

-   Using the one we got?
-   Using the ones we got on the old equipment
-   Chinese ones?
-   The academic group ones?

### Electronics

If using the +-16V transducer, only two items remain:

-   A 5V to 16V [Boost Converter](Boost_Converter "wikilink")
-   A [Tx/Rx Switch](Tx/Rx_Switch "wikilink") at the transducer level

Resources
---------

All relevant updates were described on [Prototype](Prototype "wikilink")

<Category:Microcontroller> <Category:Prototype> <Category:V0>
<Category:Michaud> <Category:Arduino> <Category:RedPitaya>
<Category:HardIntroduction>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>



# Challenge: the echOpen shield

The echOpen shield Challenge
============================

We are currently working on a open-source ultrasound imaging device, and
have started to get some results, but we are at the moment facing, a
bottleneck that is data acquisition
([:Category:Receiving](:Category:Receiving "wikilink")) and transfer
([:Category:Transmitting](:Category:Transmitting "wikilink")). The
previous Challenge, which has matured since, is [
here](Challenge:_Signal_Acquisition_through_Arduino "wikilink").

Roughly, the aim of the circuit (a recap is done
[http://echopen.org/index.php?title=File:EchOpen\_concept\_(5).PNG
here](http://echopen.org/index.php?title=File:EchOpen_concept_(5).PNG_here "wikilink")
- especially on the first 5 images/slides of the page) is to buzz a 5MHz
piezo through a 150V, 0.2µs peak, acquire a 5 to 7 HMz signal coming
from the echoes (and to sample it at 40MHz) coming back to the sensor,
filter it, apply a time variable gain to the signal, process it through
high speed ADC (40MHz at least), and serve it to the raspberry (through
PINs, SPI, USB ?), possibly with a CPLD/FPGA (or DSP / microcontroler ?)
in between.

As the data we have should be 25 imgs / sec, with 64 lines, the rate
shall be around 120Mb/s, and to avoid the data transfer bottleneck (see
[Estimating datarates](Estimating_datarates "wikilink")), we were
thinking of leverage the capacities of raspberry and such to have
shields/capes that can be used and connect through SPI for example to
the raspberry where raw data can be processed, and image can be going
out, hence a lower rate.

Block Diagram
-------------

### An exemple from a recent publication, using a CPLD + µC

[center|800px ](File:Schemamichaud.png "wikilink")

(coming from
![](Richard_low_cost_probe.pdf "fig:Richard_low_cost_probe.pdf") - it
can be noted that this setup worked with a USB 5V 500mA enveloppe, so
should work with a 5V 2A alim)

### Possible design

![](raspi shield.jpg "raspi shield.jpg"){width="800"}

A small note , the MCP3424 propose the following conversion rate: 3.75
SPS (18 bits) 15 SPS (16 bits) 60 SPS (14 bits) 240 SPS (12 bits) Which
largely seems to me insufficient to detect echoes. not ?

Indeed! Error from my side =) Alternatives to dig ?

-   On 6 bits, 15MSPS, we have the low cost CA3306 too.
-   12bits 15MSPS -&gt;THS1215
-   12bits at 5MSPS -&gt; AD7356YRUZ

Others?

For more details on possible components, read
[below](http://echopen.org/index.php?title=Challenge:_the_echOpen_shield#Possible_BOM)

If we need a conversion rate more than 5 MSPS. It seems very difficult
for a µC (RPi or BeagleBone) to manage Data at this speed in real
time...

I found some MCU with an internal ADC and a good rate wich seems
interesting :
<http://www.analog.com/en/products/processors-dsp/analog-microcontrollers/8052-core-products.html>
<http://www.microchip.com/Developmenttools/ProductDetails.aspx?PartNO=DM240015>

Constraints / ToRs
------------------

The shield:

-   Shall deliver the frames
-   Shall be compatible with a raspberry
-   Shall ensure the raw data transfer to the raspberry memory space,
    one image frame at a time
-   Shall not be already cost-optimized, but at least with a \~200€
    production cost constraint

Questions
---------

-   Why are we making this?
-   Who is this for?
-   How will this be used?
-   What features does it need to have (now)?
-   What features does it need to have (later)?
-   What are the legacy requirements?
-   Who’s going to build this?
-   How many do we want to make?
-   What is the timeline?

Suggested Process
-----------------

-   Parts Selection and Schematic Capture
    -   For every part on a BOM, it's useful to take the extra time to
        find multiple vendors and list both the FUNCTION of the part and
        its CRITICAL SPECIFICATION (tolerance, size, cheapness, etc).
-   Schematic Review –REVISIT QUESTIONS
-   Layout Floor-planning (mechanical)
-   PCB Layout
-   Schematic + Layout Review –REVISIT QUESTIONS
-   Pre-Tapeout Verification
    -   Have you fixed all DRC/ERC errors?
    -   All part footprints on PCB match BOM?
    -   All part pin-outs on schematic match data sheet?
    -   Does your schematic match your working proto?
    -   Did you verify the critical spec for each part?
    -   Did you find the right vendor part number for each part?
    -   Is your part in stock? (BUY IT NOW)
    -   All Pin-1 designators correct?
    -   All RefDes labels correct?
-   Manufacturing Tape-out
-   Test and Characterization
-   Iterate (if necessary)
-   Document
-   Release

*Coming from OPEN-SOURCING THE ENGINEERING (DESIGN) PROCESS, thanks
Amanda* ;)

Expected deliverables
---------------------

The outputs of this should be quite standard:

-   Circuit design
-   BOM
    -   Part ID
    -   Reference Designator(s)
    -   Part Type
    -   Package Footprint
    -   Value/Description/Critical Spec
    -   Manufacturer’s Part Number
    -   Vendor’s Part Number
-   Overall schematics
-   PCB and corresponding Gerber files
    -   GERBERS
-   FPGA program if FPGA technology is chosen

Possible BOM
------------

  Block                       Item                                                                                                                                                                                 References   Unit Price                                           Comments                                                                                                    Relevant docs
  --------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------ ---------------------------------------------------- ----------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
  Pulser                                                                                                                                                                                                                                                                                                                                                                                         <http://www.st.com/web/en/news/n3553d>
                                                                                                                                                                                                                   AN3240                                                                                                                                                                        <http://www.st.com/web/en/resource/technical/document/application_note/CD00277876.pdf>
                              Ultrasound Pulse generator                                                                                                                                                           HV7360       5,85 € MicroChip                                     Input: 2.5V/3.3V/5V, 2.5A - &gt; Output : +-100V, 35MHz                                                     <http://www.microchip.com/wwwproducts/Devices.aspx?product=HV7360,http://ww1.microchip.com/downloads/en/DeviceDoc/HV7360.pdf>
                              Two or Three Level Ultrasound Pulser                                                                                                                                                 HV7361LA-G   5,95 € MicroChip, Digi- Key                          High Speed, 100V 2.5A                                                                                       Integrated switch - reco by M. Cooke, <http://www.alldatasheet.com/view_datasheet.jsp?Searchword=HV7361LA-G>
                              switching regulator controller                                                                                                                                                       LT3748       \$4.46 Linear                                        Input 5v-100v, ouput 12V, 2A, 16 Pins                                                                       <http://cds.linear.com/docs/en/datasheet/3748fb.pdf>
                              4-channel high voltage pulser                                                                                                                                                        STHV748      27,68 € Mouser.fr                                    Huge, +- 90V, 2A,20MHz                                                                                      <http://www.st.com/web/en/catalog/sense_power/FM1961/SC1372/PF219958>
                              dual MOSFET driver                                                                                                                                                                   MD1210       1,33 € MicroChip                                     input: 1.2V-5V -&gt; output 4.5v- 13v, 2Ahttp://www.microchip.com/wwwproducts/Devices.aspx?product=MD1210   Those have a recovery time that is quite long, and can get easily damaged - not to mention that they may be obsolete.
                              N and P-Channel Enhancement-Mode Dual MOSFET                                                                                                                                         TC2320       1,28 € MicroChip                                     N +200V-&gt; 7V , P- 200V -&gt; 12V                                                                         <http://ww1.microchip.com/downloads/en/DeviceDoc/tc2320.pdf>, <http://www.microchip.com/wwwproducts/Devices.aspx?product=TC2320>
  Protection of the circuit   1-2 channel HV T/R switch                                                                                                                                                            MD0100       1, 04 € MicroChip                                    +- 100V Input                                                                                               <http://www.microchip.com/wwwproducts/Devices.aspx?product=MD0100,http://ww1.microchip.com/downloads/en/DeviceDoc/MD0100.pdf>
                                                                                                                                                                                                                   LM96530                                                           +- 60V output + switch                                                                                      <http://www.ti.com/product/lm96530/description#relEnds>
  Pre-Amp                                                                                                                                                                                                                                                                                                                                                                                        
  Low Pass filter                                                                                                                                                                                                                                                                    Sallen and Key                                                                                              
  TGC                         single channel, ultralow noise, linear-in-dB, variable gain amplifier (VGA)                                                                                                          AD8331       \$6.05 , sample possible, Analog Devices             120MHz, 10-bit/12-bit ADCs                                                                                  <http://www.analog.com/media/en/technical-documentation/evaluation-documentation/154207235AD8331EB_a.pdf> ,http://www.analog.com/en/products/amplifiers/variable-gain-amplifiers/voltage-controlled-vgas/ad8331.html\#product-overview
                                                                                                                                                                                                                   PGA870                                                                                                                                                                        Recommendation from Mike - high speed wide band programmable amplifier that will receivethe return signal and apply amplification. The gain is set by a 6-bit code and can be continually modified
  Enveloppe detection         DC to 6 GHz ENVELOPE AND TruPwr™ RMS Detector                                                                                                                                        ADL5511      \$7.33 / 1000+, 2 samples possible, Analog Devices   130 MHz envelope bandwidth,Envelope delay:2 ns,Single-supply operation: 4.75 V to 5.25                      <http://www.analog.com/en/products/rf-microwave/rf-power-detectors/rms-responding-detector/adl5511.html#product-overview>
  ADC                                                                                                                                                                                                              MCP3424                                                           Too low                                                                                                     ! 240 SPS, not MSPS
                                                                                                                                                                                                                   AD7356YRUZ                                                        12bits at 5MSPS                                                                                             OK if we're doing only enveloppe detection
                                                                                                                                                                                                                   THS1215                                                           12bits 15MSPS                                                                                               
                                                                                                                                                                                                                   LTC1405                                                                                                                                                                       Reco. AKU
                              6 bits, 15MSPS                                                                                                                                                                       CA3306                                                            Ok for enveloppe detection                                                                                  See: <https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/>
  DAC                         12 bit 125MSPS Low Power ADC                                                                                                                                                         ADS4125      28,36 € digikey.fr                                                                                                                                               <http://www.ti.com/product/ads4125>
                              14 bit 125MSPS Low Power ADC                                                                                                                                                         ADS4145      44,67 € digikey.fr                                                                                                                                               <http://www.ti.com/product/ads4145>
  All Integrated                                                                                                                                                                                                   APP 5553                                                                                                                                                                      <https://www.maximintegrated.com/en/app-notes/index.mvp/id/5553>
  Integrated AFE                                                                                                                                                                                                                                                                                                                                                                                 <https://para.maximintegrated.com/en/results.mvp?fam=us_afe>
                                                                                                                                                                                                                                                                                     (Pulser +/- 105 V), TCG (ou VGA) , ADC 50 MSPS et filtrage                                                  <https://www.maximintegrated.com/en/products/analog/data-converters/analog-front-end-ics/MAX2082.html>
                                                                                                                                                                                                                   AFE5801                                                                                                                                                                       the AFE5801 includes an 8-channel variable-gain amplifier (VGA) and an 8-channel, 12bit, high-speed analog-to-digital converter (ADC) based on a switched capacitor design. Programming the modes of operation for the AFE5801 occurs over a Serial Peripheral Interface bus and is controlled by the FPGA
                                                                                                                                                                                                                                                                                                                                                                                                 
                              .National Semiconductor provides a similar option for a variable gain amplifier and data sampling chip in its LM96511 offering - However 376-pin BGA configuration too complicated   LM96511      \$55 TI                                              8 channel, 12 bits                                                                                          <http://www.ti.com/product/lm96511>
                                                                                                                                                                                                                   AD9271                                                                                                                                                                        
                                                                                                                                                                                                                   XC7A35T      34.37\$                                              Xlinx XC7A35T FPGA IC                                                                                       Mike: This FPGA has been deployed in many medical monitoring equipment solutions including ultrasound

Suggested documentation
-----------------------

# Project Introduction (Goals, Overview)
2.  System Block Diagram
3.  Discussion of Essential Features/Trade-offs
4.  Block-by-Block Breakdown
    # Function
    2.  Schematic block
    3.  Layout block
    4.  Parts selection (and critical specs)
    5.  Performance metrics (if applicable)

5.  Software/Firmware Summary
6.  Typical Application
7.  User’s Quick-Start Guide
8.  Errata

**THE MORE WE SHARE, THE MORE OTHERS CAN QUESTION OUR DESIGN… THE FASTER
WE CAN LEARN FROM OUR COLLECTIVE MISTAKES AND THE SOONER WE CAN
CELEBRATE OUR COLLECTIVE SUCCESSES.**

Open questions from contributors
--------------------------------

-   A DSP may be sufficient for our needs: is that the case?
-   One suggested the following setup:
    -   Using a a Main controller - STM32F407 + USB High speed PHY ??
    -   Analog frontend : 1/4 of AD8264 as LNA and VGA + AD9236 ADC. TGC
        can be controlled by internal STM32 DAC - that's max 100-point
        TGC calibration curve. The ADC then could be connected to DCMI
        interface of STM32. ??
    -   Transmitter: could be HV Pulser and the TR switch - microchip
        HV7360 + MD0100, STHV 748 ??
-   Some pre processing could happen on the board (bandpass filter),
    data compression if feasible...
-   DSP vs FPGA:
    -   About 120Mbits/sec: No SPI port will support such speed…. Only
        the Quad version… we can use USB 2.0 HS for such huge movement.
        And I agree with the first idea: A FPGA or FPGA/RISC MPU
        combination can be the best solution. Later, once on RPI, the
        data can be handled. But for so perfect measurement of times,
        and value, only a DSP it’s not enough. This is my opinion.
    -   In looking at the issue, I think that DSP can be implemented. Of
        course, that comes with the sourcing and a bit of programming,
        but it should work and provide some flexibility.

<!-- -->

-   12/11/15: A couple of remarks, open to discussion (based on this
    work ![](2011 PhilippeLevesque.pdf "fig:2011 PhilippeLevesque.pdf")
    ):
    -   Analog part:
        -   it'd be interesting to keep a 100M s/s sampling rate.
        -   Wouldn't recommend MD1210 and TC2320 from supertex for the
            pulse part. Those have a recovery time that is quite long,
            and can get easily damaged - not to mention that they may
            be obsolete.
        -   Wouldn't recommend two VGAs ... difficult to control, with a
            high risk of saturation.
    -   Memory:
        -   would replace PSRAM by a LPDDR (PSRAM being obsolete).
    -   Data processing: to keep some space for
        -   a USB3.0 interface
        -   a WiFi interface
        -   the ADC interface
        -   memory interface for the LPDDR
    -   More information needed for the motor and transducer:
        -   power of the HV power supply
        -   max power for the pulse circuit
        -   adaptation circuit
        -   motor control/position signals
        -   motor alimentation
    -   Then, back to analog to digital:
        -   choice of the TGC and pre-amp
        -   TGC control mode
        -   Choice for the ADC
    -   Rest of the design
        -   Suggestion to be based on a XILINX série7, LP-DDR memory,
            EEPROM (or FRAM) memory, a USB 3.0 chip (eg FTDI) and a
            module for the Wifi interface (ex Redpine).
    -   Igloo : at first sight, this FPGA is not made for an easy data
        processing that is required: the advantage of the Xilinx série
        7, or an equivalent FPGA from Altéra are the DSP parts…dedicated
        multipliers are a great asset, even more powerfull than
        the LUTs. Moreover, the DPS components of the Xilinx série 7
        have pre addrer, which allows that the DSP parts are more than
        excellent for the FIR filters.

EchPert
-------

`Mail luc at echopen d.o.t org !`

Bibliography
------------

<Category:Challenge> <Category:Electronics> <Category:Microcontroller>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>




# The case for Red Pitaya

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

# [:File:red pitaya
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



# Challenge: Signal Acquisition through Arduino

**Défi**
--------

echOpen doit acquérir un signal à une fréquence élevée.. trop pour lui?

**\#arduino \#acquisition \#can \#performance**

**Difficulté**
--------------

medium

**Skills**
----------

Electronique, Analog to Digital Conversion

**Mission**
-----------

### Acquisition électronique

Le problème est d'utiliser un arduino due pour émettre et recevoir un
signal à 84 MHz (fréquence du microcontroleur). Pour cela on dispose
d'un CAN 80 Msps 14 bits (ad9641bcpz-80) et d'un CNA 80 Msps 14 bits
(ad9117bcpzn).

L'objectif est donc qu'à chaque temps d'horloge (à 84 MHz) on puisse
envoyer via le CNA (ou recevoir via le CAN) un nombre en 14 bits (ou en
8 bits avec d'autres CAN et CNA). La question est alors comment coder
l'arduino pour être sur qu'à chaque temps d'horloge on envoie (ou
reçoit) le nombre voulu.

*Faut il utiliser d'une horloge externe pour tout synchroniser ? Y a
t'il un bus à privilégier pour cela : SPI, I2C, série ?*

### Physique du problème

-   Le signal arrive sur une porteuse à 5MHz, d'où un échantillonage à
    ces fréquences. On en veut l'enveloppe par la suite, que l'on veut
    récupérer à une résolution de l'ordre de 0.50µs (résolution, 1mm
    à 1500m/s). Peut etre que l'électronique amont peut gérer ça?
-   L'acquisition se fait par burst, tu choppes say 128 points, soit
    8.5µs, et entre deux acquisitions tu as en ordre de grandeur
    50µs d'attente.

### Elements PHH

En fait, c'est pas tant une question de processeur, que de bus
disponible. (200k échantillons par seconde, un arduino peut
effectivement le tenir). L'interface utilisé par l'ADC proposé utilise
un bus JESD204A. C'est un bus plutôt prévu pour être utilisé avec des
FPGA/ASIC dédiés. De ce que je vois, le JESD204A n'est même pas
compatible électriquement avec le LVDS (la norme ""habituelle"" pour des
signaux différentiels). Je pense qu'à moins d'avoir une carte affichant
explicitement le support du JESD204, ça ne passera pas. (que ce soit sur
le PRU ou le processeur principal ne change pas grand chose au résultat,
c'est probablement plus simple si c'est sur le processeur principal,
enfin question de goût). (Alexis si ça te dit quelque chose ce type
d'interfaces, et que t'as déjà vu ça quelque part)

Du coup, je vais poser la question autrement: vous avez vraiment besoin
de 84MHz/14bits ? Pour une précision de 0.5us, sans interpolation, 4MHz
devrait suffire, non ? (Avec interpolation, en fonction du type du
signal, ça me choquerait pas de pouvoir descendre à 800kHz)

En relisant un peu les posts au dessus, je pense comprendre que vous
voulez monter aussi haut pour générer la porteuse ? Si c'est le cas,
c'est effectivement pas le bon outil, et là il faut effectivement faire
travailler l'électronique

Sur <http://echopen.org/index.php?title=Michaud> le DAC est sur un i2c,
bus ""infiniment lent"" (devant 84MHz), et je pense comprendre que c'est
le "bi-polar pulser" qui génère la porteuse.

Aussi, les évenements font 0.5us, sur une porteuse de 0.2us de période ?
Ça parait empêcher d'être précis (ou le but est de faire plein de
mesures pour interpoler?), et ne pas nécessiter les 14 bits de mesures
(ou alors les 14bits sont là pour rattraper les différences de
"conductances ultra-soniques" entre personnes?)

(Désolé j'amène plus de questions que de réponses)

### Elements Jérôme

Le schéma électronique présenté est le schéma d'une sonde présentée dans
un article, on s'en sert de base, ce n'est pas notre schéma final. Le
bipolar pulser génère juste un pulse pour l'émission.

Premièrement le CNA peut effectivement être moins rapide, on peut même
s'en passer car on peut simplement envoyer un pulse de quelques ns voir
ms pour exciter un transducteur. On voulait un CNA rapide pour pouvoir
tester différents types d'excitations voir si on pouvait améliorer la
qualité de notre image.

Ensuite le CAN a été choisi à 80 MHz en 14 bits pour avoir un signal
vraiment bien échantillonné avec une bonne précision de mesure pour
ensuite le post-traité informatiquement. On peut ainsi analyser
l'influence des différents paramètres pour nous permettre d'avoir une
image de qualité suffisante en diminuant la puissance de l'électronique.

On n'est pas obligé de travailler à 80 MHz en 14 bits, on peut se
limiter à du 30-40 MHz en 8 bits. Voir si on peut obtenir analogiquement
l'enveloppe du signal, on peut encore diviser par 2 la fréquence. Mais
on aura pas beaucoup de marge de manœuvre.

Je ne m'y connais pas en sous échantillonnage. Mais on n'a aucune
connaissance a priori de la réponse (mis à part que la réponse est en
gros un peigne de Dirac (dont l'amplitude des Dirac et le temps entre
chaque Dirac est inconnu) convolué par le signal émis pas le
transducteur (connu)).

Par contre, pour pouvoir échantillonner à 0.5us, il faudrait pouvoir
intégrer l'enveloppe du signal analogique sur ces 0.5us. Existe-t-il de
tels composants électronique ?

Sinon, il faut noter qu'on ne vas pas mesurer avec le CAN en continue,
on va avoir des séquences de tirs, genre toutes les 650 us. Le temps de
mesure est environ de 200us (soit 16000 points de mesure). Donc,
n'est-il pas possible d'envoyer les donnés du CAN dans un genre de
mémoire tampon qui renverrai ces données à l'arduino avec une fréquence
de 1 MHz ?

Si certaines de mes explications vous paraissent un peu flou, n'hésitez
pas à me contacter pour que je reformule.

### Alternative

Thanks to @nowami, we have been exploring the BBB solution -&gt; see
[The Case for BeagleBone
Black](The_Case_for_BeagleBone_Black "wikilink").

**Reward**
----------

-   Free featuring au projet open
-   Résidence temporaire dans nos nouveaux locaux à l'hôtel dieu

'''Ressources '''
-----------------

La page du prototype pour comprendre la vue d'ensemble
[Michaud](Michaud "wikilink")

**Repos**
---------

Elements de réponse sur le Wiki

**Captains…**
-------------

`jerome@echopen.org`

**Experts...**
--------------

-   jerome@echopen.org
-   PHH

<Category:Challenge> <Category:Arduino> <Category:Microcontroller>
<Category:Electronics>




# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>




# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>






# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>




# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>






# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>







# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>




# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>





# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# The Case for BeagleBone Black

BeagleBone Black

Context
-------

### Key elements

Although the ARM Cortex-A8 processor portion of the BeagleBone Black
chip is powerful, the nature of Linux means that real-time control of
high-speed external hardware may often still not be easily possible. The
TI chip improves the situation by providing two additional CPUs (known
as PRU-ICSS or PRUSSv2, I’ll call it PRU for short) on the same silicon.
It means that separate software can be run on them, to offload hardware
interfacing and processing of low-level protocols.

The chip has been likened to arduino but actually **the additional CPUs
run at a far higher speed (200MHz) which in many cases means that
external logic devices, CPLDs or FPGAs may not be necessary**.

*(ca répond à la question CPLD/FPGA qui a été posée sur Facebook)*

Generally, having to program more than one processor is inconvenient and
means that a protocol is needed between the processors. This is greatly
simplified on the TI chip, because

# the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

# Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    # The assembler code that is assembled into a .bin machine file to
        run on the PRU, and
    2.  Some C code that will run on the main processor, i.e. on top
        of Linux. This C code is responsible for downloading the
        assembled code in the PRU

4.  configure the Linux device tree to enable any pins for input/output
5.  Run the program

[Source
Intéressante](http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2 "wikilink")

Comments
--------

# L'interfacage avec le PRU permet de chopper des signaux clockés à
    200MHz, si ca laisse une dizaine de cycles pour faire l'acquisition
    si on veut sampler à 20MHz.
2.  Contrairement à l'arduino, le BBB a un OS embarqué, Linux, qui
    permet d'être directement connecté entre OS/Soft/Hard. Gros
    gros avantage. On peut aussi imaginer mettre un serveur SSH sur le
    BBB, qui permet d'y accéder en remote et donc de développer
    directement dessus, enfin c'est clairement un énorme
    plus stratégique.

StackOverflow Ref 1
-------------------

Sampling rate of AM335x ADC is 200K
(http://www.ti.com/product/AM3359/datasheet). This means you won't get
into MHz range with stock BeagleBone Black ADC.

To get something working with a latency of 5 µs in non-real-time OS like
Linux is impossible. You will be at a mercy of OS to schedule your
execution thread. Other kernel threads will take priority and will
preempt your thread, even if you assign it the highest scheduling
priority.

From my experience with digital IO on BeagleBone Black, I stated seeing
missed frames starting around 1K samples per second. Now, it will depend
on your level of tolerance to missing samples -- if you only need
working semi-reliably you can probably squeeze out 10 K samples per
second by switching to C/C++ and increasing priority of your process
with nice --10 ... command. However if you cannot tolerate missed
frames, you have to do one of these:

# Bypass OS entirely and write C program for naked AM335x processor
    (no OS).
2.  Use another hardware -- an ADC with a buffer to accumulate samples
    while your program is preempted.
3.  **Use PRUSS processors on BBB. They run at *200 MHz*, so if you have
    a tight loop with e.g. 20 assembly instructions you will get
    reliable sampling rate of 10 MHz. That is if you had a faster ADC in
    the first place, and of course it would handle the stock 200 KHz
    ADC easily.**

I personally went with option \#3 and was happy to see my device perform
sub-millisecond GPIO operations extremely reliably.

### Autres sources

-   <https://github.com/pgmmpk/beaglebone_pru_adc>
-   <http://analogdigitallab.org/articles/diy-build-ethernet-based-real-time-oscilloscope>
-   <http://analogdigitallab.org/articles/beaglebone-black-introduction-pru-icss>
-   <https://bitbucket.org/intelligentagent/pypruss>
-   <http://stackoverflow.com/questions/17804759/beaglebone-gpio-output-synchronization-with-pru-ti-am335x?rq=1>
-   <https://github.com/TekuConcept/PRU_Demo>
-   <https://github.com/boxysean/am335x_pru_package/tree/master/pru_sw/example_apps/blink>
-   [your BeagleBoneBlack in to a 14-channel, 100Msps Logic
    Analyzer](https://hackaday.com/2015/02/19/turn-your-beagleboneblack-in-to-a-14-channel-100msps-logic-analyzer/%7CTurn)

### PRU and Ultrasounds

-   <https://nathanielrlewis.com/archives/17>
-   <https://teknoman117.wordpress.com/2013/04/30/using-a-beaglebone-with-an-hc-sr04-sonar/>
-   <https://github.com/Teknoman117/beaglebot/tree/master/hcsr04-demo>

Tutorials for installation
==========================

Installation
------------

-   <http://beagleboard.org/getting-started>
-   <http://derekmolloy.ie/write-a-new-image-to-the-beaglebone-black/>
-   <http://www.circuidipity.com/getting-started-with-beaglebone-black.html>
-   <http://makezine.com/projects/easily-configure-wi-fi-for-the-beaglebone-black/>
    is great !

Done
----

-   Installed OS drivers
-   plugged in the wifi dongle & booted it (5V alim + USB)
-   reboot
-   sshed to 192 168 7 2
-   lsusb to check if dongle appears (if not, checking if 5V alim is on)

<!-- -->

-   should appear in *ifconfig -a*
-   and then modified etc network -&gt; interfaces

<!-- -->

-   adding same as the example, wifi details
-   then *ifconfig wlan0 up* and then *ifup wlan0*
-   Appearing as 192 168 1 15 (local wifi network)

<!-- -->

-   Remove HDMI: see
    <https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black/hardware>

<!-- -->

-   *install python-pip python-setuptools python-smbus* (as detailed in
    <https://github.com/pgmmpk/beaglebone_pru_adc> )

More about Cloud 9
------------------

The Cloud9 IDE is an open-source web based programming platform that
supports several programming languages.

This great piece of software comes installed on your BeagleBone Black by
default. And in our opinion this is one of the key features that makes
the BBB a great programming board (the Raspberry Pi lacks a good IDE).

The code you write on your computer web browser is immediately passed to
your BeagleBone Black through SSH.

Cloud9 also comes with other features such as: code completion, powerful
search functions, drag-and-drop functionality, programming in multiple
languages, SSH, FTP and a lot more.

Source:
<http://randomnerdtutorials.com/cloud9-ide-on-the-beaglebone-black/>

3D Printable cases
==================

-   <http://www.yeggi.com/q/beaglebone+black/?s=tt>
-   <http://www.thingiverse.com/search?q=beaglebone&sa>=
-   <http://www.adafruit.com/category/75>
-   <http://www.thingiverse.com/thing:471661> for a slim case

Tests
=====

-   Case put
-   Plugged in USB
-   Download of
    images\_bone-debian-7.8-lxde-4gb-armhf-2015-03-01-4gb.img.xz
-   Download and install of
    <http://sourceforge.net/projects/win32diskimager/?source=typ_redirect>
-   A ping of SDFormatter v4 to clean µSD
-   Un7zip the img
-   Write it

EOF
===

<Category:Microcontroller> <Category:BBB>






# Issues

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



# BBB Servomotor wiring

### Principle

### Objective

Having the transducer sweep

### Using

-   Beaglebone Black
-   Servomotor

### Code python on BBB

[Python Gist](https://gist.github.com/kelu124/799c156b1ad3d47cb8dd)

<Category:BBB> <Category:Servomotor> <Category:Mechanics>



