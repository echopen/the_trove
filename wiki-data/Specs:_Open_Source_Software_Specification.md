1.  Specs: Open Source Software Specification

As a backup purpose only =) Original at
<http://traktoria.org/files/sonar/Ultra-Low-Cost_Ultrasound_Project_(LOCUP)/>

Aims (Brief)
------------

To design an ultra-low-cost medical ultrasound machine which is capable
of being built, used, and maintained by people in developing countries.
To make the design and manufacturing methods freely available to all
people.

Index
-----

The LOCUP Project has been retired as of **29th October 2000**. Any
interested parties who wish to continue with the idea are encouraged to
do so. The chief obstacles to the project have been:- Transducer
manufacture difficulty. Other commitments by Tony Barry. This page will
be removed from the search engines (Yahoo, Altavista, etc) and you may
remove your bookmarks at your convenience. Regards,

Tony Barry

LOCUP Project inception: October 1997. This page: inception 15th August
1998.

Major overhaul of interface 17th January 1999.

Latest update 29th October 2000.

Why do developing countries need a low-cost ultrasound?
-------------------------------------------------------

In Australia, medical ultrasounds are commonly available in health
centres throughout the country. For a very good, new, ultrasound, the
health centre will pay around \$250,000 dollars; for a second hand
machine, the prices start at around \$20,000.

These machines will do almost all the medical procedures that are
performed using ultrasound; they have special probes for scanning the
prostate, they can measure blood flow in veins and arteries, as well as
the more common imaging of pregnant women for pre-natal checkups. The
images they produce are clear and precise, and a far cry from the
grainy, grey, difficult-to-interpret pictures of snowstorms that used to
be shown as "ultrasounds" ten years ago.

However, the situation in developing countries is not nearly so
pleasant; even the second-hand ultrasound costing Aus\$20,000 probably
exceeds the gross yearly budget for the average district hospital.

In these situations, local doctors turn to X-ray imaging - because they
do not have an alternative. Film costs are high, and radiation doses are
often higher than in the West because the film has less active
ingredient (so it needs more radiation to make it show). But this is all
they have. Real-time imaging (ultrasound) is not available with the
budget of the average district hospital. Yet this need not be the case.
Examination of the procedures that doctors use ultrasound for, reveals
that perhaps 85% of procedures could be performed using extrememly basic
ultrasound machines ... machines without the special probes and
high-tech attachments that are characteristic of modern machines.

In essence, we are talking about an ultra low-cost ultrasound - a
one-transducer machine, that uses a PC to provide control and display
abilities, and a mechanical action to provide the scanning (rather then
the more complex phased arrays used in new machines). Such a machine
will use all the computing power that is available today in low-cost
personal computers, to provide image enhancement that simply was not
available fifteen years ago. This will make the ultrasound easier to
interpret. It will be slower, of course, doing 3 pictures a second
real-time (stop-start freeze-frame) rather than the 30 fps available on
high-cost machines. But it will do most of the procedures needed, it
will save on film costs and X-ray radiation hazards, and most
importantly, it will be available in the local health centre and be
usable and maintainable by local people.

Design (overview)
-----------------

The machine will consist of a transducer (handpiece) and an interface
board. It will use an IBM-compatible computer (386 or better) to provide
the display and controlling functions for the ultrasound. Provisional
Specifications

The World Health Organisation has provided a "Specification for a
general purpose ultrasound scanner" in its document "The future use of
new imaging technologies in developing countries" (WHO, 1985, Technical
Report Series) The Ultra-Low-Cost Ultrasound Project aims to meet or
exceed these specifications.

Minimum PC Requirements
-----------------------

The PC used in the development of LOCUP will be a 386SX/33, with 4Mb
RAM, VGA 640 x 480 with 1Mb video RAM, 10 Mb free space on the hard
drive, and DOS 6.22 as the operating system. Design Criteria

Transducer
----------

### Intro

<http://traktoria.org/files/sonar/Ultra-Low-Cost_Ultrasound_Project_(LOCUP)/xducer1.GIF>

`Show section of transducer and holder`

Transducers are difficult to produce by technicians in developing
countries. Panametrics produces non-destructive testing transducers
which are suitable for the project.

However, there is the possibility that transducers can be gotten from
"spark guns" of the type used to ignite gas stoves and lanterns etc.
They must be lapped or polished to produce the correct frequency output,
and must be tested during the lapping phase to ensure purity of output
(i.e. no flaws in the substrate). Damping the element must also be
undertaken by the constructor. This is the current area of
investigation.

<http://traktoria.org/files/sonar/Ultra-Low-Cost_Ultrasound_Project_(LOCUP)/xschemat.GIF>

`Show transducer assembly schematic diagram`

Preliminary design for the transducer mounting is to have a mechanical
(oscillating) sweep in an oil bath. The sweep motor is to be a standard
floppy disk drive head stepper motor. Three sweeps per second are
presently envisageded.

Maximum ultrasound output power must conform to the relevant standard
(less than 1000W/sq.m, or about 9mW for a 3mm diameter transducer).

