1.  Transducer Models

\
=Fully integrated CMOS ultrasound transceiver chip for high-frequency
high-resolution ultrasonic imaging system=\
\
![](Thesis_Insoo_Kim.pdf "fig:Thesis_Insoo_Kim.pdf")\
\

Avis
----

Document très riche. Présente la fabrication d'une sonde échographique
haute fréquence (&gt;10MHz) et haute résolution. Un historique des
technologies est fait.\
Le sujet est axé **électronique**.\

Images
------

\
![](digital-ultrasound-imaging-system.png "fig:digital-ultrasound-imaging-system.png")\
\
\
![](huygens-principle.png "fig:huygens-principle.png")![](imaging-system.png "fig:imaging-system.png")\
\
\
![](dynamic-focusing-and-steering-delay.png "fig:dynamic-focusing-and-steering-delay.png")\
\
\
![](abf-system.png "fig:abf-system.png")\
\
\
![](abf-system2.png "fig:abf-system2.png")\
\
\
![](dbf-system.png "fig:dbf-system.png")![](dbf-system2.png "fig:dbf-system2.png")\
\
\
![](ascan-bscan.png "fig:ascan-bscan.png")\
\
\
![](preamplifier-core-circuit-scheme.png "fig:preamplifier-core-circuit-scheme.png")\
\
\
![](receiver-block-diagram.png "fig:receiver-block-diagram.png")\
\
\
![](sonicWindow.png "fig:sonicWindow.png")![](spectrum.png "fig:spectrum.png")\
\
\
![](fga-chip-simplified.png "fig:fga-chip-simplified.png")![](FPGA.png "fig:FPGA.png")\
\
\
![](transceiver-chip.png "fig:transceiver-chip.png")\
\
\
![](transceiver-chip-floor-plan.png "fig:transceiver-chip-floor-plan.png")\
\
\
![](TIQ-ADC-block-diagram.png "fig:TIQ-ADC-block-diagram.png")\
\

Table des matières
------------------

### LIST OF FIGURES

### LIST OF TABLES

### ACKNOWLEDGEMENTS

#### Chapter 1 Introduction to High-frequency Ultrasound Imaging

##### Applications of Ultrasound

##### Research Motivation and Goal

##### Previous Related Work

###### Emergence of Ultrasound ASIC Chips and Digital Beamforming

###### Closed-Coupled Electronics

###### FPGA-based Systems

###### Commercial Ultrasound Chipsets

##### Challenges and Approaches

##### Thesis Organization

#### Chapter 2 Fundamentals of Ultrasonic Imaging Systems

##### Principles of Ultrasound Imaging

###### Ultrasound Wave Physics

###### Brightness Mode (B-Mode) Ultrasound Imaging

###### Resolution

##### Beamforming

###### Huygens Principle, Diffraction, and Beamforming

###### Analog Beamforming vs. Digital Beamforming

##### B-Mode Ultrasound Imaging System

###### System Overview

###### Ultrasound Front-end

#### Chapter 3 Proposed High-frequency Ultrasound Imaging System

##### Configuration of the Proposed Ultrasound Imaging System

##### Transceiver Chip Architecture

###### Closed-Coupled Electronics Scheme

###### Proposed System’s Architectural Features

##### Function Definition

###### Major Functions

###### Mode-set configuration

###### Operational Flow

#### Chapter 4 Design of the Ultrasound Transceiver Chip

##### Receiver

###### Required Specifications

###### Circuit Diagram

##### A/D Converter

###### Required Specifications

###### Configuration of the TIQ ADC

###### TIQ Comparator

###### Design Automation of the TIQ Comparator

###### Analytical Model-based Design Methodology

###### Encoder

##### SRAM

###### Required Specifications

###### Design Details

##### Transmitter

#### Chapter 5 Simulation and Results

##### Transceiver Chip Characterization

###### First-generation Chip

###### Second-generation Chip

##### Ultrasound Transducer Characterization

###### Thin Film Ultrasound Transducer Array

###### Composite High Frequency Ultrasound Transducer Array

##### Pulse Echo Experiments

###### Pitch Mode Experiments

###### Catch Mode Experiments

###### Pitch–catch Mode Experiments

### Chapter 6 Future Work

##### Differential Input Quantization ADC

##### Ultrasound Imaging System Simulation Model

##### Integration of DBNS DSP

### Chapter 7 Conclusions

### References

### Appendix A Auto-tuning Software C++ Code

### Appendix B MATLAB Programming Code for Channel Delay Calculation

<Category:Emission> <Category:Bibliographie> <Category:Sonde>
<Category:Receiving> <Category:Transmitter>
