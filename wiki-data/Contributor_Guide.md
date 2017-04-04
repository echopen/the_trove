1.  Contributor Guide

<div class="jumbotron">
<h1>
<span class="mw-headline" id="Cabals">Guide to Contribution</span>

</h1>
\
If you want to contribute to echOpen project, you should read this first
and then go and follow your instinct there -&gt; **[GitHub
echOpen](https://github.com/echopen)**.

</div>
Contributing to Code
====================

Set up dev env
--------------

The project uses `gradle` as a build tool and we advise the use of
`Android` `Studio` as an ide.

You must create and set `local.properties` file. There, you must set the
paths to the `Android` `SDK` and the `Android` `NDK`. The `Android`
`SDK` installation is well documented
[there](https://developer.android.com/intl/ko/sdk/installing/index.html).
You’ll find the doc related to `Android` `NDK`
[here](https://developer.android.com/intl/ko/tools/sdk/ndk/index.html).
You’ll need to downlaod and install the materials found
[there](https://developer.android.com/intl/ko/ndk/downloads/index.html).

For `C/C++` coders, the `JNI` configuration is already set to wrap non
java code and libraries. It is not easy to maintain these kind of code
but the performance will be our benchmark in the sense that if the
advantage of using `C/C++` tools is so important that it provides images
drastically closer to real time, this solutions will be adopted.

Clone and code
--------------

` git clone git@github.com:echopen/android-app.git`

-   Create your own branch
-   Write your code, following the convention detailed below

Test the code
-------------

<div class="alert alert-warning" role="alert">
<strong>Wait ! </strong> Your code you write must be covered with tests.
It should pass the specific tests of your code and pass all the
**echOpen** tests.

</div>
As mentionned above, it is of critical medical interest that the image
can be displayed in near real time, at most \~10ms, the code should not
lower the performance of the app. A lot of tools help monitoring the
performance and debugging issues. [VisualVM](https://visualvm.java.net/)
is good stuff to deal with, and it is Open Source.

Pull requests
-------------

To submit your code, you must run a Pull Request, see
[here](https://help.github.com/articles/using-pull-requests/) for the
way to do that.

Contributors
------------

All the contributors will have their name set in our Wall of Fame !!

Contributing via Documentation : for Noobs and Experts
======================================================

Some times, parts of code or part of its documentation remain cryptic or
non documented at all. It is a perfect fit for contributions.

For contributors already easy with coding, it is a good way to dive into
the code and turn it more familiar. For those that are not really easy
with coding, they can also contribute to detect : typos, non observance
of the coding convention described below.

Code format
===========

Naming Convention
-----------------

The `*.java` files have the same name as the class whom they are the
source of.

package : names are lower-cased

classes, interfaces and constructors : each words that decomposes the
name has a first capital caracter example : MyClass, MyGreatInterface

methods and variables are camel-cased - they should be meaningful

setters and getters of a field are named setField and getField

for specific pattern as Builder or factory, this should be user
MyClassBuilder, MayClassFactory

Code documentation
------------------

The indentation unit is 4 spaces

A blank line should always be used in the following cases:

-   Before the declaration of a method
-   Between the declarations of local variables and the first line of
    code
-   Before a review of a single line
-   Before each logic section in the code of a method

As for breaking long lined code :

-   Avoid line greater than 80 characters
-   Break after a comma
-   Break before an operator
-   Align the new line with the beginning of the expression at the same
    level on the previous line

Classes are grouped by functional packages according to homogeneity
criteria.

Each class is documented the following way

constants are upper-cased

` /*`\
` * Created by author on 16/09/15.`\
` *`\
` *  Description of the class`\
` */`

The class and interfaces declaration meet the following schema

-   Comments as detailed above
-   The declaration of the class or interface
-   The declaration of variables in the ollowing order public &gt;
    protected &gt; private
    -   first static class variables
    -   then instance variables
-   Constructor(s)
-   the methods

non-trivial methods are documented

`/*`\
`* @param Param1 param1`\
`* @param Param2 param2`\
`* @return Value value`\
`* @exception Exception1 exception description`\
`*/`\
` public Value myMethod(Param1 param1, Param2 param2){...}`

The comments useful for the code understanding can be in-lined or
multi-lined inside the code

More specific conventions
-------------------------

No shorthands for if-then-else loops in order to enhance the easiness of
development

There should be a space between the class name and the opening brace

` MyClass extends OtherClass {...`

Reporting issue
===============

Resolving Issue
---------------

All the **echOpen** issues are opened and discussed on
[GitHub](https://github.com/echopen/android-app/issues). For code issue,
you can help verify that the issue is indeed one tes it in local in
order to evaluate its reproduciblity.

When a solution is supposed to solve the issue, the whole code should
pass **all** the tests.

Since it is of critical medical interest that the image can be displayed
in near real time, at most \~10ms, the code should not lower the
performance of the app. A lot of tools help monitoring the performance
and debugging issues. [VisualVM](https://visualvm.java.net/) is good
stuff to deal with, and it is Open Source.

Create a bug report on [Github](https://github.com/echopen/android-app/issues)
------------------------------------------------------------------------------

Any issue related to the app or the documentation can be reported
[here](https://github.com/echopen/android-app/issues).

You should follow the following plan to report the issue :

**Synthetic title &gt; Brief abstract &gt; all details &gt; proposals of
resolution if any &gt; discussion**

Any bug must be as documented as possible and should reproduce each step
that leads to it. If you have a suggestion to fix it, include it in the
bug report.

Each issue should be labelled with the help of our dedicated github
labels.

If you’re not a Github user and you have no intent to be, please contact
us via email : contact \[at\] echo pen \[dot\] org

<div class="alert alert-danger" role="alert">
<span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
<span class="sr-only">Rermark</span> If any vulnerability issue is
found, please please email us rather than issuing on GitHub

</div>
Android App
===========

Android-App display overview
----------------------------

In order to prevent form too verbose classes, we’ll follow as much as
possible the MVC pattern.

Each android `Activity` inherits from `CustomActivity`

Each `Activity` should call an

` initActionController()`

method. This method instantiates some `MyActivityActionController` that
takes in load the templating of the `Activity`

Directories
-----------

### utils

The `utils` directory is dedicated to some helper routines to facilitate
logging, async loading, touch effects,…

The constants that relies on each android specific devices will b
defined via `Config` singleton class. And the physical constants related
to the incoming raw signal will be defined in Constants.PreProc

### filters

This is related to the image post-processing.

EchOpen will rely on `BoofCV` library as main image processing tool. It
is pure \`JAVA\` libraries, contrary to the well-known `OpenCV`, which
is `C/C++` library.

As specified in the `BoofCV` doc, one have to turn the images - say for
instance bitmap image - in `ImageUInt8` or `ImageFloat32` class in order
to use simply \`BoofCV\`

`  File image = new File($ultrasound_file);`\
`  Bitmap bitmap = BitmapFactory.decodeFile(image.getAbsolutePath());`\
`  ImageUInt8 boofcv_image = ConvertBitmap.bitmapToGray(bitmap, (ImageUInt8) null, null);`

for those interested, here's a
[link](http://boofcv.org/index.php?title=Performance:OpenCV:BoofCV) to
find `OpenCV` vs. `BoofCV` performance benchmark. As said there,
`OpenCV` seems better on low level operations but `BoofCV` seems better
on most of high level operations.

The client does not worry about `BootCV` Images class, they are
instanciated from `BaseImage`. Then client throws to image processor
class an `ImageView` and gets backs a `BitMap` class. Any filter must
inherit from `BaseProcess`. For instance, the app implements this kind
of code corresponding to a wavelette denoising treatment.

` WaveletDenoise waveletDenoise = new WaveletDenoise(image); `\
` waveletDenoise.denoise();`\
` bitmap = waveletDenoise.getBitmap();`

Processing can take a long time. It is recommended to wrap it in an
`AsyncTask` !

PreProc
-------

This deals with scan conversion. The incoming raw signal is formatted in
polar coordinate, so as a (r,theta)-array : the r-coordinate corresponds
to data whose steps are sampled with some fixed step, and the
theta-coordinate corresponds to the angle of the emission-reception
signal line, with again some fixed step. The scan conversion converts
this (r,theta)-array to an (X,Z)-array that fits the pixels of the
device.

Guide to release notes
======================