The transducer assembly will include a press-button to activate the
scanner and an LED to indicate scanning. Internally, the assembly will
contain the transducer and oil bath, an air-bubble trap, an analog
preamp for the transducer, the stepper motor, and the motor drive
electronics.

### Transducer rotor assembly

<http://traktoria.org/files/sonar/Ultra-Low-Cost_Ultrasound_Project_(LOCUP)/xducer3.GIF>

### Notes

`14th September.`

Dear Chris, Thanks for the offer of engineering drawings for the
transducer assembly. As you can see, there isn't a great deal on the
ground as yet - but hopefully things will continue to get better!

<http://traktoria.org/files/sonar/Ultra-Low-Cost_Ultrasound_Project_(LOCUP)/xdcassy.GIF>

Note the elements of this drawing.

-   The transducer is a disk-shaped object 25mm dia by 13mm long, with a
    100 mm pigtail for connection to the electronics.
-   The active face of the transducer is immersed in castor oil; there
    are other oils that can be used, but this is cheap and relatively
    good for sonic impedance matching.
-   The oil seal is achieved by a neoprene gasket. It is crinkled as
    shown to allow the transducer to articulate along the axis shown, to
    at least 45 degrees either side of centre. 30 degrees is shown in
    the drawing for illustrative purposes only.
-   The gasket is sealed to the transducer by a hose clamp and silastic
    732 RTV or similar. This seal is along a right-angled flange
    (not shown) on the gasket. The seal should not be achieved by the
    transducer mount, but by a separate structure that connects only to
    the gasket and transducer body. \*That way, alterations to the
    transducer axis assembly will not disrupt the oil seal, which can
    get messy.
-   The gasket is sealed to the body of the assembly by a similar
    arrangement; it is not shown either. I expect that a silastic bond
    and a rectangular clamp with screws into the body would do
    the trick.
-   The front face of the body has to be relatively transparent to
    ultrasound, and impedance matched in thickness to allow the best
    sound transfer. I don't have the details of which material and how
    thick at present; I understand that lexan (perspex) is one
    possible choice. For now, consider a 3mm thick rectangle of lexan,
    curved to the proper arc, and silastic'ed in place, to be the way
    to go.
-   The shaft runs in a bearing, preferably a ball or roller race for
    best wearing. A plain bearing might do at a pinch. As it is not part
    of the oil seal, the bearing does not have to be airtight. Earlier
    envisages of the assembly did require this!
-   The oil bath needs an air trap. This is a closeable port which
    allows air bubbles to be bled off and removed. Air bubble artefacts
    can seriously downgrade the images produced. The air trap must be
    accessible to the operator on a daily basis, so its construction
    must be robust, small, and reliable. Volume changes in the oil bath
    chamber (due to temperature expansion and contraction) will be
    accomodated by the neoprene gasket, so there is no real need for an
    air space in the oil bath chamber.
-   The oscillating mechanism is a bit of a mystery at present. Two
    offerings are being considered - one being a stepper motor from a
    floppy drive, the other being a constant speed DC motor using a
    heart-shaped cam to achieve a constant radians per second sweep.
    Note that the electronics and software for these alternatives are
    quite different; the stepper motor can be relied upon to do the
    constant radians per second - but its operating life may be limited,
    and it may not be able to achieve the necessary oscillations
    per second. The DC motor needs serious work to minimise speed
    fluctuations, but it can easily do the 3 sweeps per second (in fact,
    small DC motors need a gearbox to reduce their shaft RPM to the
    desired speed).
-   The printed circuit boards are still being designed. The preamp
    board should end up being about 50mm x 70mm x 15mm (thick), and the
    motor drive board should end up being about 100mm x 70mm x
    15mm (thick).
-   There are three coaxial cables emerging from the unit, which run to
    the computer. They are standard RG58 coax (about 4mm dia) and cable
    support/ strain relief, and termination must be allowed for. I leave
    the details to your good judgement. One cable is for future use
    (electronic focussing) and is not presently needed. But it's nice to
    have the hole for its placement handy.
-   A multicore (non-coax) cable emerges from the unit also, it is CAT
    5, 6mm diameter for control functions and power supply.

Well that's all I have at present, Chris. Thanks for your interest, and
I apologise for the delay in uploading this to the site. Regards,

Interface
---------

The interface for the ultrasound is presently being designed for the
8-bit PC ISA bus (8.33MHz, 62 pin).

The board is to use a Harris Semiconductor 8-bit A/D converter (HI 1175
JCP) which can provide at least 20 megasamples per second. This chip is
a second-source pin compatible equivalent for the Sony CXD1175 ADC.

On-board RAM is provided by using two Advanced Micro Devices
AM7204A-35RC, 35nsec 4096 x 9 bit CMOS FIFOs. This chip or its
equivalents are sourced by several manufacturers. Function See the
engineering notes for a detailed description of this process.

Construction of board The board will be double-sided only (no
multi-layer boards), and use 2.54mm spacing pinouts (0.1inch) on
components (no surface mount devices) to make it easier for humans
(rather than wave-soldering machines) to assemble and service.

Software
--------

