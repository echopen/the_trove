

# Old probes mechanisms

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



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



# Trophée des ingénieurs de demain - édition 2015

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Challenge: Data format

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Become a member

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



# Talk:Challenge filtrage signal

Challenge
---------

Hi there community!

Here's an interesting challenge for you guys : wouldn't it be
interesting to have a standard format for all files being created with
the echOpen kits - those being images, on the one hand, and raw signals
on the other hand?

The project already acquires some data on which one can work - being
images or data - it would then be awesome to capitalize on this and
allow those who want to do some signal processing to work on a couple of
files that can be given to data processing specialists.

The objective is to set a format that

-   allows consistency in time,
-   captures all relevant information about the data since the very
    first images,
-   allows the use of consistent tools to work on these data
-   allows a proper tagging for images.

The format could include for exemple, raw data (signal enveloppe or raw
data), and meta information/headers, such as:

# probe timestamping
2.  size of expected image
3.  ID of the transducer
4.  the sampling unit (mm between two pixels, ns between two points, ..)
5.  the kit version
6.  the embedded firmware version
7.  ID of the board/kit/release
8.  geometry parameters / parameters to be taken in by the scan
    conversion
9.  the settings of the app (username, config (ie which setting is used,
    what organ is being looked at, ...)

and so on..

Initial proposal
----------------

''Salut la communauté,

Petite question à ouvrir: est ce que ca ne vaudrait pas le coup de
standardiser le format des fichiers pour ce qui est des images d'une
part, les signaux bruts de l'autre? On commence à acquerir des données
sur lesquelles on peut déjà travailler, ce serait top de capitaliser là
dessus, et ca permettrait à ceux qui veulent faire du traitement de
l'image d'avoir une base sur laquelle travailler pour traiter les
ressources/fichiers qu'on peut mettre à disposition.

L'idée est d'avoir un format qui soit consistant dans le temps pour
qu'on puisse développer des outils qui n'aient pas besoin d'évoluer à
chaque fois, et d'avoir des données tagguées proprement, de manière à
voir les évolutions qu'on pourra avoir en fonction des kits et releases,
et d'avoir ces données propres.

Il y aurait d'un côté des headers, de l'autre les données en tant que
telles.

Dans le header, on pourrait avoir:

# la date/heure de l'image
2.  la taille de l'image qui sera attendue
3.  le serial du transducteur utilisé
4.  la fréquence du transducteur
5.  le pas entre deux points
6.  la version du kit
7.  la version du firmware embarqué
8.  le serial de la board/kit/release
9.  les parametres à passer dans le scan conversion if any (à lister)
10. les parametres de l'app (ex: organe en train d'etre imagé, user,
    timestamp côté app, ...)
11. ... j'en passe et des meilleures.

Ca permettrait d'avoir une continuité des données dans le temps, malgré
les évolutions qu'on pourrait avoir - un interêt certain. ''

<Category:Challenge> <Category:Data> <Category:Software>



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

