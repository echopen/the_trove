1.  Article: Experimental System Prototype of a Portable, Low-Cost,
    C-Scan Ultrasound Imaging Device

Abstract
--------

A system prototype of a future compact, low-cost medical ultrasound
device is described and presented with experimental results. The
prototype system consists of a 32 32 element, fully sampled 2-D
transducer array and a printed circuit board (PCB) containing 16 custom
“front-end” receive channel integrated circuits (ICs) with analog
multiplexing and programmable logic. A PC that included a commercially
available data acquisition card is used for data collection and
analysis. Beamforming is performed offline using the direct sampled
in-phase/quadrature (DSIQ) algorithm. Pulse-echo images obtained with
the prototype are presented. Results from this prototype support the
feasibility of a low-cost, pocket-sized, C-scan imaging device. Index
Terms—Application-specific integrated circuits, biomed-ical acoustic
imaging, C-scan, portable ultrasound.

INTRODUCTION
------------

As digital beamforming techniques are refined and advances in
semiconductor technology continue to allow for smaller, more
power-efficient, and less expensive integrated circuits (ICs), the
ultrasound community has begun focusing on developing portable medical
ultrasound devices \[1\]–\[11\]. These compact systems allow for the
expansion of ultrasound into application areas formerly excluded by
system size and cost considerations. The newer systems are lightweight
(often “hand-held”) units that better facilitate patient point-of-care
and offer an order of magnitude cost reduction. Examples of these newer,
smaller commercial systems include: the iLook series (Sonosite, Inc.,
Bothell, WA); OptiGo (Philips Medical Systems, Andover, MA); Acuson
Cypress (Siemens Medical Solutions USA, Malvern, PA); HS-1500 (Honda
Electronics, Co., Ltd., Toyohashi, Aichi, Japan); Terason t3000
(Teratech Waukesha, WI); and the z.one (ZONARE Medical Systems, Inc.,
Mountain View, CA). While these devices have already found widespread
use, a vast niche for medical ultrasound remains unfilled among
un-conventional or uninitiated users of ultrasound. Such clinicians,
medical technicians, battlefield medics, and veterinarians would greatly
benefit from using ultrasound to provide adjunct information during
routine medical examinations or when rapid diagnosis is crucial to
patient survival. Adapting the development of a medical ultrasound
device to these clinical needs requires judicious tradeoffs in system
complexity to provide an avenue to creating a pocket-sized unit with a
simple, intuitive interface and order of magnitude cost reduction beyond
that offered by current hand-held systems. Furthermore, by employing a
2-D transducer array, more intuitive scan formats such as C-mode become
available to users who may have had limited exposure to B-mode imaging.
The Sonic Window is a low-cost, pocket-sized medical ultrasound system
currently under development at the University of Virginia with these
concepts and target applications in mind. Potential applications for the
Sonic Window include guiding needle and catheter insertion
\[12\]–\[16\]; guiding biopsies \[17\], \[18\]; locating foreign bodies
\[19\], \[20\]; identifying internal bleeding and fluid collection
\[13\], \[21\]; and supporting routine physical examination \[3\],
\[21\]–\[24\]. The low cost and com-pact size of the device could open
applications in veterinary medicine and animal research. One such
application would be tumor localization and growth monitoring, a task
that is currently performed via palpation or visual inspection. In this
and other applications, the Sonic Window is envisioned as a widely
available, easy to use device suitable for users with little or no prior
ultrasound experience. As such, it will not compete with state of the
art systems with respect to image quality or flexibility, but must
surpass them with respect to ease of use, cost, and portability. The
high level of integration required by the Sonic Window requires a
significant degree of collaboration and cross-innovation between
transducer, electronics, and beamforming development. There exists a
need, therefore, to experimentally verify the expected performance and
tradeoffs of these three components not only in isolation, but also as a
system, and in a manner versatile enough to accommodate modifications in
their design. It is probable that several versions of the transducer
will be designed and fabricated as the dicing procedure, backing design,
and material selection are refined. Also, any modifications to the
receive electronics circuitry will require new ICs to be fabricated.

