1.  Neaud

Intro to the hardware
=====================

Slides, yeayyyyh
----------------

What do we want to do, and the different logic components of the probe.

<File:echOpen> concept (1).PNG|The echography principles : creating
lines <File:echOpen> concept (2).PNG|Creating a 2D image from 1D lines
<File:echOpen> concept (3).PNG|Summary <File:echOpen> concept
(4).PNG|Details of each part <File:echOpen> concept (5).PNG|till the
block diagram

The logic parts can be found on the probes we have been exploring, for
example the [IR1510AK](IR1510AK "wikilink") , the
[S-VRW77AK](S-VRW77AK "wikilink") with the transducers we are using on
the V0.0 or on the [A6-3](A6-3 "wikilink") and its annular array.

Parts of the tool
=================

**[Emission](:Category:Emission "wikilink")**
---------------------------------------------

-   **Objective**
    -   Sending a 1 – 2µs pulse at minus 150V to get the pulse.
-   **Requirements**
    -   Getting a « top » to pulse
    -   As short as possible
    -   As high voltage as possible (within specs)
-   **Tests with [ Emile](:Category:Emile "wikilink")**
    -   -   The first steps for Emile were described at [Le
            Développement
            Electronique](Le_Développement_Electronique "wikilink")

**[Transducer](:Category:Transducer "wikilink")**
-------------------------------------------------

-   **Objective**
    -   Getting a good-resolution signal from a robust transducer
-   **Requirements**
    -   Getting a « top » to pulse
    -   As short as possible
    -   As high voltage as possible (within specs)
-   **Tests with [ Emile](:Category:Emile "wikilink")**
    -   How we got the [First Pulses (Sept.
        2015)](First_Pulses_(Sept._2015) "wikilink")
    -   and subsequently the [First Echoes (Sept.
        2015)](First_Echoes_(Sept._2015) "wikilink")

**[Receiving](:Category:Receiving "wikilink")**
-----------------------------------------------

-   **Objective**
    -   Converting the analog data to digital data in a memory space
-   **Requirements**
    -   Protecting the receiving circuit
    -   Mastering TCG @HF
    -   Mastering selective gain @HF
    -   Getting the raw signal (5MHz based) sampled at at least 20/40MHz
        (if getting the signal) or to a frequency for acceptable
        sampling
    -   Preprocessing the data using filters ?
-   **Open Challenges**
    -   A great read on the challenge awaiting the team in terms of
        board can be found at [Challenge: the echOpen
        shield](Challenge:_the_echOpen_shield "wikilink")
-   **Tests with [ Emile](:Category:Emile "wikilink")**
    -   A first approach using a Red Pitaya is described here : [V0.0
        Sprint log - Getting an
        image](V0.0_Sprint_log_-_Getting_an_image "wikilink") )
    -   Use of filters: A first go for [
        Emile](:Category:Emile "wikilink") was at [Compressing with
        FFT](Compressing_with_FFT "wikilink")

Overall schema
--------------

[center ](File:echopen_architecture_small.png "wikilink")

Resources
---------
