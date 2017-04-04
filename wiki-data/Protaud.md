1.  Protaud

Planning the V0.0
=================

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Planning détaillé |----      Septembre S1   Septembre S2   Septembre S3   Septembre S4 |----   Assemblage   -   Tranducers testing                       -   Low voltage circuit :      -   Physical structure                      -   Assembling   Documentation            |----   Challenges   -   Low tension circuit : Arduino is not fast enough to read and write         
                                                                                                              -   Connecting Arduino - Transducer 40 kHz       1.  CNA                    -   Circuit assembling (High/Low) + Relay   -   Testing                                                                                                                                   
                                                                                                              -   Motor :                                      2.  CAN                    -   Phantom : produce or recover                                                                                                                                                          
                                                                                                                  1.  Power supply                         -   High voltage circuit                                                   |----                                                                                                                                         
                                                                                                                  2.  Encoder operation                                                                                                                                                                                                                                             
                                                                                                              -   Communication Arduino-Computer           1.  Transducer amplification                                                                                                                                                                                             
                                                                                                              -   Ultra fast data transfer                 2.  Power supply                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                           <li>                                                                                                                                                                                                                     
                                                                                                                                                           Relay                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                           </li>                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                    
  ------------------------- -- -------------- -------------- -------------- -------------------- ------------ -------------------------------------------- ------------------------------ ------------------------------------------- ---------------- --------------- -- -- -- ------- ------------ ------------------------------------------------------------------------ -- -- --
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Electronical issue
==================

The arduino don't allow us to sampling the analogical data comming from
the transducer at the right frequency. We want to sample the signal at
80 MHz in the first time. We can do this with the red pitaya board which
have 14 bits DAC and ADC sampling at 125 Msps.

We know how to drive the motor with the encodor with the arduino. So at
the beggining, for simplifying the problem, we can continue to drive the
motor with the arduino. When the transducer will be at the right place,
the arduino will send a pulse (trigger signal) to the red pitaya for
initiating an acquisition sequence. So the mixing red pitaya/arduino due
protaud will be like that :

![](Mixing Red Pitaya and Arduino Due.png "Mixing Red Pitaya and Arduino Due.png"){width="500"}

In a second time we will make a full red pitaya protaud :

![](Full red pitaya.png "Full red pitaya.png"){width="500"}

Protaud's life
==============

week 1
------

It appears that we can't sampling the emitted and received signal's at
80 MHz even by connecting 80 Msps DAC and ADC to the arduino. So we have
discuss with some people to figure a satiffying simple solution. A
second microcontroler? A FIFO?

On second hand, we have look how to acces high datarate with the arduino
and receive data with python. The function Serial.write(buf,len) is the
key (not the classical Serial.println() function which convert data into
ASCII format, so it's a slow function).

week 2
------

It appears the red pitaya board seems to be a good option because it has
2 DAC and 2 ADC with a 14 bits resolution sampling at 125 MHz, all we
need and relatively easy to use. We got one, and now we will test this
board shortly. We are confident.
