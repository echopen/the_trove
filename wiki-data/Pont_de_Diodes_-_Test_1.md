1.  Pont de Diodes - Test 1

Schematics
----------

Using our transducer, we're adding the protection circuit

![](TrnsCvr.PNG "TrnsCvr.PNG")

Files
-----

[http://echopen.org/attachments/29-09-15%20Ecreteur.zip Archive is
here](http://echopen.org/attachments/29-09-15%20Ecreteur.zip_Archive_is_here "wikilink")

Principle
---------

The protection circuit includes D3-D6 and R2-R3. When there is no input,
D3-D6 are all open. The voltage at D3-D5 joint is the same as that at
D4-D6.

When there is a small positive voltage signal comes in and causes input
voltage at right side of C2 to increase but less than +4.3v, the voltage
at R3 will increase accordingly and thus the output voltage at left side
of C3. The output voltage only increases when D4 and D6 are open. It
will stop at 4.3v no matter how high is the input.

When there is a small negative voltage signal comes in causing input
voltage at right side of C2 to decrease but still higher than 0.7v, the
voltage at R3 will drop accordingly and thus the output at right side of
C3. The same as above mentioned, the output will stop at 0.7v no matter
how low the input voltage goes.

Data
----

                 Detail                                        Global
  -------------- --------------------------------------------- -----------------------------------------------
  Output         ![ 500px](LOW Out Detail.png " 500px")        ![ 500px](LOW Out Global.png " 500px")
  Input          ![ 500px](HIGH Out Detail.png " 500px")       ![ 500px](HIGH Out Global.png "fig: 500px") !
  Disconnected   ![ 500px](Disconnected Detail.png " 500px")   ![ 500px](Disconnected Global.png " 500px")
