# web/Search Engine

### Description
> Чи знайдете ви свою відповідь?

Upon opening page we can see input form with exaple text below.

![search_engine1](/2023/UA30/web/images/search_engine1.png)

Looks like it takes response from backend and loads it on new page

![search_engine2](/2023/UA30/web/images/search_engine2.png)

Could it be SQLi?

Yes, entry point is `'`

On `Capital of United Kingdom'` it answers with what looks like 500 error

![search_engine3](/2023/UA30/web/images/search_engine3.png)

So we have SQLi so we can check manually or use sqlmap, I did the last one

`sqlmap -u https://search-engine.ua30ctf.org/submit --data="question=Capital of United Kingdom" --dump`

And we have the flag

*CTF{1_n3Ed_An5w3rS}*