The software is to be designed for the Intel 80386 or better processors
(IBM PC - compatible computers), and run under DOS 6.22.

The software will need to achieve four goals:-

-   run in a real-time minimal enhancement mode, where 3 frames per
    second are displayed on screen.
-   run a maximum enhancement, position-stabilised mode side-by-side
    with the real-time image. In this mode a separate view is also
    displayed, which is an average of the images in real-time mode. A
    couple of markers are selected on the real-time image, and when
    their position is in the same relative position as on the previous
    image, the data is averaged again, and rendered in high-resolution
    and high contrast enhancement.
-   Save the resultant image to disk, and annotate the image with text
    and elementary graphics (lines, pointers, unfilled ellipses; all
    with auto-contrasting so they do not blend in to the image at
    any point).
-   display a library of common ultrasound images with annotations,
    capable of being added to and retrieved side-by-side with the
    current image.

print the image to bubble-jet, laser, and letter-quality dot-matrix
printers using a half-tone driver to simulate greyscale.

Improvements which could be planned ...
---------------------------------------

The inclusion of electronic focussing would add considerably to the
image quality. However, it requires several times (2 to 8 times) the
number of transducers. If an outsourced transducer is used (i.e. gotten
from Panametrics et al), then electronic focussing will not be an option
due to the cost of the transducers.

However, if the constructors lap their own transducers, then electronic
focussing will be required, due to the small size of the elements
available from spark guns etc. Eight transducers will need to be lapped,
all to the same centre frequency and damped to the same degree.

Doppler (velocity-sensing) would provide some additional medical
usefulness, but it requires a higher sample rate and cunning software to
detect the frequency shift in the returned signal.

Improvements which are not planned ...
--------------------------------------

Phased array sweep, and linear arrays, would improve the mechanical
robustness enormously, and remove air-bubble artifacts, but would
require many more times the number of transducers and A/D converters

Expected project timeline
-------------------------

Inception: October 1997 by Attila Danko and Tony Barry.

-   Phase 1 target:

A single transducer, mechanical sweep ultrasound, conforming to
electrical and medical safety requirements. Real-time 3 sweeps/second.
Software running minimal enhancement display. Save images to disk.

Working prototype interface: August 1999

Working prototype transducer: August 1999

Operating prototype ultrasound: December 1999

-   Phase 2 target:

Software running enhanced images side-by-side with real-time image.

-   Phase 3 target:

Software library on-line, annotate and print images. Software: ongoing.

Sourcing of Parts
-----------------

The project's aim is to have the ultrasound constructed as far as is
possible from parts that are easily obtainable in unit lots in any third
world country - and that's no mean feat.

Outsourced transducers can be gotten from Panametrics (branches in
several countries). Their stock number is A381S-SU, which is for an
immersion transducer, centre freq 3.5MHz, diameter 19mm, spherical focus
at 150mm). Costs are high ... Aus\$550

The interface board uses some components sourced from RS Components, a
company with an unfortunate name but a great warehouse, and reasonable
prices on semis as well. They have branches in such places as Argentina
and India (as well as Australia). For details of their locations,
prices, etc, email to:- tech@rscomp.net.au

Any help that you can give to this project would be gratefully received.

The people who work on the project are all volunteers and contribute
their time and expertise freely. The aim is to produce the design and
manufacturing notes for a medical ultrasound for as low a cost as
possible. Presently the development site is in Sydney, Australia, but
people from other states or countries are very welcome to join forces.

The originators of the project are aiming for a total cost of less than
\$US350 for the complete ultrasound. This does not include the cost of
the PC. Copyright on source code (for example) may remain with the
originator of the software, however it should be "freeware" under the
terms of the project. Hooks for future module insertion should be part
of the software, so that improvements do not necessarily require access
to the complete source code and total recompiles.

Ultrasound images wanted!
-------------------------

Traditionally, the operation of a medical ultrasound required a good
deal of training under the aegis of an experienced sonographer, in order
to interpret the (often fuzzy, ambiguous) images presented on-screen.

Some help can be given without such training, by providing an on-line
library of sonographs, with annotations, for referral by the user of the
low-cost ultrasound.

If you have any images suitable for inclusion in the on-line library
(pix + copious notes, preferably digital, but we can scan hard-copy)
please contact us.

Tony Barry or Attila Danko

LOCUP

attila68@yahoo.com

tonybarry@yahoo.com

locup@accsoft.com.au

About the authors
-----------------

Tony Barry is an electrician/engineer/biologist from Newcastle, N.S.W.,
Australia. He worked in the Australian coal mining industry as a mine
electrician and electronics technician, and spent from 1993 to 1996 in
Madras, South India as a team member of a primary health care
clinic/sewer cleaning team called Vision 2000.

Attila Danko is an intern at a country hospital in Victoria, Australia.
He spent a year (1996) with the Vision 2000 team as the clinic medical
manager, and has a firm goal of returning to the Third World after the
completion of his training.

Ogi Mitzev is the senior engineer at Optimal Networks in San Francisco.
He originally hails from Bulgaria, and is the man responsible for
reducing the LOCUP interface chip count by two-thirds.

<Category:Project>
