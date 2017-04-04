1.  Introduction to acoustic imaging

In this document, we will explain some basis of the acoustic theory to
understand the propagation of acoustic waves and the echographic
process.

Propagation of acoustic waves
=============================

In this section, we will define the different types of acoustic waves
and some basic equations and properties of the propagation of acoustic
waves. Here you can download the [ pdf
version](:File:acoustic.pdf "wikilink") of this page. Our wiki does not
support latex interpretor yet, so we can't draw correct equation here,
but the equation will be written in the latex equation format. If you
prefer to read clear equation, we suggest you to read the pdf file. Here
some mathematical formulation with latex equation format:

-   \\lambda: greek font lambda
-   \^{x}: upperscript or power x
-   \_{x}: underscript x
-   \\dfrac{x}{y}: fraction, x divided by y
-   \\Re{x}: real part of x
-   \\Im{x}: imaginary part of x
-   \\e\^{x}: exponential x
-   \\im: imaginary constant, \\im\^2 = -1

Wave types
----------

An acoustic wave is a perturbation of the local state without
displacement of the global state. Acoustic waves are periodic, their
spatial periodicity is given by the wavelength \\lambda. Consider a
medium at rest such as on Fig. 1, where the particles are represented by
the dots. Such a periodic structure represent a metal for example. When
an acoustic wave propagate in this medium, the particles will have a
local displacement.

![300 px|center|thumb|alt=Alt text|Fig. 1: Medium at
rest.](at_rest.png "300 px|center|thumb|alt=Alt text|Fig. 1: Medium at rest.")

There is two types of acoustic waves, the longitudinal waves (Fig. 2)
also named P waves and the transverse waves (Fig. 3) also named SH or SV
waves. The longitudinal waves are compressional waves, the direction of
the displacement of the particles is the same than the direction of
propagation of the wave. The transverse waves are shear waves, the
direction of displacement is then perpendicular to the direction of
propagation of the wave. In a fluid, such as the water, only
longitudinal waves can propagate. In the human body, the shear modulus
is very small, it can be considered as a fluid, and so only longitudinal
waves will be generated.

![300 px|center|thumb|alt=Alt text|Fig. 2: Longitudinal
wave.](Pwave.png "fig:300 px|center|thumb|alt=Alt text|Fig. 2: Longitudinal wave.")![300
px|center|thumb|alt=Alt text|Fig. 3:Shear
wave.](Swave.png "fig:300 px|center|thumb|alt=Alt text|Fig. 3:Shear wave.")

In the rest of the document, we will only consider longitudinal waves.

Mathematical formulation
------------------------

In acoustic, a fluid medium is describe by two mecanical parameters: the
mass density \\rho and the bulk modulus \\kappa. The bulk modulus relate
the change of volume of a medium to the isostatic pressure apply on it.
The velocity of the acoustic wave c is:

`c = \sqrt{\dfrac{\kappa}{\rho}}, (1)`

for example, for the water we have: \\rho = 1000 kg.m\^{-3}, \\kappa =
2.19 MPa and c = 1480 m.s\^{-1}.

The mathematical formulation is obtained by solving the Helmholtz
equation, for exemple, the acoustic pressure p\\left(x,t\\right) can be
expressed as:

`p\left(x,t\right) = (A^{+}\e^{\im kx}+A^{-}\e^{-\im kx})\e^{-\im\omega t}, (2)`

A\^{+}\\e\^{\\im kx} is a wave of amplitude A\^{+}, propagating toward
the positive x, A\^{-}\\e\^{-\\im kx} is a wave of amplitude A\^{-},
propagating toward the negative x. k = \\dfrac{\\omega}{c} is the
wavenumber, \\omega=2\\pi f the angular pulsation and f the frequency.

When we make an echographic image, we are intresting only on the
intensity of the wave:

`I = \dfrac{1}{2}\Re[p(x,t)v^{*}(x,t)], (3)`

where v\\left(x,t\\right) is the velocity of the particle, and x\^{\*}
represent the complex conjugate of x. It can be shown with the Euler's
equation that the intensity is directly proportional to the square
modulus of the pressure.

Refraction and diffusion of acoustic waves
------------------------------------------

When an acoustic wave passes from a medium (0) to a second medium (1), a
part of the wave is reflected an the over part is transmitted through
the interface. When the interface is flat in the point of view of the
wave, we have refraction (it is a quasi one dimensional problem, because
the wave is reflected on only one direction of the space). When the wave
sees the curvature of the interface, the wave is scattered on all the
directions of the space, we talk then about diffusion.

