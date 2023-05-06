# web/Under Construction

### Description
> Сайт перебуває на повній реконструкції, але, можливо, старі сторінки все ще доступні?

Started gobuster (obvious from description)

`gobuster dir -w /usr/share/wordlists/dirb/common.txt -u https://under-construction.ua30ctf.org/`

It found **/administrator**, so I opened it and in source code there was an interesting comment

`<!--TODO: Review /developernotes-->`

So I opened **/developernotes** and there was the flag 

*ctf{d1r3ctOry_3numEr4T10n}*
