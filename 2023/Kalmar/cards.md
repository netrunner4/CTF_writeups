# forensic/cards

### Description
> Follow the shuffle.

We have pcap file with FTP packets, opened it with wireshark
If we follow TCP stream we can find around 80 similar FTP connections

Example:
```
220 FTP Server
USER user
331 Please specify the password.
PASS 123
230 Login successful.
SYST
215 UNIX Type: L8
CWD 342
250 Directory successfully changed.
TYPE I
200 Switching to Binary mode.
PASV
227 Entering Passive Mode (0,0,0,0,156,70).
RETR flagpart.txt
150 Opening BINARY mode data connection for flagpart.txt (1 bytes).
226 Transfer complete.
QUIT
221 Goodbye.
```
Here we can see that user conncets to server, chooses directory (342) and recieves one byte of data which is part of the flag
So now we can use `data` filter in wireshark to see all flag's parts, but they sent in random order

To find out which letter is connected to which directory we can use this filter (N is number of stream):
`data or (frame contains "CWD" or frame contains "BINARY") and tcp.stream eq N`

And this way we can connect each directory to its letter - first data packet sent after packet containing BINARY has part of flag corresponding to directory number in chosen stream. Do this to all streams and get flag

*kalmar{shuffle_shuff1e_can_you_k33p_tr4ck_of_where_th3_cards_are_shuffl3d_n0w}*

