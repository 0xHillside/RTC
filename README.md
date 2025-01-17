# RTC, short for Rubeus To Cache
Rubeus To Cacche is a python tool to decode base64-encoded Kerberos tickets and convert them into .ccache files

A tool that makes interoperability between linux and windows systems easier, I made this tool so I wouldnt waste 5 more seconds when doing a box or anything of the sort

## WARNING
script uses calls for impacket-ticketConverter, so if you have it under the name ticketConverter.py change it in the script then.


# Installation & Dependencies

```
git clone https://github.com/0xHillside/RTC
```

Dependencies to install
```
pip install impacket
```


## Usage
```
kali@kali ~> r2tc -h
usage: r2tc [-h] [-f FILE] [-r READ]                                                                                
                                                                                                                    
options:                                                                                                            
  -h, --help            show this help message and exit                                                             
  -f FILE, --file FILE  The txt file containing the base64 ticket                                                   
  -r READ, --read READ  The base64 text itself containing the ticket                                                
```

### Using it quickly 
File argument
```
kali@kali ~> rtc -f tickethere.txt
[+] text file provided: tickethere.txt
[+] kirbii file saved: tickethere.kirbii
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] converting kirbi to ccache...
[+] done
[+] ccache file saved: tickethere.cacche

```

The read argument

```
kali@kali ~> rtc -r "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"
[+] text provided: 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
[+] text file saved: ticket.kirbii
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] converting kirbi to ccache...
[+] done
[+] cacche saved: ticket.cacche
```
