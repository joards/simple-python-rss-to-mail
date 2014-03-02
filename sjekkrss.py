#!/bin/python
import calendar
import time
import feedparser
import msender
import hentrss
import iorss

def sjekk():
    tiderUt = []
    adresser, tider, navn = iorss.lesConfig()
    while (len(adresser) > len(tider)):
        tider.append(float(0.0))


    iorss.skrivtillog("sjekker rss " + time.strftime("%Y-%m-%d %H:%M:%S"))
    
    for ind in range(len(adresser)):
        mixed = adresser[ind]
        ltall = tider[ind]
        feed = feedparser.parse(mixed)
        bodyTekst, nytid, antallNyePoster = hentrss.sjekkFeed(feed, ltall)
        emnefelt = str(antallNyePoster) + " nye beskjeder fra rss"
        if (len(navn) > ind):
            emnefelt = str(antallNyePoster) + " nye beskjeder i kurset " + navn[ind]

        tiderUt.append(nytid)

        if (antallNyePoster > 0):
            msender.sendTingiMail(bodyTekst, emnefelt)
            iorss.skrivtillog("sendt mail " + time.strftime("%Y-%m-%d %H:%M:%S"))

    iorss.skrivTilConf(adresser, tiderUt, navn)

if __name__ == "__main__":
    sjekk()

