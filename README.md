# RansomVirusProtector

## firewall script creator based on countries' internet block net addresses

### Introduction 
We live in tragic times where war is returning in Europe. This, After we have witnessed death and destruction in Afghanistan, Yugoslavia, Syria, and many countries in Africa and Asia.


Now we have to face cyberwar and rogue cyberattacks. I can't do anything to stop a cyber war but I really hope this script will become useful to SMEs and healthcare organizations. 
In brief: malware needs to "phone home" for both activation and to exfiltrate stolen data. It will phone home to get the 'key' to encrypt all your data before demanding for ransom. 

What if it can't "phone home"? Nothing will happens. It will wait and try to communicate with its owner using other means. But a firewall correctly configured can buy you some time to fix the thing. 

So I have written and published this script, which I use as a sort of "swiss army knife" to block suspect IP addresses coming from a given country or a set of countries. 

I'm using it on Linux but it can be used on Windows too. You can try on WSL (Windows Subsystem for Linux) and possibly via PowerShell. 

The license ? AGPL. Look at it. 


### Technologies
* Python 3

### Data source
1. RIPE

### Examples
1. To obtain the some net blocks:
* net blocks related to France:  python ransomvirusprotector.py -c FR
* net blocks related to Italy and France: python ransomvirusprotector.py -c FR,IT

2. To block IP addresses, use the following command:
:
* All Russian IP addresses: python ransomvirusprotector.py -c RU -p "iptables -I INPUT -s " -P " -j REJECT"

Create the file h.txt with the following content:
iptables flush

Then:
python ransomvirusprotector.py -c DE -p "iptables -I INPUT -s " -P " -j REJECT" > script.sh 

You will obtain a simple script that blocks all connections coming from Germany. 


### Installing

You need python 3 and you need to install request. If you use conda, you can run the command: conda install -c anaconda requests. If you prefer pip: pip install requests. 

If you like to have a separate environment for this tool: conda create -n ransomprotector python=3.9 requests -y. 

To install the script you can download the script alone or clone the whole repository. 

