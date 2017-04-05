1.  Compressing with FFT

Rationale
---------

We're playing on the raw signal dataset coming from the EmileKit setup.
( all files can be found at
<https://github.com/kelu124/rechOpen/tree/master/FiltrageFrequentiel> ).
Parameters are as follows:

-   Sampling at 125MHz
-   16\*1024 points of acquisition (\~131µs)

The aim of this is to "see" the actual signal.

+--------------------------------------+--------------------------------------+
| ![](X-nofiltrage.png "X-nofiltrage.p | ![](X-line76-raw.png "X-line76-raw.p |
| ng"){width="500"}                    | ng"){width="500"}                    |
|                                      |                                      |
| The raw signal is 16k points long,   | The image is barely visible - the    |
| and in this sample has 256 lines.    | echo for example barely is over the  |
|                                      | noise at position \~9000.            |
+--------------------------------------+--------------------------------------+

Filtering
---------

To clear the white noise, we'll take advantage that the piezo has only
his own resonance - we can make this appear by applying a FFT to the
signal, and zooming where it should be. All code is in octave/matlab
format in the corresponding github repo.

+--------------------------------------+--------------------------------------+
| ![](FFT_1000to1000%2B2048.png "FFT_1 | ![](FFTImageSquared.png "FFTImageSqu |
| 000to1000%2B2048.png"){width="500"}  | ared.png"){width="500"}              |
|                                      |                                      |
| A first zoom between points 1000 and | Again, zooming between 1500 and      |
| 1000+2048 of the FFT have them       | 1500+1024, squaring the FFT to see   |
| appear.                              | the figures appear                   |
+--------------------------------------+--------------------------------------+

Going back in the time domain
-----------------------------

With a reverse FFT, zeroing all "uninteresting" frequencies, we do
obtain a filtered image:

### On a single line

+--------------------------------------+--------------------------------------+
| ![](X-line76-raw.png "X-line76-raw.p | ![](x-line76-squared-filtered.png "x |
| ng"){width="500"}                    | -line76-squared-filtered.png"){width |
|                                      | ="500"}                              |
| Before the filter                    |                                      |
|                                      | After the filter, squared, the echo  |
|                                      | appears better.                      |
+--------------------------------------+--------------------------------------+

### On the image

+--------------------------------------+--------------------------------------+
| ![](X-filtrage-2048 large.png "X-fil | ![](x-filtrage-1024 large.png "x-fil |
| trage-2048 large.png"){width="500"}  | trage-1024 large.png"){width="500"}  |
|                                      |                                      |
| Using the 2048-wide filter           | Using the 1024-wide filter           |
+--------------------------------------+--------------------------------------+

Next steps
----------

We have defined our image using only 2048 points out of the 16k points
series, while at the same time enhancing the signal we were looking for.
Isn't it some time of image compression?

Gallery of images
-----------------

<File:X-filtrage-2048> large.png <File:x-filtrage-1024> large.png
<File:ImageScSquared.png> <File:x-line76-raw.png>
<File:x-line76-squared-filtered.png> <File:X-nofiltrage.png>
<File:raw.png> <File:FFTImageSquared.png> <File:UDPLOG.png>
<File:FFT_1000to1000+2048.png>

<Category:Transmitting> <Category:SignalProcessing>
