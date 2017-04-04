1.  Estimating datarates

Objective
=========

Trying to get data from the Red Pitaya. Specs are as follows:

-   10 cm back and forth at 1500m/s amounts to 130µs
-   Acquisition at 125MHz gets 16234 points for 130µs
-   Display a line using the arduino trigger.

UI

-   Should have the graph with points
-   Should have a button to download the raw points.

Steps
=====

Setup
-----

1.  Uploaded the <https://github.com/RedPitaya/RedPitaya> project into
    <https://github.com/kelu124/rechOpen>
2.  Updated development tools on dev machine
    1.  Enable Linaro toolchain repository (only required for Ubuntu
        10.04 users):
        1.  sudo add-apt-repository ppa:linaro-maintainers/toolchain
        2.  sudo apt-get update

    2.  Install build-essential and ARM cross compiler:
        1.  sudo apt-get install build-essential
        2.  sudo apt-get install gcc-arm-linux-gnueabi

3.  Getting the in the applications folders, *make
    CROSS\_COMPILE=arm-linux-gnueabi- clean all* creates the
    **controller.so** object ... (remark: and creates if not existing
    the src/ folder)

Getting new apps (and codes?)
=============================

Going onto the bazaar, getting the programs, having them installed,
getting those into the dev machine, and uploading..

Why? Because the simple oscilloscope program was not functioning... and
to get more code to understand

Code
====

The controller interesting code for the oscilloscope is in:

-   <https://github.com/kelu124/rechOpen/blob/master/Applications/scope/src/worker.c>

Structure
=========

### TLDR

RP stores data prepared by the Controller to the <RPIP>/data endpoint
(JSON) so that the webapp that requires it gets it. The UI serves the
data once formatted. The controller is a controller.so file in each of
the <app_name> folder, cross-compiled.

### More details

Each Red Pitaya WEB application consists of three basic elements:

-   WEB based user interface - enables user to control and represent
    acquired data provided by controller from the WEB browser
-   Controller - used for connection between WEB interface & FPGA
-   FPGA image for FPGA that connects the Red Pitaya with periphery
    (ADCs, DACs and other)

WEB applications are located in /opt/www/apps/<app_name> on Red Pitaya.
Source code of applications is available at the same location as well as
at Red Pitaya Applications repository on GitHub. The FPGA logic control
registers are documented on the "Red Pitaya WEB application structure
detailed overview"
![](500px-WEB_app_structure.png "fig:500px-WEB_app_structure.png")

Alternatives
============

Resources
=========

-   <http://wiki.redpitaya.com/index.php?title=Developer_Guide>
-   <http://wiki.redpitaya.com/index.php?title=Red_Pitaya_WEB_application_structure_detailed_overview>
