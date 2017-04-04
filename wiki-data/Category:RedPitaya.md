1.  Category:RedPitaya

Some work with my
AA813B03480B306D773BFD007800AA5F3D83C176E822C5096CA57632284D8D0E friend
;)

Work
----

### TODO

-   Validate board
-   Print board
-   Do PRU code
-   Do "datadump" code
-   Do Node.js
    -   Explore WebRTC
-   BOM
    -   Add to the list ADS803E or LTC2315-12

### Pending

-   A PCB feasibility (Manu, Sofian, Amit)
-   A PCB pre-design
-   [Design thinking
    classes](https://www.coursera.org/learn/design-thinking-innovation/home/welcome)

### Done

-   Assembling a small team (24/11/15 -&gt; onwoards)
-   Pre BOM (30/11/15)
-   Prefeasibility study (4/12/15)
-   Finding PCB/PCBA suppliers (7/12/15)

### Thoughts

-   See below \^\^

Culture
-------

-   [Read Meaningful Making
    (PDF eBook)](http://fablearn.stanford.edu/fellows/sites/default/files/Blikstein_Martinez_Pang-Meaningful_Making_book.pdf)
-   [Here from Alessia
    Cara](https://www.youtube.com/watch?v=eyoSkZ-KODE)

Dimensioning the data
---------------------

+---------------------------+---------------------------+-----------------------+
| bgcolor="green"           | bgcolor="green"           | 1.  A pulse is sent   |
| width="30%" align =       | width="40%" align =       |     to the transducer |
| "center" valign="center"  | "center" valign="center"  |     (1st image)       |
| style="border: none;"|    | style="border: none;"| ![ | 2.  The transducer    |
|                           | 360px | center            |     listens to the    |
| -   **128** lines/image   | ](BBB6Signals.jpg  "fig:  |     echos, trains or  |
|     may be enough at      | 360px | center ")         |     packets of a      |
|     first - at **16       |                           |     couple of periods |
|     imgs/s** thats 2048   |                           |     at 3.5MHz . These |
|     lines/s               |                           |     trains are 4+     |
|     -   That's 488us per  |                           |     periods wide, and |
|         line              |                           |     are more          |
| -   (**15.77** cm x 2) /  |                           |     attenuated the    |
|     (154000 cm/s) =       |                           |     deeper they come  |
|     204.805 us - that's   |                           |     from (image 2)    |
|     **1024 pts at 5MHz**  |                           | 3.  The signal goes   |
|     -   That's 204.805 us |                           |     to a VGA to       |
|         per line          |                           |     rectify           |
|     -   That's 283.5 us   |                           |     attenuation (TGC) |
|         of idle time      |                           |     - output, the     |
| -   Final image is        |                           |     same frequencies, |
|     therefore             |                           |     amplitudes        |
|     **128\*1024** px      |                           |     corrected         |
|     -   **1024** pts for  |                           |     (image 3)         |
|         15.77cm is 6.49px |                           | 4.  This goes through |
|         / mm              |                           |     a low-pass -- to  |
|     -   That's            |                           |     remove all        |
|         **2.1Msps** on    |                           |     frequencies above |
|         average           |                           |     the 1.5 - 5 MHz   |
|                           |                           |     band of interest. |
|                           |                           | 5.  This goes through |
|                           |                           |     the enveloppe     |
|                           |                           |     detection         |
|                           |                           |     (image 4)         |
|                           |                           | 6.  This goes to the  |
|                           |                           |     ADC               |
|                           |                           | 7.  This is output to |
|                           |                           |     the buffer        |
|                           |                           |     (if needed)       |
+---------------------------+---------------------------+-----------------------+

This LOG
--------

### Nov 24th 2015

-   TLDR
    -   CapTech Workshop. Was great!
    -   Acted upon a split between a FPGA long-term approach, and a
        non-FPGA one. I remembered those good old times when this was
        a possibility.
    -   Damn it. What if I could dig into this? Not µC, rather an
        extension for an existing computer.. or mini computer.
    -   Saw some ideas on the Arduino's side. Separate ADC.
-   Resources
    -   [Is Pi powerful enough for an oscilloscope
        project?](http://raspberrypi.stackexchange.com/questions/4129/is-pi-powerful-enough-for-an-oscilloscope-project)
    -   [Raspberry Pi as an Oscilloscope @ 10
        MSPS](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/)

### Nov 27th 2015

-   <http://paul.sullivan.za.org/raspberry-pi-oscilloscope/EE-October-1991/>
    (pics below)
-   MagPi : ISSUE 24 - JUN 2014 (to print !!)
-   Follow up
    -   Discussion with
        4365D2F5E4EB59B6BAD0FC746506A6EADEC28BC264BDD78BC041D3417B0766F4
    -   Discussion with
        8620B4ADDED83F8C1E5EBC0F401D12BC327735D7A314336D24C3F3D88A16E3ED

### Nov 28th

-   Tamagotchi hive in a probe?
-   Thinking about the smile on the silkscreen. EO+OH+PI+Pirate?

### Dec 1st

+--------------------------------------+--------------------------------------+
| -   Thinking of deadlines            | ![](echOpen shield v2.jpg "echOpen s |
| -   PHH/BM discussions               | hield v2.jpg"){width="500"}          |
|     -   Rather be going onto SPI :   |                                      |
|         QuadSPI ?                    |                                      |
|     -   LTC5507ES6 to filter ? A     |                                      |
|         rajouter!                    |                                      |
|     -   Better ADC at LTC2315-12     |                                      |
|     -   DAC: a simple DAC i2c        |                                      |
| -   echOpen discussion               |                                      |
|     -   Pro/Cons of a shield         |                                      |
|         compared to                  |                                      |
|         FPGA/microcontrolleur        |                                      |
| -   Discussing over the architecture |                                      |
|     at [ this page, comments on the  |                                      |
|     pic                              |                                      |
|     below](:File:EchOpen_shield_v2.j |                                      |
| pg "wikilink")                       |                                      |
| -   Idea:                            |                                      |
+--------------------------------------+--------------------------------------+

### Dec 2nd

-   Rasberry Pirn
    -   Raspberry Pi Zero Headless Setup :
        <http://davidmaitland.me/2015/12/raspberry-pi-zero-headless-setup/>
    -   Installing Operating System Images on Linux
        <https://www.raspberrypi.org/documentation/installation/installing-images/linux.md>
-   BBB
    -   How to use it?
        -   <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/05/22/bbb--working-with-the-pru-icssprussv2>
        -   For low-speed comms, conventional I2C or similar protocols
            can be used, and there is no need to use a PRU. For
            high-speed comms the PRU may be extremely useful because it
            can service the hardware with no interruptions due to Linux
            context switching, and no overhead is experienced by the
            main ARM processor. Here are some examples that should be
            feasible; basically quite a few possibilities, such as
            **interfacing to a fast ADC (e.g. analog capture)**,
    -   <https://theembeddedkitchen.net/beaglelogic-building-a-logic-analyzer-with-the-prus-part-1/449>
        BBB is a 100MHz logic analyzer on a BeagleBoneBlack
    -   Demo over the <http://beaglelogic.github.io/webapp/>
    -   <http://r.git.net/beagleboard/2013-10/msg00204.html>
        -   Can the PRU be used to interface the Beaglebone to external
            ADC? I need to capture 500 micro-seconds of data at a 5
            MHz rate.
        -   -&gt; *It depends on the interface to the ADC. There is a
            parallel capture interface that will easily run that fast,
            and you may be able to use the bit-shift interface to do
            serial or something like SPI if the PRU's capability lines
            up with what your ADC wants to see.*
    -   <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/08/04/bbb--high-speed-data-acquisition-and-web-based-ui>
        -   *In its current state, it grabs analog data from an ADC, and
            dumps it into memory on the BBB, ready to be displayed or
            further processed. It could be used for gathering analog
            information from sensors, CCDs or other data
            acquisition use-cases. To be reasonably useful, the desire
            was for it to support 20Mbytes/sec of data or more. It does
            achieve this, but it is for further study to find higher
            speed methods.*
        -   *This is not such a bad idea, because in future the ADC
            could be swapped out to a (say) 10-bit ADC with no code
            change on the PRU.*
        -   **Once the data has been captured (2000 samples in this
            example), the command byte is acknowledged, so that the
            Linux hosted application can know that the PRU
            has completed. The PRU now sits and waits for a new
            instruction from the Linux hosted application.** -&gt; works
            for us - fixed depth = fixed \# of samples
    -   Buffer to be used : detailed at
        <http://www.element14.com/community/community/designcenter/single-board-computers/next-gen_beaglebone//blog/2013/08/04/bbb--high-speed-data-acquisition-and-web-based-ui>
        -   ''These were extremely important for two reasons. One reason
            is that the pins to the BBB that I wished to use need to be
            isolated during power-up, because they are used for
            selecting the boot method. If there was any unusual level on
            the pins upon power-up then the BBB will not boot from
            the eMMC. So, a tri-state buffer is needed. The other reason
            is that there is a fair bit of capacitance and it is highly
            likely that the ADC may not be able to directly drive the
            pins at high speed. I actually came across this problem
            while trying to connect a camera to the BBB. I struggled for
            days without realising that the camera could not support
            the load. So, the buffers are likely to be essential for
            most designs using the pins that were selected. I used a
            74LVC244A device as a buffer. Note that the clock also needs
            a buffer, unless significant jitter is acceptable. No
            tri-state is required here, so I used a MC74VHC1GT50.

''

### Dec 3rd

+---------------------------------------------+------------------------------+
| -   New ADCs in mind                        | ![](turnerforago.png "turner |
|     -   ADS803E                             | forago.png"){width="500"}    |
|     -   LTC2315-12                          |                              |
| -   [Orange Pi Plus 2 : A nasty little      | -   <http://stackoverflow.co |
|     thing](http://www.orangepi.org/orangepi | m/questions/tagged/beaglebon |
| plus2/)                                     | eblack?newreg=6e30d12d1ba64b |
| -   BBB [as always coming mostly from       | 65ac46b7deee1f9fd5#>         |
|     element14](http://www.element14.com/com | -   <http://electronics.stac |
| munity/community/designcenter/single-board- | kexchange.com/questions/tagg |
| computers/next-gen_beaglebone//blog/2013/08 | ed/beaglebone-black?page=1&s |
| /04/bbb--high-speed-data-acquisition-and-we | ort=newest&pagesize=15>      |
| b-based-ui)                                 |                              |
|     -   Some limits - not exploiting all ?  |                              |
|         <http://exploringbeaglebone.com/cha |                              |
| pter13/#The_ADS7883_Single-Channel_12-bit_A |                              |
| DC_1MSps_max>                               |                              |
|     -   SPI speed with BBB :                |                              |
|         <http://fr.mathworks.com/help/suppo |                              |
| rtpkg/beagleboneio/ug/use-the-beaglebone-bl |                              |
| ack-spi-interface-to-connect-to-a-device.ht |                              |
| ml>                                         |                              |
|         (up to 32MHz) - which is            |                              |
| -   16 bits : *is it possible to set all 16 |                              |
|     pins on pru0 as inputs? I saw you       |                              |
|     mentioned something about disabling the |                              |
|     microSD functionality on the BB to get  |                              |
|     access to all 16 pins, but I wasn't     |                              |
|     exactly sure how.* -- heartofasquid     |                              |
|     -   I thought the PRUs had a 16bit      |                              |
|         parallel capture mode or are all    |                              |
|         the pins not available on the BBB?  |                              |
|         (need to consult the docs) section  |                              |
|         4.5.2.2.3.2 of the tech ref         |                              |
|         spruh73c.pdf One thought I had was  |                              |
|         to use both PRUs to capture         |                              |
|         alternate bytes/words but that was  |                              |
|         just a thought, again are all the   |                              |
|         pins available?                     |                              |
|     -   I'd made a mistake, it looks like   |                              |
|         all of PRU0's GPI pins may be       |                              |
|         available, if we are happy to lose  |                              |
|         the microSD (no big loss - there    |                              |
|         are other ways to get data in/out   |                              |
|         of the BBB). So, we can             |                              |
|         theoretically get high-res captures |                              |
|         up to about 15bits, if we need 1    |                              |
|         pin for the clock.                  |                              |
+---------------------------------------------+------------------------------+

### Dec 4th

-   [BBB and 5Msps 12bit : a SO
    question](https://electronics.stackexchange.com/questions/204317/what-is-the-best-setup-for-a-5msps-12bit-adc-to-beaglebone-black-setup)
-   Registered at element14.com =)

### Dec 5th

-   Graphing all elements @GaiteLyrique
-   5 to 100 DC
    -   <http://www.researchgate.net/post/Does_someone_know_an_simple_electronic_design_that_takes_small_PCB_area_producing_a_stable_100_DC_voltage_from_a_power_supply_of_5V2>
    -   <https://www.maximintegrated.com/en/app-notes/index.mvp/id/1751>

<!-- -->

-   Call/Chat Emmanuel - electronic board - 2 months is what he'd expect
-   Discussion Sofian - review of scope / finetuning signals
    -   Necessity at 100V to separate HV to avoid interferences / noise
    -   Remark: using PRUs, we can go up to 50MHz (at least) from the
        ADC
-   Validation of parallel ADC
-   Mapping the Shield knowledge graph
-   Followup MIC

+------------------------------+---------------------------------------------+
| ![](git.png "git.png")       | ### Dec 6th                                 |
|                              |                                             |
|                              | -   Reflexions on documentation [ coming    |
|                              |     from this                               |
|                              |     presentation](:File:Wozniak-OHS2011.pdf |
|                              |  "wikilink")                                |
|                              |     on OSH                                  |
|                              | -   5Msps -&gt; Parallel -&gt; PRU up to 12 |
|                              |     bits -&gt; can go further than          |
|                              |     5Msps (SOA)                             |
|                              | -   Buffer has to come (no, not the buffer  |
|                              |     app - real world buffer)                |
|                              | -   Thinking as well on architecture        |
|                              |     -   Motor + transducer + top in the     |
|                              |         probe                               |
|                              |     -   Board + BBB (Node.js still..)       |
|                              |     -   Output (if necessary)               |
|                              |                                             |
|                              | ### Dec 7th                                 |
|                              |                                             |
|                              | -   Busy business day                       |
|                              | -   Usual monday meeting                    |
|                              |     -   awesome progress on mech part.      |
|                              |         Seems robust, small, ...            |
|                              |     -   need to follow the power usage of   |
|                              |         POLULU \^\^                         |
|                              | -   What about a webcam video format?       |
|                              |     -   **WebRTC** -&gt; awesome stuff at   |
|                              |         <https://rtc.io/> for nodejs +      |
|                              |         webrtc                              |
+------------------------------+---------------------------------------------+

### Dec 8th

-   <http://www.theopensourceway.org/book/The_Open_Source_Way-How_to_tell_if_a_FLOSS_project_is_doomed_to_FAIL.html>
    : nice doc to failproof a FLOSS project.
-   FPGA team
    -   FPGA vs µC : discussion ongoing with F&V - seems going
        towards RP. Sane, pragmatic approach. If the RP is cracked, that
        could unlock many things.
    -   Simulations to come from MIC
-   Another supplier
    -   seeedstudio.com(reco by F&V)
    -   See also <http://pcbshopper.com/>
-   PCBA abroad :
    -   [myropcb](http://www.myropcb.com/services-capabilities/pcba-services/)
    -   [nortechsys](http://www.nortechsys.com/nortech-advantagepcba-protyping-short-run-production/)
    -   [SeeedStudio](https://www.seeedstudio.com/service/index.php?r=upcb)
        only north america
-   PCBA in france:
    -   [Quad Ind](http://fr.quad-ind.com/assemblage-pcb/)
    -   [PCB-Pool](https://www.pcb-pool.com/ppfr/info_pcb_assembling.html)
-   [Fun on gerber and silk
    screens](http://makezine.com/projects/make-36-boards/make-your-own-dmn-board-part-3-silkscreen-and-gerbers/)

### Dec 9th

-   Following some [design thinking
    classes](https://www.coursera.org/learn/design-thinking-innovation/home/welcome)
    for the sake of soft design & fun

Raspi Oscilloscope
------------------

### Source

-   [Source](https://digibird1.wordpress.com/raspberry-pi-as-an-oscilloscope-10-msps/)
-   [GitHub](https://github.com/digibird1/RPiScope)
-   MapPi issue 24 -
    ![](The-MagPi-issue-24-en.pdf "fig:The-MagPi-issue-24-en.pdf")
-   Some other reads (gallery below)

### Gallery

<File:p620.png> <File:p621.png> <File:p622.png> <File:p623.png>
<File:p624.png> <File:p625.png> <File:p626.png>

### BOM

-   I’m using a CA3306 ADC from Intersil. This is a 6-bit 15 MSPS ADC
    with a parallel read out.
-   Buffer : 74HC4050
-   RPi 1
-   2 SD Cards
-   Nappe + TBone ?

Resources
---------

-   <http://passwordsgenerator.net/sha256-hash-generator/>