### Refraction of a wave

![300 px|center|thumb|alt=Alt text|Fig. 4:Normal refraction of a
wave.](refraction.png "300 px|center|thumb|alt=Alt text|Fig. 4:Normal refraction of a wave.")

We consider an incident wave \\phi\_{\\inc} normal to an interface, the
reflected \\phi\_{R}=R\\phi\_{\\inc} and the transmitted
\\phi\_{T}=T\\phi\_{\\inc} waves are also normal to the interface (Fig.
4). R and T represent respectively the reflexion and transmission
coefficient. By solving this problem, we show that:

`R = \dfrac{Z_2-Z_1}{Z_2+Z_1}, (4)`

where Z\_i = \\rho\_ic\_i is the acoustic impedance of the medium i.

If we consider, for example the reflection of a wave at an interface
between water (\\rho\_0 = 1000 kg.m\^{-3}, c\_0 = 1480 m.s\^{-1}) and a
muscle (\\rho\_1 = 1070 kg.m\^{-3}, c\_1 = 1590 m.s\^{-1}), the
reflection coefficient is equal to 69.10\^{-3}, so only 7% of the
pressure is reflected. If we know consider an interface between water
and bone (\\rho\_1 = 2175 kg.m\^{-3}, c\_1 = 4000 m.s\^{-1}), then
nearly 70% of the incident wave is reflected. The echos due to bones are
much more higher than the ones due to the muscles.

### Scattering of a wave

Even if an object is very small in front of a wave, it still scattered
the wave (Fig. 5). It is much more complicated to determine the
scattered wave than the reflected wave such as in sec. Refraction of a
wave.

![300 px|center|thumb|alt=Alt text|Fig. 5:Scattering of a
wave.](diffusion.png "300 px|center|thumb|alt=Alt text|Fig. 5:Scattering of a wave.")

The diffused wave goes in every direction of the space, it lead that its
amplitude decreases with the distance from the object.

Attenuative media
-----------------

The human body is an attenuative media, this mean that the amplitude of
a wave propagating in such medium decreases along its direction of
propagation. Mathematically, the propagation of waves in this kind of
medium is written as:

`p(x,t)=(A^{+}\e^{\im kx}\e^{-\alpha x}+A^{-}\e^{-\im kx}\e^{\alpha x})\e^{-\im \omega t}. (5)`

The difference between the propagation of a wave between a
non-attenuative and an attenuative medium is present on Fig. 6. So when
we do acoustic imaging in the human body, we must gradually amplify the
received signal if we want to convert correctly the analogical signal
into a digital signal, because if the amplitude of the signal is smaller
than the precision of the ADC, we can't measure it (see appendix ADC).
Classically, we do Time Gain Compensation (TGC) on the receive signal in
order to keep a convenient amplitude of the received signal. An example
of this kind of treatment is presented on Fig. 7, it's apply to the
attenuated signal on the right side of Fig. 6.

![300 px|center|thumb|alt=Alt text|Fig. 6:Acoustic pressure of a wave
propagating in a non-attenuative (left) and attenuative (right)
medium.](attenuative_medium.png "300 px|center|thumb|alt=Alt text|Fig. 6:Acoustic pressure of a wave propagating in a non-attenuative (left) and attenuative (right) medium.")

![300 px|center|thumb|alt=Alt text|Fig. 7:Example of TGC applied on the
attenuated signal (right side of Fig.
6).](tgc_example.png "300 px|center|thumb|alt=Alt text|Fig. 7:Example of TGC applied on the attenuated signal (right side of Fig. 6).")

Transducer
==========

A transducer is an acoustic sensor, it convert electric power to
mechanical power and conversely. So if you apply an electric signal on
it, it will generate acoustic wave (like a speaker), and if an acoustic
wave deform it, it generate an electrical signal (like a microphone).

In order to have a correct radial precision in acoustic imaging, the
acoustic wave must be focused on one point. This can be done by two kind
of technologies: focussed transducer and transducers array.

Focussed transducer
-------------------

![300 px|center|thumb|alt=Alt text|Fig. 8: Acoustic wave focalisation
(red) by a focussed
transducer.](transducer_scheme.png "300 px|center|thumb|alt=Alt text|Fig. 8: Acoustic wave focalisation (red) by a focussed transducer.")

This kind of transducer have a spherical shape, so the emitted acoustic
wave naturally focalised at the center of the sphere (Fig. 8). The area
of the focal spot is an ellipse, the value of l and L can be approximate
by:

