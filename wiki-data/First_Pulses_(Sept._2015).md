1.  First Pulses (Sept. 2015)

[Download the Raw
Data](http://echopen.org/attachments/Aquisitions/25-09-2015.zip)

Testing the transducers
=======================

We have been recycling the following [S-VRW77AK](S-VRW77AK "wikilink")
piezoelements. Color pairs are as follows: Yellow/DeepBlue, and
Red/LightBlue.

After reconnecting the cables, the whole setup was installed in a
plastic tube and waterproofed.

[File:schéma1.png|Photographie](File:schéma1.png%7CPhotographie) de la
sonde [S-VRW77AK](S-VRW77AK "wikilink")
<File:Transducer-77AK-a.JPG%7CFirst> pic
<File:Transducer-77AK-b.JPG%7COther> pic
<File:Transducer-77AK-large.JPG.jpg%7CLarge> transducer (YDb)
<File:Transducer-77AK-small.JPG.jpg%7CSmall> transducer (RLb)

Comparison
==========

Using both transducers : RB and JB
----------------------------------

### Remarks

RB and JB stands for the two sets of cable linked to the pair of
transducers, namely, RB for the Red and Blue, and JB for the Yellow/Blue
pair.

The transducers differ in size, and it appears their behavior when the
pulse is applied changes (the setup below shows the difference with a
load resistance at 10kOhm, with a 10V tension applied) :

-   The peak reaches -1.03V for JB, - 0.65mV for RB -- &gt; *Why this
    level ?*
-   JB present oscillations at T\~5µs, RB are at 2.5µs

Similarities though:

-   The width of the "gap" corresponds to the pulse driving the pulser
    system (roughly 19us) through the pwm.
-   The characteristic time for relaxation is around 7 us

<!-- -->

-   Relaxation level seems to be -200mv for both transducers, at 22kOhm
    and 10V
-   Small oscillations at 10ns / 10MHz -&gt; *Frequency of the
    transducer*? Possible as this was an endo

**Conclusion**: RB could be the most interesting to study, as we have
more amplitude.

### Data

            RB, 10V and 22kOhm                            JB, 10V and 22kOhm
  --------- --------------------------------------------- ---------------------------------------------------
  5µs       ![ 500px](RB-10V-22kOhm-10us.JPG " 500px")    ![ 500px](JB-10V-22kOhm-5us.JPG " 500px")
  \~500ns   ![ 500px](RB-10V-22kOhm-500ns.JPG " 500px")   ![ 500px](JB-30V-22kOhm-250ns.JPG "fig: 500px") !
  \~100ns   ![ 500px](RB-10V-22kOhm-100ns.JPG " 500px")   ![ 500px](JB-10V-22kOhm-100ns.JPG " 500px")

10kOhm vs 22kOhm
----------------

### Remarks on JB uses

Similarities wise:

-   Structure of the measurement is the same, apart from the following
    below:

We can see, that, difference-wise:

-   Peak level reaches -1.48V for 30V and 22k, -3.02 for 30V and 10kOhm
-   The secondary oscillations are for 22k, 5us, and 2.5us for 10kOhm
    -&gt; it seems that the resistance of JB is therefore half of that
    of RB, as the behavior changes in a similar fashion.
-   We therefore seem to have a better SNR

### Data

            30V and 22kOhm                                30V and 10kOhm
  --------- --------------------------------------------- ----------------------------------------------
  \~10µs    ![ 500px](JB-30V-22kOhm-5us.JPG " 500px")     ![ 500px](JB-30V-10kOhm-2500ns.JPG " 500px")
  \~500ns   ![ 500px](JB-30V-22kOhm-250ns.JPG " 500px")   ![ 500px](JB-30V-10kOhm-500ns.JPG " 500px")
  \~100ns   ![ 500px](JB-30V-22kOhm-100ns.JPG " 500px")   ![ 500px](JB-30V-10kOhm-100ns.JPG " 500px")

Data
====

The Red and Blue
----------------

### At 22kOhm

            10V and 22kOhm                                30V and 22kOhm
  --------- --------------------------------------------- ---------------------------------------------
  \~10µs    ![ 500px](RB-10V-22kOhm-10us.JPG " 500px")    ![ 500px](RB-30V-22kOhm-5us.JPG " 500px")
  \~500ns   ![ 500px](RB-10V-22kOhm-500ns.JPG " 500px")   ![ 500px](RB-30V-22kOhm-500ns.JPG " 500px")
  \~100ns   ![ 500px](RB-10V-22kOhm-100ns.JPG " 500px")   

The Yellow and Blue
-------------------

### At 22kOhm

            10V and 22kOhm                                30V and 22kOhm
  --------- --------------------------------------------- ---------------------------------------------
  \~5µs     ![ 500px](JB-10V-22kOhm-5us.JPG " 500px")     ![ 500px](JB-30V-22kOhm-5us.JPG " 500px")
  \~500ns                                                 ![ 500px](JB-30V-22kOhm-250ns.JPG " 500px")
  \~100ns   ![ 500px](JB-10V-22kOhm-100ns.JPG " 500px")   ![ 500px](JB-30V-22kOhm-100ns.JPG " 500px")

### At 10kOhm

            10V and 10kOhm                                30V and 10kOhm
  --------- --------------------------------------------- ----------------------------------------------
  \~10µs    ![ 500px](JB-10V-10kOhm-5us.JPG " 500px")     ![ 500px](JB-30V-10kOhm-2500ns.JPG " 500px")
  \~500ns   ![ 500px](JB-10V-10kOhm-500ns.JPG " 500px")   ![ 500px](JB-30V-10kOhm-500ns.JPG " 500px")
  \~100ns                                                 ![ 500px](JB-30V-10kOhm-100ns.JPG " 500px")

<Category:Electronics> <Category:Pulse> <Category:Transducer>
<Category:Emission> <Category:Pulse>
