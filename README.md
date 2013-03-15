Commodore 64 Serial Printer
===========================
This repo contains Arduino code to drive a C64 serial printer, bodged by Al, John H and New Mike to emulate a generic serial printer. The Arduino code is modified from [Tapani Rantakokko's original](http://www.rantakokko.net/tapani/blog/2009/06/02/interfacing-old-commodore-64-printers-with-arduino/).

There's also a python script to delay piped output to the serial port to avoid overrunning the serial buffers. This needs work.

We have used jp2a to convert JPEGs into ASCII art for output like this:
jp2a -i logo.jpg |python delay.py > /dev/ttyACM0
