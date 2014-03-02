simple-python-rss-to-mail
=========================

Simple rss update checker that sends email with new posts


addresses of rss feeds are put in the con.cfg file with the prefix "address: "
last updated and title can also be included, the order defines correlation

The email sender(msender.py) is dependent on a gmail user and a email address to send to.

To make it work in a cronjob absolute paths and right premissions helps considerably.

PS: names and text are in norwegian