# web/Search Engine

### Description
> Коли у вас з'явиться можливість ставити запитання - використовуйте її якомога різноманітніше, не бійтесь задавати нетипові питання, адже диявол ховається у деталях.

On main page we see 2048 game without anything interesting

With gobuster we can find **/admin** page with password recovery functionality

[!image1]

Looks like we need to find/guess mail

After some tries email `admin@ua30ctf.com` gave us link to recovery page

[!image2]

But it had number covered with six **x** letters, so it's obvious that this is 6 number token

I used ffuf to brute-force it

`ffuf -u 'https://hi-jack.ua30ctf.org/admin/recovery.php?token=FUZZ' -w ~/CTF/UA30/6-digits-000000-999999.txt -ac`

FUZZ: 286653

So we open `https://hi-jack.ua30ctf.org/admin/recovery.php?token=286653` and get the flag

*ctf{sugar_is_a_poison}*