*Fig. 1. Long-term concept of the Sonic Window device. A model of the
Sonic Window is used to demonstrate its use in guiding needle insertion,
one of many possible applications.*

Equally important, the development of an experimental system containing
a custom, fully sampled 2-D array and custom receive circuitry provides
a unique opportunity to study the performance of a variety of
beamforming and signal processing algorithms while having knowledge and
control over design parameters that are inaccessible on commercial
clinical scanners. This paper discusses the design and assembly of an
exper-imental ultrasound system consisting of a 32 32-element, fully
sampled 2-D transducer array, a PCB containing sixteen 64-channel
front-end receive ICs with associated control logic and bias circuits, a
PCI card digitizer, and a PC that executes beamforming and signal
processing algorithms in software. The 2-D transducer array was
fabricated on a separate PCB and mates with the receive electronics PCB
by way of surface mount connectors. This experimental system can capture
and store 1024 channels of RF data for subsequent offline pro-cessing,
enabling us to explore the effects of our transducer fabrication,
circuit topologies, and beamforming strategies on image quality. A
description of the system and obtained experimental results are provided
next.

SYSTEM-LEVEL DESCRIPTION
------------------------

A description of the proposed ultracompact, low-cost med-ical ultrasound
device, the Sonic Window, was presented earlier \[25\], \[26\]. The
ultimate concept (Fig. 1) is a fully integrated, pocket-sized unit
consisting of a 2-D array, receive and protection circuitry implemented
on a custom integrated circuit, beamforming implemented on a digital
signal processor (DSP), and a high-resolution LCD screen for image
display. Crucial savings in circuit area and complexity are gained
through the use of a novel beamforming approach, direct sampled
in-phase/quadrature (DSIQ) beamforming \[27\], as well as new integrated
circuit topologies \[25\], \[35\]. These innovations, combined with the
development of an inexpensive method for fabricating a fully sampled 2-D
transducer array on a PCB \[28\], enable an unprecedented level of
integration and dramatic reductions in system cost.

*Fig. 2. System block diagram of the proposed Sonic Window device. The
design is partitioned into a single transmit circuit, a fully sampled
2-D transducer array, a custom IC containing receive circuitry, a
commercially available DSP, and a liquid crystal display.*

A block diagram of the future Sonic Window system is illus-trated in
Fig. 2. The design is partitioned into a single transmit circuit, a
fully-sampled 2-D transducer array, a custom IC containing an array of
receive channels, a commercially available DSP, and a liquid crystal
display. The common node of the 2-D array is connected to the transmit
circuit during transmit mode and to analog ground during receive mode.
Each receive channel will consist of an on-chip transmit protection
shunting device, a variable gain preamplifier, a bandpass filter, a
sampleand-hold (S/H) stage, an analog-to-digital converter (ADC), and
static memory. Placing the transmit protection devices on-chip
eliminates the need for bulky, expensive, and power-consuming off-chip
switching elements. The S/H stage consists of two S/H units, whose
output samples are one quarter period apart at the center frequency of
the received pulse. This operation estimates the in-phase (I) and
quadrature (Q) components of the RF signal, as defined by the DSIQ
beamforming algorithm \[27\]. Further-more, by forming C-mode images
rather than B-mode, each S/H unit need only capture a minimum of one
sample per image. The combination of these two properties dramatically
simplifies the design of the ADC by permitting digitization rates as low
as 10 kHz and produces much less stringent memory and data bandwidth
requirements. Since a standard CMOS process is used, this results in
significant reductions in cost, IC area, and power consumption.

DESCRIPTION OF EXPERIMENTAL SYSTEM PROTOTYPE
--------------------------------------------

