# RansomVirusProtector

## firewall script creator based on countries' internet block net addresses

### Introduction 
We live in tragic times where war is returning in Europe. After that we had death and destruction in AF, YU, SY and, a lot of both African/Asian places. 
Now we have to face cyberwar and rogue cyber attacks. I can't do anything to stop a cyber war but I really hope this script will become useful to SME owners and healthcare organizations. 
In brief: malware needs to "phone home" for both activation and to exfiltrate stolen data. It will phone home to get the 'key' to encrypt all your data before asking for ransom. 

What if it can't "phone home"? nothing... It will wait and try to communicate with its owner by using other means. But a firewall correctly configured can buy you some time to fix the thing. 

So I have written and published this script that I use as a sort of "swiss knife" to block suspect ip coming from a given country or a set of countries 

I'm using on Linux but it can be used on windows too. You can try on WSL (Linux on Windows) and maybe from PowerShell. 

The license ? AGPL. Look at it. 


### Technologies
* python 3

### Data source
1. RIPE

### Examples
1. Obtain the:
* net blocks related to France:  python ransomvirusprotector.py -c FR
* net blocks related to Italy and France: python ransomvirusprotector.py -c FR,IT

2. Do you want to know the command to block:
* All russian IP addresses: python ransomvirusprotector.py -c RU -p "iptables -I INPUT -s " -P " -j REJECT"

Create the file h.txt with the following content:
iptables flush

Then:
ransomvirusprotector.py -c DE -p "iptables -I INPUT -s " -P " -j REJECT" > script.sh 

You will obtain a simple script that blocks all the connection coming from Germany. 


### Installing

You need python 3 and you need to install request. If you use conda, you can give the command: conda install -c anaconda requests. If you prefer pip: pip install requests. 

If you like to have a separate environment for this tool: conda create -n ransomprotector python=3.9 requests -y. 

To install the script you can download the script alone or, you can clone the whole repository. 

