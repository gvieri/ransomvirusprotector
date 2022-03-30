#!/usr/bin/python
######################################################
### (c) Giovambattista Vieri 2022 All Rights Reserved
### License AGPL V 3.0
######################################################

import sys
import math
import requests
import hashlib
import argparse
from pprint import pprint



##########################################

def getOptions(args=sys.argv[1:]):
    parser=argparse.ArgumentParser(description='program description')
    parser.add_argument('-H','--header', help='header file name which file contents will preponed to program output', action='store', dest="headerfilename" )
    parser.add_argument('-p','--prefix', help='line prefix', action='store',default='',  dest='prefix' )
    parser.add_argument('-c','--countries', help='cpuntries\'s ip that will be used as: RU,IT...', action='store', dest='countrieslist' )
    parser.add_argument('-P','--postfix', help='text to be written at line end', action='store', default='', dest='postfix' )
    parser.add_argument('-v','--verbose', help='more verbose output', action='store_true')

    opt=parser.parse_args(args)
    return(opt)

##########################################

def addressList():
    al=[]
    with open(fn, 'r') as f:
    
        for line in f.readlines():
            s=line.split("|")
            if (('ipv4' in line) & (s[1] in listofcountry)) :
                verbp(line)
                s=line.split("|")
                net=s[3]
                cidr=float(s[4])
                final_cidr= (str(net) + "/" +  str( math.trunc((32-math.log(cidr,2))) ))
                al.append(final_cidr)
    return(al)

##########################################

def verifyFileMd5(f,m):

    with open(m,'r') as md5h:
        original_md5 = md5h.read().split(" = ") [1]

    with open(f, 'rb') as fnh:
        md5_returned = hashlib.md5(fnh.read()).hexdigest()

    if original_md5 == md5_returned:
        return(True)
    else:
        return(False)

##########################################

def download(site,file):
    r=requests.get(site+file)
    r.raise_for_status()
    f= open(file,"w")
    f.write(r.text)
    f.close()

verbose=False

##########################################
if __name__ == "__main__":


    fn     = 'delegated-ripencc-latest'
    md5fn  = 'delegated-ripencc-latest.md5'


    download("https://ftp.ripe.net/pub/stats/ripencc/",fn)
    download("https://ftp.ripe.net/pub/stats/ripencc/",md5fn)

    opt=getOptions()
    verbose=opt.verbose
    verbp= print if verbose else lambda *a, **k: None
    if(verbose):
        pprint(opt)

    listofcountry=tuple(opt.countrieslist.split(','))

###### verify md 5
    if verifyFileMd5(fn,md5fn):
        verbp ("MD5 verified.")
    else:
        verbp ("MD5 verification failed!.")

   
    addresslist=tuple(addressList())
    f=opt.headerfilename
    if(f):
        with open(f, 'r') as fnh:
            print(str(fnh.read()))

    for a in addresslist:
        print(str(opt.prefix)+a+str(opt.postfix))