An experimental ultrasound system was designed and con-structed (Fig. 3)
consisting of a 2-D array, custom receive and protection circuitry, and
a PC that included a Gage Com-puscope 12100 PCI card (Gage Applied
Technologies, Inc., Lachine, QC, Canada). The transducer array was
fabricated on a PCB substrate \[28\]. Each transducer element was
electrically connected to a dedicated pad on a surface mount connector
on the back of the PCB, while all the elements shared a common
connection on the top. A separate ten-layer, in in PCB was fabricated
(Fig. 4) that contains 16 custom receive circuitry ICs, four ADG707 8:1
differential analog multiplexing ICs (Analog Devices, Norwood, MA), two
output buffer channels, and an onboard XCR3064XL complex programmable
logic device (CPLD) (Xilinx, Inc., San Jose, CA). The PCB containing the
2-D transducer array was designed to mate with the receive circuitry PCB
by way of the surface-mount

*Fig. 3. Schematic diagram of the experimental prototype system. The
transducer array was fabricated on a PCB substrate. A separate PCB
contains 16 custom receive circuitry ICs each consisting of 64 front-end
receive channels. Each transducer element is electrically connected to a
unique receive channel on the electronics PCB. The outputs of the 1024
receive channels are multiplexed on-chip (64:2) and off-chip (32:2) down
to two bandpass filter output channels coupled to a PC fitted with a
two-channel data acquisition card.*

connectors (FX11-series, Hirose Electric (USA), Inc., Simi Valley, CA).
The data acquisition card was capable of capturing two channels of
12-bit data simultaneously at a sampling rate of 50 MHz. Thus, 512
separate transmit events were necessary to capture all 1024 channels of
RF data, and memory depth in each channel was limited to 1600 12-bit
samples. Volume RF data acquired with the prototype system was sampled
and stored on a PC for subsequent processing and data analysis in Matlab
(The MathWorks, Inc., Natick, MA).

### A. Fully Sampled, 2-D Transducer Array

Transducer development for the Sonic Window \[28\] in-volves the dual
challenge of constructing a fully sampled (high channel count) 2-D array
that is also inexpensive. The largest difficulty is the interconnect,
where an electrical connection must be made between each transducer
element and its dedicated receive channel. To date, we have used a
printed circuit board substrate, which can be fabricated much less
expensively than other approaches such as multilayer flex circuits,
wire-bonding, and solder connections. The transducer was fabricated by
attaching a 0.53-mm-thick wafer of high permittivity,
high-electromechanical-coupling-coefficient ceramic (HD3203, CTS
Wireless, Albuquerque, NM) to an array of pads on the PCB using Chobond
silver epoxy (Chomerics, Woburn, MA). The wafer was then diced using a
NBC-ZH2040 Disco dicing blade (Disco Corp., Tokyo, Japan) to form
isolated elements. The kerfs were 0.04 mm wide and 0.125 mm deep into
the PCB substrate. A low-viscosity, unfilled epoxy (RE2039, Loctite,
Rocky Hill, CT) was used to fill the kerfs. Finally, the entire
transducer array was covered with a gold-plated polyester electrode that
serves as a common node to all the elements \[Fig. 5(a)\]. The PCB
(MetroCircuits, Rochester, NY) consists of nine routing layers to fan
out each element pad to a contact on one of 16 surface-mount (SM)
connectors on the rear of the board \[Fig. 5(b)\], which electrically
mate the transducer array to corresponding SM connectors on the receive
circuitry PCB. A tenth layer serves as a ground plane. Design parameters
such as trace width and spacing (3 mil/76 m), minimum drill size (6
mil/152 m), and pad size (12 mil/305 m) represent the threshold of
current industry capabilities for a ten-layer PCB.

### B. Custom-Integrated Circuit Design

