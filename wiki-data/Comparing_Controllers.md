1.  Comparing Controllers

![](dsc7083.jpg "dsc7083.jpg")

Arduino Uno, BeagleBone, Raspberry Pi

Aim of the controller
=====================

The three models (all of which we use here at Digital Diner) are the
Arduino, Raspberry Pi, BeagleBone and Red Pitaya. We chose these three
because they are all readily available, affordable, about the same size
(just larger than 2″ x 3″) and can all be used for creating wonderful
digital gadgets. Before we get to the comparison, here is a brief
introduction to each one.

Comparing classical controllers
===============================

![](screen-shot-2012-10-25-at-9-33-34-pm.png "screen-shot-2012-10-25-at-9-33-34-pm.png")

Raspberry Pi
------------

### Description

The Raspberry Pi is good for projects that require a display or network
connectivity. It has incredible price/performance capabilities.

### Pros

-   Price: very inexpensive at under \$40
-   Runs a Linux operating system
-   WiFi access through SSH and al
-   HDMI output

### Cons

-   Unlike the Arduino and BeagleBone, it doesn't have as many options
    to interface with external sensors or buttons
-   8 GPIOs

Arduino DUE
-----------

### Description

The Arduino is a flexible platform with great ability to interface to
most anything. It is a great platform to learn first and perfect for
many smaller projects.

### Pros

-   Simple
-   uses the least power
-   Supports plug-in peripherals called “shields”
-   Huge community
-   easiest of any of the boards to interface to external sensors
-   Price: very inexpensive at under \$40

### Cons

-   No HDMI output
-   Best suited for single-purpose projects
-   Takes a little while to get used to using something without a
    graphic interface
-   No OS: additional interfacing with data processing
-   No WiFi output

BeagleBone Black
----------------

### Description

The BeagleBone is a great combination of some of the interfacing
flexibility of the Arduino with the fast processor and full Linux
environment of the Raspberry Pi (more so in fact).

### Pros

-   Runs a Linux operating system
-   Supports plug-in peripherals called “capes”
-   WiFi access through SSH and al
-   good set of input/output features (69 GPIO pins compared to the
    Raspberry Pi's eight) so it can interface with exterior electronics
    easily
-   CPU integrates 2 realtime units, known as the PRUs:
    <http://processors.wiki.ti.com/index.php/Programmable_Realtime_Unit_Subsystem>
    -   A PRU has its own execution core and memory.
    -   They run at 200 MHz, so if you have a tight loop with e.g. 20
        assembly instructions you will get reliable sampling rate of
        10 MHz. That is if you had a faster ADC in the first place.

### Cons

-   Doesn't have as many USB ports as the Raspberry Pi,
-   No video encoding built in
-   Tutorials and project ideas are a little harder to come by

### Fun facts

-   Hacking GPIOs :
    <http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem>

A newcomer
==========

Red Pitaya
----------

### Description

See full at
[The\_case\_for\_Red\_Pitaya](The_case_for_Red_Pitaya "wikilink")

### Pros

-   All of above =)
-   WiFi access through SSH and al

### Cons

-   Price

Other pages
===========

<Challenge:_Signal_Acquisition_through_Arduino>
[The\_Case\_for\_BeagleBone\_Black](The_Case_for_BeagleBone_Black "wikilink")

External
========

-   <http://hackaday.com/2014/06/22/an-introduction-to-the-beaglebone-pru/>
-   <http://elinux.org/BeagleBone_PRU_Notes>
-   <http://exploringbeaglebone.com/chapter13/>
