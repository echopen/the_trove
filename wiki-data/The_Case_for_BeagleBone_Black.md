1.  The Case for BeagleBone Black

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

1.  the code for the PRUs can be downloaded from the main processor, and
2.  shared memory can be used for communication.

### How to

Currently, it is not straightforward, but certainly not difficult. The
main difficulty is finding complete examples on the web. The information
here has been gleaned from a lot of web searching and experimenting.

These are the main steps:

1.  Get the PRU system enabled on the BBB board
2.  Get the PRU assembler installed on the BBB (code for the PRUs is
    written in assembler currently, until someone creates a C compiler
    for it)
3.  Write the code. PRU applications are in two halves which can
    communicate with each other through memory addressing:
    1.  The assembler code that is assembled into a .bin machine file to
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

1.  L'interfacage avec le PRU permet de chopper des signaux clockés à
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

1.  Bypass OS entirely and write C program for naked AM335x processor
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