A number of researchers have recently implemented front-end receive
electronics on custom ICs for applications such as real-time 3-D imaging
\[29\], intravascular ultrasound \[30\], \[31\], intra-oral ultrasound
\[32\], high-frequency annular arrays \[33\], and portable ultrasound
\[6\], \[8\], \[34\]. We designed a custom IC containing 64 analog
front-end receive channels implemented in a standard TSMC 0.35- m CMOS
process available through the MOSIS Integrated Circuit Fabrication
Service (Marina del Rey, CA). Sixteen of these 64-channel ICs are used
to form all 1024 receive channels in our prototype system. Each channel
consists of an on-chip transmit protection shunting device, a variable
gain preamplifier, and a transconductance buffer. The receive channel is
fully differential to reduce distortion and suppresses the effects of
power supply and substrate noise.

The transmit protection scheme, described in \[35\], excludes the
expensive and area-consuming off-chip components used in other systems
to prevent the high-voltage transmit pulse from damaging the receive
electronics. Instead, a suitably sized NMOS transistor implemented
on-chip is connected between the preamplifier input and a low-impedance
power supply serving as analog ground. During the transmit event, this
NMOS transistor is turned on, shunting the large current transient from
the high-voltage transmit pulse to analog ground. Only a fraction (on
the order of 100 mV) of the transmit voltage (as high as 100 V) appears
at the input to the preamplifier. The shunt device is turned off during
receive to permit amplification of the received echo signal.

The low-noise preamplifier design (Fig. 6) consists of two identical
differential stages with variable gain. The gain can be adjusted between
30 and 85 dB by adjusting the bias voltage of triode-region device M3,
which serves as a source degen-eration resistance (Fig. 7). A novel
low-frequency suppression scheme is incorporated into the preamplifier
design to serve the dual purpose of reducing 1/f noise and rejecting dc
offset. The active load of the amplifier is designed to have high
mid-band gain, but small low-frequency gain, as shown in Fig. 7. The
gain profile can be tuned by adjusting the bias voltage LowFreqAdj. The
preamplifier equivalent input noise of 5 nV/ Hz (within the band of
interest) was found in simulation by performing a noise analysis in the
Cadence Virtuoso Spectre Circuit Simulator (Cadence Design Systems,
Inc., San Jose, CA).

Each preamplifier is followed by a differential transconduc-tance buffer
performing a voltage-to-current conversion, pro-viding the means to
implement a current-mode analog multi-plexing scheme in which multiple
channels can share the same output node with minimal impact on signal
bandwidth. The 64 channels are grouped into two 32-channel banks each
having a differential output (Fig. 8). One channel per bank is permitted
to drive its signal onto the common output nodes at any given time. The
output buffers of the inactive channels are disabled by turning off
their respective output MOSFET devices, effec-tively forcing them into a
high-impedance state. A 5-bit decoder selects the active channel in each
bank.

*Fig. 4. Photograph of the 11 in x 11.5 in receive electronics PCB (top
view). The PCB contains sixteen 64-channel custom receive circuitry ICs,
four differential analog multiplexing ICs, two output buffer channels,
and an onboard CPLD. The 2-D transducer array was designed to mate with
the rear side of the receive circuitry PCB by way of surface-mount
connectors.*

The active die area of the front-end receive circuit IC is 1.9 mm 0.9
mm, and includes the 64 analog receive channels and associated
multiplexing logic (Fig. 9). The die were packaged (Promex Industries,
Santa Clara, CA) into a Kyocera PGA121M (Kyocera America, Inc., San
Diego, CA) 121-pin ceramic package.

METHODS
-------

The experimental prototype system was assembled and tested for basic
functionality prior to attempting a transmit event or forming pulse-echo
images. Test points on the back of the transducer array were probed with
the transducer PCB connected to the receive electronics PCB. A 100-mV
sinusoidal test signal was applied to each element and RF data were
acquired from all channels. This experiment provided verification of the
mapping of transducer elements to channels and identified open or
shorted connections between the transducer elements and the inputs to
the receive circuitry ICs.

