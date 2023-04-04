# web/Didactic Octo Paddle

### Description
> You have been hired by the Intergalactic Ministry of Spies to retrieve a powerful relic that is believed to be hidden within the small paddle shop, by the river. You must hack into the paddle shop's system to obtain information on the relic's location. Your ultimate challenge is to shut down the parasitic alien vessels and save humanity from certain destruction by retrieving the relic hidden within the Didactic Octo Paddles shop.

After opening website we can see login page and we can find register page.
![didactic_octo_paddle1](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle1.png)
![didactic_octo_paddle2](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle2.png)

By trying to register as admin we understand that user exists
![didactic_octo_paddle3](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle3.png)

Logging in gives us access to items list, with nothing interesting and JWT token. It uses HS256 and contains id
![didactic_octo_paddle4](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle4.png)

We can look up how it works in source code
![didactic_octo_paddle5](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle5.png)

It checks for “none” algorithm but only in lowercase. It can be abused

jwt_tool confirms it (with id set to 1)
![didactic_octo_paddle6](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle6.png)
*1148 byte response is redirect to login page*

On admin page we have list of active users
![didactic_octo_paddle7](/2023/Cyber_Apocalypse/web/images/didactic_octo_paddle7.png)

It is implemented by this string:

			`res.render("admin", {
               users: jsrender.templates(`${usernames}`).render(),
           });`

Which is vulnerable to SSTI using this payload(**":"** added because website uses JsRender):
`{{:7*7}}`

And then we construct payload to read file.txt and open admin page
`{"username":"{{:\"pwnd\".toString.constructor.call({},\"return global.process.mainModule.constructor._load('child_process').execSync('cat ../flag.txt').toString()\")()}}","password":"123"}`

*HTB{Pr3_C0MP111N6_W17H0U7_P4DD13804rD1N6_5K1115}*
