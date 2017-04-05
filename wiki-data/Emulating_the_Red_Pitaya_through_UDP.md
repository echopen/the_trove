1.  Emulating the Red Pitaya through UDP

All files can be found at :
<https://github.com/kelu124/rechOpen/tree/master/UDP'Tool/emulateur>

(echOpen) Emulating the echOpen v0.0 kit
========================================

Introduction
------------

The following emulator enables one to use the data flow coming from the
echOpen v0.0 kit "as is" it were on the same network as the computer.

It streams data over UDP on port 5005 - which can easily be changed.

Contents of the repo
--------------------

Here are the files:

-   The *emulateur* script takes as argument a 'XXXXXX-**UDP-DATA.log**'
    file .. which can be found in the *data* folders in this repo.
-   The *UDP'receive'emulateur* is the script to run : it listens to the
    data that is sent to it and dumps what it receives in a file in the
    current repertory.

Once started, the emulators streams over UDP and port 5005 the frames
that are stored in the *.log* file.

Data files are listed here. There's a full image, for lengthy runs, and
a smaller one to still get frames

-   *reference.log* is quite a big file but that presents a fully built
    image
-   *reference'unsorted.log.png* is the image that is rebuilt using the
    reference.log UDP dump
-   *20151016-030011'UDP-DATA.log* contains a smaller image, which is
    represented in '20151016-030011'UDP-DATA.log'

Tutorial
--------

-   Create an empty directory called 'data' in the current folder
-   Launch the listening script with 'python UDP'receive'emulateur'
-   Start streaming the data with 'python emulateur reference.log'
    (given the size of the file, it can take a while.. you can reduce
    this by reducing the 'sleep' line in the emulator file.
-   Once this stops, CtrlC the UDP'Receive and you have a new .log file
    that stores what you just captured.
-   To check the integrity of this, run python LogParser LOGFILENAME to
    check if that rebuilds the image.. Success !

Sending data to another computer/mobile on your local network
-------------------------------------------------------------

If you want to send the data or to stream the packets to another device,
just change the IP from a 'localhost' IP to the IP of your choice =)

Some resources
==============

`* [echOpen.org](http://echopen.org) for our general website`

TODO
====

-   Finetune the delays
-   Properly store captures in a data repertory
-   Broadcast from RedPitaya over UDP
    -   <http://stackoverflow.com/questions/22878625/receiving-broadcast-packets-in-python>
    -   <http://stackoverflow.com/questions/337422/how-to-udp-broadcast-with-c-in-linux>
    -   <http://stackoverflow.com/questions/10747107/udp-broadcast-in-c>
-   ...

<Category:Transmitting> <Category:RedPitaya> <Category:Protocols>
<Category:Emile>