Pulse-echo volume datasets were acquired using the proto-type system.
The transducer was driven at its center frequency of 3.3 MHz with an
eight-cycle Gaussian-enveloped sinusoid having a full-width at
half-maximum (FWHM) bandwidth of approximately 30% and a peak-to-peak
amplitude of 30 V. As described above, the data acquisition hardware was
capable of acquiring and storing 1024 channels of data sampled at 50 MHz
with a memory depth of 1600 12-bit samples. C-mode images of each target
were formed on the PC in Matlab using three beamforming techniques:
beamforming using only time delays, conventional baseband demodulated
I/Q beamforming using only phase delays, and DSIQ beamforming that also
uses only phase delays. Beamforming was implemented to be consistent
with the methods followed in \[27\], with the exception of the assumed
transducer fractional bandwidth (30% versus 55%), center fre-quency (3.3
MHz versus 5.5 MHz), the sampling rate (50 MHz versus 39.27 MHz), and
that fact that our experimental system forms C-mode images (in keeping
with the Sonic Window de-vice concept) as opposed to the B-mode images
formed in \[27\]. The acquired data was filtered in Matlab to 30% -dB
fractional bandwidth at 3.3 MHz with a 51-order FIR filter. Hann window
apodization was used \[36\]. Scaling was applied where applicable to
compensate for energy differences in pixels beamformed with receive
apertures that intersected edges of the 2-D array.

Time-delay beamforming was implemented using unquan-tized time delays
(IEEE double precision floating point repre-sentation). A cubic
spline-based continuous representation of the sampled data was used to
evaluate the received signals in each channel at the requisite time
points \[27\], \[37\]. RF data produced by summing across channels were
envelope detected using the Hilbert transform. Conventional baseband
demodulated data were obtained by multiplying the received data by to
form the in-phase (I) component and by to form the quadrature (Q)
component, where was the transducer center frequency of 3.3 MHz, was the
sample number, and was the sampling interval.

This data were then low-pass filtered with a fifth-order Butterworth
filter and zero-phase distortion was accomplished by filtering once in
the forward direction and then filtering a second time after reversing
the output. This produced a -dB cutoff at 3.3 MHz. The I and Q
components were combined into an analytic representation of the received
echo signal that was then apodized and focused via phase rotation
through complex multiplication operations, the results of which were
summed across channels to yield the intensity at a given point on the
image plane.

As described in \[27\], DSIQ samples will be formed in our final system
by splitting the received signal between two parallel sample-and-hold
(S/H) channels. As described in Section II, the Sonic Window device will
ultimately include S/H stages and ADCs on the same IC as the front-end
receive circuitry components. In each receive channel, one S/H will
acquire the I component and then the other S/H will acquire the Q
component by sampling one quarter of a period later at the center
frequency of the signal. In the experimental system prototype, only the
front-end circuitry was implemented on-chip, and the sampling was
performed by the Gage Compuscope 12100 PCI card at a rate of 50 MHz at
uniform sampling intervals.

The I component sample was taken directly from this acquired RF data—the
Q component sample was synthesized by interpolating the acquired RF data
at a time lag of a quarter period at the assumed center frequency using
cubic spline interpolation \[27\], \[37\]. The apodization, phase
rotation and summation across channels were implemented as in the
conventional base-band demodulation case described above. The three
beamforming methods described above were used to form C-mode images from
pulse-echo data acquired off two targets for the purpose of comparing
the performance of the DSIQ method to the time-delay and conventional
I/Q methods, as well as evaluate the overall performance of the
experimental system. The first target was a 200- m nylon wire in a water
tank placed 1.5 cm below and parallel to the face of the transducer. The
second target was a custom-made “edge phantom,” which consisted of 10%
acrylamide gel ( m/s) having one speckle-generating region and one
nonspeckle-generating region. The speckle-generating region was
constructed by incorporating Sephadex (Amersham, Piscataway, NJ) into
the acrylamide. The procedure followed in constructing this phantom was
based on that described in \[38\], although higher acrylamide
concentrations were used. The geometry of this edge phantom is such that
an ideal C-mode image acquisition should produce an image with speckle
in one half and an absence of speckle (anechoic region) in the other
half.