`l = \dfrac{\lambda R}{2r}, (6)`

`L = 15(1-0.01\theta)l. (7)`

More \\theta is high, more the ellipse is small. When we do acoustic
imaging, we want l to be as small as possible to increase the radial
precision. Moreover we want L to be high, because the echo of an object
outside of this ellipse will be too small to be measured. So we have to
make a compromise between l and L.

At the nearfield (it depend on \\lambda and r) of the transducer, the
acoustic pressure is to chaotic so we can't do acoustic imaging in the
nearfield of this kind of transducer.

Transducers array
-----------------

On a transducers array, generally, the size of each transducer is small
compare to the wavelength, so they emit spherical waves. If all the
transducers emit a wave at the same time, the array will emit a plan
wave. If you apply a right delay between the emission of each transducer
it is possible to generate a focussed acoustic wave (Fig. 9). This delay
can be simply calculated, indeed, by knowing the distance between each
transducer, you just have to determine a delay that consist on having
all the wave generated by each transducer arriving exactly at the same
on a given point of the space. By doing this the waves interfere
coherently near this point (high pressure) and incoherently everywhere
else (low pressure).

![300 px|center|thumb|alt=Alt text|Fig. 9: Acoustic wave focalisation
with an array of
transducers.](transducers_array.png "300 px|center|thumb|alt=Alt text|Fig. 9: Acoustic wave focalisation with an array of transducers.")

With a transducers array, it is possible to focalise at different points
at the same time, so acoustic imaging can be faster with this and it
don't need a motor to image a plane. However they are much more
expensive than a simple focussed transducer and the electronic is much
more complicated to drive a transducers array.

Signal Processing
=================

In this section we introduce the Fast Fourier Transform (FFT) and
present a basic signal processing to improve an echographic signal.

Fast Fourier Transform
----------------------

The Fourier Transform is a transformation that express a function of a
given dimension as a function of another dimension. Classically, a time
dependent signal is expressed as a function of the frequencies. In
acoustic we also apply Fourier transform to a space signal, so the
transform is a function of the wavelength. The Fourier Transform S of a
real signal s is complex and \\Re(S) is an even function and \\Im(S) is
odd.

The FFT is an algorithm that calculate the Fourier Transform of a signal
very fast, the number of point of the signal must be a power of 2. The
FFT of a signal is a periodic function with a periodicity equal to the
frequency sampling of the initial signal. Classically, the FFT algorithm
return the Fourier Transform for the positive frequencies. Due to the
periodicity of the FFT, the second half of the signal is the negative
frequency part.

Consider a time signal sample at frequency f\_e=640 MHz composed of
N=1024 points (Fig. 10). If you keep only the positive frequencies, the
frequency vector corresponding to the FFT go from 0 to
f\_e\\dfrac{N-1}{N}. On octave its given by linspace(0,fe\*(N-1)/N,N).
The FFT of the time signal keeping the positive frequencies is presented
on Fig.\~\\ref{fig:positive frequencies}.

![300 px|center|thumb|alt=Alt text|Fig. 10: Example of a time
signal.](time_signal.png "300 px|center|thumb|alt=Alt text|Fig. 10: Example of a time signal.")

![300 px|center|thumb|alt=Alt text|Fig. 11: FFT of the signal presented
on Fig. 10 keeping only the positive frequencies. On blue, real part and
green imaginary
part.](positive_frequenciesb.png "300 px|center|thumb|alt=Alt text|Fig. 11: FFT of the signal presented on Fig. 10 keeping only the positive frequencies. On blue, real part and green imaginary part.")

If one want to filter the signal, it is more convenient to consider the
negative frequencies, because if you to filter the a signal between x
and y MHz, you must put to 0 all frequencies except the points between x
and y MHz and also the points between -x and -y MHz. In this case, the
frequency vector is given by linspace(-fe/2\*(N-1)/Nfe/2,N) and you must
put the second half of the FFT signal at the beginning. To do that you
must create a new vector of the same size than the FFT signal, and doing
fox example: S2(1:N/2-1)=S(N/2+2:end) and S2(N/2:end)=S(1:N/2+1). Then
you obtain the signal presented on Fig.\~\\ref{fig:negative
frequencies}.

The real and imaginary part of the FFT presented on
Fig.\~\\ref{fig:positive frequencies} and \\ref{fig:negative
frequencies} are divided by their maximum amplitude to have readable
graphics.

If one want to know the central frequency of transducer, you must take
the modulus of the FFT of an echo of the transducer. The central
frequency is the frequency where the modulus has the higher value.
