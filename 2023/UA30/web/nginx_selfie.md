# web/Nginx Selfie

### Description
> До безпеки сайтів завжди необхідно підходити послідовно, починаючи від правильного режиму підтримки, завершуючи правильним налаштуванням веб-серверу.

Used gobuster as usual, found **/uploads** page

![image1]

After playing with link I found out that **/upload../** gives us access to root directory

From it I went to **/home** and found flag

Full link is `https://nginx-selfie.ua30ctf.org/uploads../home/flag.txt`

*ctf{Commander8071973}*