EXPERIMENTAL RESULTS
--------------------

Fig. 10 is a binary mapping of “dead” channels discovered from the
probing procedure. It was found that 69 out of 1024 electrical channels
(6.74%) contained an open circuit between the transducer element and its
corresponding receive channel input. The cause of the majority of these
open connections was determined to be due to errors in the layout design
of the 2-D transducer array PCB. Poor contact was also noted between the
surface-mount connectors on the transducer PCB and the receive
electronics PCB. Since contact between these surface-mount connectors
relies on a friction fit, minor bending and warping of the transducer
PCB can result in localized misalignment of connector contacts. This
overall net channel yield should be distinguished from the transducer
element yield, which was measured to be 99%. The top panel in Fig. 11
illustrates the simulated 2-D point spread function (PSF) in the C-mode
plane for the ideal case in which 100% of the receive channels are
connected to their respective transducer elements. The bottom panel in
Fig. 11 illustrates the simulated 2-D PSF in the C-mode plane for a
6.74% channel loss having the same distribution (channel-to-element
mapping) observed in the experimental prototype system (see Fig. 10).
These two PSFs were computed in Matlab using a narrowband
Rayleigh–Sommerfeld formulation \[39\] fora plane parallel to the
transducer at a depth of 2 cm. Hann window apodization \[37\] was used.
The images in Fig. 11 were normalized, logarithmically compressed, and
mapped so as to present image intensity over the range to 0 dB. The
C-mode images of the wire target acquired with the prototype system
(Fig. 12) were formed using conventional unquantized time-delay
beamforming (TD), conventional baseband demodulated I/Q beamforming
(IQ), and DSIQ beamforming (DSIQ) methods for f\#s of 0.5, 1, and 2.
Hann window apodization was used. The C-mode images were normalized,
logarithmically compressed, and mapped so as to present image intensity
over the range to 0 dB. The FWHM of the wire in the acquired images at
f/1 is 1.2 mm. One-dimensional integrated cross-sections of the wire
target images in azimuth were formed by performing a 2-D spline
interpolation (8x) on the original absolute image, summing in elevation,
and then plotting the normalized, logarithmically compressed result.
C-mode images of the edge phantom target acquired with the prototype
system (Fig. 13) were formed using pure time-delay beamforming (TD),
conventional baseband demodulated I/Q beamforming (IQ), and DSIQ
beamforming (DSIQ) methods for f\#s of 0.5, 1, and 2. Hann window
apodization was used. The contrast between the region with speckle and
region with no speckle was 10 dB. The C-mode images were normalized,
logarithmically compressed and mapped so as to present image intensity
over the range to 0 dB. One-dimensional integrated cross-sections of the
edge phantom images in elevation were formed by performing a 2-D spline
interpolation (8x) on

*Fig. 11. Simulated 2-D PSF (C-mode plane at a depth of 2 cm) for the
ideal case in which 100% of the receive channels are connected to their
respective transducer elements, and for a 6.74% channel loss following
the distribution (channel-to-element mapping) observed in the
experimental prototype system. Both images were normalized,
logarithmically compressed and mapped so as to present image intensity
over the range —40 to 0 dB. the original absolute image, summing in
azimuth, and then plotting the normalized, logarithmically compressed
result.*

DISCUSSION
----------

