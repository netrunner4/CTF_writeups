# web/Troubleshooting

### Description
> Лишаючи щілину у дверях, завжди будь готовим, що хтось зможе підглядати.

On the page we can see functionality that lets us send requests to any url (SSRF)

![troubleshooting1](/2023/UA30/web/images/troubleshooting1.png)

I initially tried to do a request to myself (vpn was used to connect to ctf's network) but with no succes

Then I tried 127.0.0.1 and 0.0.0.0. Last one worked and made PDF with main page

After some guessing I found that `http://0.0.0.0/flag.txt` contains flag

*ctf{i_know_you_have_to_type_it_from_screen}*
