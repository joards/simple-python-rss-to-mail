#!/bin/python

import calendar
import time
import feedparser

def cTL(tidutc):
    return time.localtime(calendar.timegm(tidutc))
def cTU(tidloc):
    return time.mktime(tidloc)

def sjekkFeed(feed, lesttall):
    antallNyePoster = 0;
    sammendrag = []
    tittler = []
    linker = []
    datoer = []

    tidlocup = cTL(feed["feed"]["updated_parsed"])
    unixtid = cTU(tidlocup)

    if (lesttall >= unixtid):
        return " ", str(unixtid), antallNyePoster
        
    nytid = str(unixtid)
    for po in feed["entries"]:
        if ( calendar.timegm(po["updated_parsed"]) <= lesttall ):
            break
        antallNyePoster += 1
        sammendrag.append(po.get("summary", " "))
        tittler.append(po.get("title", " <no title> "))
        linker.append(po.get("link", " <no link> "))
        datoer.append(time.strftime("%Y-%m-%d %H:%M:%S",cTL(po["updated_parsed"])))
        
    str_list = []
    for i in range(0,antallNyePoster):
        str_list.append('dato: ')
        str_list.append(datoer[i])
        str_list.append('\n Tittel: ')
        str_list.append(tittler[i])
        str_list.append('\n Sammendrag: ')
        str_list.append(sammendrag[i])
        str_list.append('\n Link: ')
        str_list.append(linker[i])
        str_list.append('\n\n')
    bodyTekst = ''.join(str_list)

    return bodyTekst, nytid, antallNyePoster