Overall, the experimental results shown are very promising in that they
demonstrate successful pulse-echo image formation with a low-cost,
compact, experimental ultrasound system in its proof-of-concept phase of
development. There do exist, however, multiple avenues for improving
image quality. The largest contributor to poor image quality was the
pres-ence of large grating lobes (observable in Fig. 11 approximately
1.5 cm from the focus) caused by the transducer element pitch. The pitch
was 635 m, while the wavelength at 3.3 MHz and 1540 m/s speed of sound
is 467 m. Element pitch was limited by the PCB manufacturing
capabilities, specifically the trace width/spacing and minimum pad size
for vias. The minimum pad size was necessarily increased to account for
the worsening drill tolerance as the aspect ratio (ratio of PCB
thickness to drill hole size) increased. The aspect ratio increased with
the number of routing layers, which in turn depended on the trace
width/spacing. Another significant contributor to image quality
limitations is the manner in which signals were routed from individual
trans ducer elements to their respective electronic receive channels. As
described in Section V, routing errors in the transducer PCB along with
intermittent poor contact between the surface mount connectors resulted
in a channel loss of 6.74%. As illustrated in Fig. 11, these lost
channels have the undesirable effect of significantly degrading the PSF
by raising side lobe levels to as high as dB and distorting the
mainlobe. Note also that the channel loss results in a shift variant
system—pixel-to-pixel gain varies as the receive aperture is translated
across this nonuniform pattern of “dead” transducer elements. These
effects significantly contribute to the presence of clutter and other
artifacts, causing anomalous spots and kinks or gaps in the wire target
image and poor contrast in the edge phantom image. Furthermore, the
interconnect scheme also suffers from parasitic inductances,
capacitances, and resistances associated with long PCB traces, the
surface-mount connectors, and the custom IC pin grid array (PGA) chip
packages that all contribute to signal-to-noise (SNR) degradation,
crosstalk, and impedance variation among channels. Despite successful
image formation using this preamplifier (see Fig. 6), a significant
problem was discovered involving the low-frequency suppression scheme.
When a large transient voltage appeared at the input of the preamplifier
(similar to that accompanying a transmit event), the drain-source
voltage of the triode-region device M8 (M9) was large enough that a
charge was drained from the MOScap, M12 (M13), in the active load. This
changed the bias point enough to significantly lower the overall
mid-band gain of the preamplifier. A temporary solution was implemented
in which the LowFreqAdj bias was dynamically tuned such that after each
transmit event some of the charge was allowed to return onto M12 (M13),
though the gain and dynamic range of the overall preamplifier was still
degraded.

Another factor influencing image quality is the use of the DSIQ
beamforming algorithm, which makes concessions in image quality to
provide the dramatic hardware savings ex-ploited by the Sonic Window
device. However, as illustrated in Figs. 12 and 13, the C-mode images
formed using DSIQ beamforming exhibit very little difference from the
conven-tional time-delay and I/Q methods. While it can be argued that
the transducer, interconnect, and front-end shortcomings described above
dominate the subtler differences in image quality that exist between the
three beamforming approaches, the integrated 1-D cross sections in Figs.
12 and 13 offer further insight. Here, the differences between
beamforming approaches are more evident—particularly at lower f\#s—but
the overall performance is still similar. DSIQ and conventional I/Q
beamforming appear to behave almost identically, and both deviate from
TD beamforming at lower f\#s because both approaches rely on phase
rotation to achieve delays and are thus susceptible to focusing errors
toward the edge of the aperture. The integrated 1-D cross-sections at
higher f\#s demonstrate closer agreement among all the beamforming
approaches. These trends are similar to the findings in \[27\], where
the DSIQ algorithm was shown to compare favorably with conventional
beamforming techniques in a B-mode commercial ultrasound scanner not
suffering from the grating lobe and channel-loss issues present in our
experimental system. DSIQ beamforming was also shown to be surprisingly
robust to error in the assumed center frequency, which would cause the
S/H clocks to be offset at phase differences other than 90 . According
to Fig. 6 in \[27\], an 18% error in the assumed center frequency (70
phase difference between I and Q samples) led to a loss of only 1 dB in
contrast performance. Additionally, while narrowband signals are the
ideal for DSIQ beamforming, reasonable image quality was obtained with
fractional bandwidths as high as 55% \[27\].

