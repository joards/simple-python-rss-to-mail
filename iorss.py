#!/bin/python

def lesConfig():
    adresser = []
    sistoppdatert = []
    navn = []
    aPre = "address:"
    tPre = "last updated:"
    hPre = "title:"
    try:
        f = open("con.cfg", "r")
        for line in f:
            lst = line.strip()
            if (lst.startswith("#")):
                continue
            if (lst.startswith(aPre)):
                adresser.append(lst[9:])
            elif (lst.startswith(tPre)):
                sistoppdatert.append(float(lst[14:]))
            elif (lst.startswith(hPre)):
                navn.append(lst[7:])
    except:
        pass
    finally:
        f.close()
    return adresser, sistoppdatert, navn

def skrivtillog(tillog):
    try:
        f = open("rssscript.log", "a") #passer bra inn i /var/log/
        f.write(tillog + " \n")
        f.close()
    except:
        pass


def skrivTilConf(adresser, sistoppdatert, navn):
    try:
        f = open("con.cfg", "w")
        for i in adresser:
            f.write("address: " + i + " \n")
        for i in sistoppdatert:
            f.write("last updated: " + str(i) + " \n")
        for i in navn:
            f.write("title: " + i + " \n")
        
    except:
        pass
    finally:
        f.close()

