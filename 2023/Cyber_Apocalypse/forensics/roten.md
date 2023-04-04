# forensics/Roten

### Description
> The iMoS is responsible for collecting and analyzing targeting data across various galaxies. The data is collected through their webserver, which is accessible to authorized personnel only. However, the iMoS suspects that their webserver has been compromised, and they are unable to locate the source of the breach. They suspect that some kind of shell has been uploaded, but they are unable to find it. The iMoS have provided you with some network data to analyse, its up to you to save us.

We have .pcap with attack on webserver (according to description)

In it we can see that attacker does bruteforce search /{dirname}/galacticmap.php

Before that on packet 1929 we can find that attacker uploaded php file upload. We can extract it from there (map-update.php)

It looks like obfuscated php code with `eval` in the end. We can change `eval` to `echo` to see deobfuscated code (deobfuscated.php)

And flag is in the comment

*HTB{W0w_ROt_A_DaY}*