Ultimately, the target clinical application for the Sonic Window device
dictates the losses in image quality that can be tolerated in exchange
for the low cost, compact size, and simple operation that it demands. A
consequence of the transmit protection scheme is the lack of focusing on
transmit and its associated losses in SNR and penetration. However, as
discussed in \[35\], the Sonic Window is intended for imaging shallow
targets, which significantly relaxes the penetration requirement, and
all image data is captured in parallel after each transmit event, so a
plane wave transmit is appropriate. Furthermore, the protection scheme
significantly simplifies the transmitter hardware \[27\], facilitates a
flip-chip interconnect scheme in future versions of the Sonic Window
(avoiding SNR losses through cabling) \[35\], and is critical in
enabling the use of a 2-D array, which provides array gain benefits and
compensates for slightly worse clutter in azimuth with much better
performance in elevation \[40\]. Similarly, a consequence of DSIQ
beamforming is its preference for a smaller signal bandwidth, which
corresponds to an increase in C-plane thickness. Our experimental system
used a 3.3-MHz center frequency and 30% fractional bandwidth generating
a slice thickness of approximately 770 m. However, this is more than
adequate to satisfy our initial goal of visualizing a 5-mm-diameter
blood vessel in the arm for needle or IV line insertion \[40\] and slice
thickness will decrease as the system center frequency increases in
future prototypes.

The experimental system described in this paper served well as
confirmation of our general design approach, novel technologies, and
performance tradeoffs. Several modifications will be necessary to
realize the long-term concept of a clinically viable Sonic Window
device. The grating lobe and channel loss issues can be addressed
through an improved interconnect approach providing smaller transducer
element pitch and increased channel count. By designing receive
electronics ICs with a channel pitch that corresponds to the transducer
element pitch, a flip-chip interconnect scheme is possible, providing a
straightforward connection between transducer elements and receive
channels with little or no routing \[8\], \[30\], \[31\], \[41\],
\[42\]. If DSIQ beamforming is used, digitization and memory can be
brought on-chip along with the front-end receive electronics, enabling
the simultaneous capture of all the complex data needed to form a C-scan
image—a simple depth control would vary the timing of the global S/H
clock signals. Our experimental system took as long as two minutes to
form one C-scan image, which included time for 512 transmits, memory
transfer of the volume data from the acquisition card, and processing on
the PC. However, with parallel on-chip data capture, DSIQ beamforming
could be performed in real-time by a low cost, commercially available
DSP \[27\], \[42\]. The significantly low pulse repetition frequency (as
low as the frame rate) requirements of such an approach can be exploited
by switching off the transmit and receive electronics in between
transmit events to save power and prevent overheating, even allowing for
multiple transmit events for signal averaging to improve SNR \[35\] and
compounding techniques for speckle reduction \[27\].

CONCLUSION
----------

A high-channel-count experimental ultrasound system was constructed and
experimentally shown to successfully form pulse-echo images of a wire
target and edge phantom. Images formed using the DSIQ beamforming
algorithm compared fa-vorably with that of conventional time-delay
beamforming and baseband demodulated I/Q beamforming. Image quality was
impacted predominantly by grating lobes caused by suboptimal transducer
element spatial sampling and routing errors in the transducer PCB
coupled with poor surface mount connector contact. Future efforts will
focus on reducing element pitch and utilizing alternative interconnect
approaches to provide significant improvements in image quality in the
future Sonic Window system.

ACKNOWLEDGMENT
--------------

The authors would like to thank E. Girard for her contribution to the
transducer design, E. Brush for his assistance in probing the transducer
interconnect, and M. Oberhardt for constructing our phantoms.
