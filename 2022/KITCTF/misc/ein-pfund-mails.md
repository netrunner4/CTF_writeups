# misc/ein-pfund-mails

### Description
> Someone leaked a bunch of emails from the CTF orga. Sadly there is no way to know which one is real...

We are given an archive with many .eml files signed with dkim signatures, only difference between them is flag in the message body

By the description of the task we can understand that we need to verify these mails and find real one

I found `dkimpy` library and made this bash script using it:

```bash
#!/bin/bash
FILES="./*"
for f in $FILES
do
  echo "Processing $f file..."
  cat "$f" | dkimverify
done
```

In output we can see that 438b5.eml has correct signature:
```
Processing ./438b5.eml file...
signature ok
```

Flag in this file is KCTF{1f8e659e892f2b2a05a54b8448ccbff9}
