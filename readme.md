# AlertHooks
A simple program to send discord webhook messages using cmd-line.

## Install

Install via pip:
```bash
pip install alertHooks
```

## Add a webhook using an alias
``` bash
alertHooks add -a "ALIAS" -u "URL"
```

## Remove a webhook using an alias
``` bash
alertHooks rm -a "ALIAS"
```

## List available aliases
``` basg
alertHooks ls
```

## Send messages 

``` bash
alertHooks -a "ALIAS" -m "YOUR MESSAGE HERE"
```