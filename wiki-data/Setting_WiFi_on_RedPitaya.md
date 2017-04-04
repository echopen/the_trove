1.  Setting WiFi on RedPitaya

We're using a Livebox, so we can check the list of connections through :

[`http://192.168.1.1/`](http://192.168.1.1/)

The RedPitaya we have has MAC addresses, visible through ifconfig, that
are:

-   Ethernet: XX:06:82
-   WiFi (through the EDIMAX dongle): XX:46:F9

### dnsmasq

Renamed as dnsmasq.old

Changes in files
================

init.d/rcS
----------

One line was added to enable starting the pitaya as it boots:

`ifconfig wlan0 up`

In network/
-----------

mv interfaces.ap interfaces.ap.old mv hostapd hostapd.old

### wpa\_supplicant.conf

`ctrl_interface=/var/run/wpa_supplicant`\
\
`# WPA configuration example`\
`network={`\
`       ssid="`*`ECHOPEN`*`"`\
`       psk="`*`password`*`"`\
`}`

interfaces
----------

![](interfaces.png "interfaces.png")

config
------

![](config.png "config.png")
