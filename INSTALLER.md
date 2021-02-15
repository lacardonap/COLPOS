

# COLPOS
Online GPS Data Processing Service

This is a collection of python scripts for GPS data processing using PPP or DGPS of RINEX file.

This product is free software and it was developed as a thesis work for the  [master's degree in Information and Communication Sciencies](https://rita.udistrital.edu.co/mciencias/) at Francisco José de Caldas District University.

Special thanks to:

* Professor Álvaro Espinal Ortega
* Professor ‪Héctor Mora Páez‬

## Processing software - RTKLib

### [RTKLib](http://www.rtklib.com/) 
RTKLib is an open source program package for standard and precise positioning with GNSS (global navigation satellite system). RTKLIB consists of a portable program library and several APs (application programs) utilizing the library.

**Installation**
```
git clone https://github.com/tomojitakasu/RTKLIB
cd RTKLIB/app/rnx2rtkp/gcc
sudo rnx2rtkp /usr/local/bin
rnx2rtkp -help
```

## Dependencies
### [teqc](https://www.unavco.org/software/data-processing/teqc/teqc.html)
Teqc is a simple yet powerful and unified approach to solving many pre-processing problems with GPS, GLONASS, Galileo, SBAS, Beidou, QZSS, and IRNSS data, especially in RINEX or BINEX format:

* **translation**: binary data reading/translation of native binary formats (optional RINEX file creation for OBS, NAV, and/or MET files or optional creation of BINEX)
* **editing**: including time windowing; file splicing; SV or other filtering; metadata extraction, editing, and/or correction of RINEX header metadata or BINEX metadata records
* **quality check**: quality checking of GPS and/or GLONASS data (native binary, BINEX, or RINEX observation files; with or without ephemerides)

**Installation**

```
wget https://www.unavco.org/software/data-processing/teqc/development/teqc_CentOSLx86_64d.zip
unzip teqc_CentOSLx86_64d.zip
cp teqc /usr/local/bin
```

### [Hatanaka-compressed format](https://terras.gsi.go.jp/ja/crx2rnx.html)
RNXCMP is the software for compression/restoration of RINEX observation files developed by Y. Hatanaka of GSI. It converts the foramt of GNSS observation files from the RINEX format (version 2.xx or 3.xx) to a compressed format (the CompactRINEX format, or often called the Hatanaka-compressed format) and vice versa.


You should have installed csh
```
sudo apt install csh
```

### Install GCC
Install the GNU Compiler Collection (GCC)
```
sudo apt install build-essential gcc
```

### Config archive access
https://cddis.nasa.gov/Data_and_Derived_Products/CreateNetrcFile.html

### Antenna calibration
[IGS14 Reference Frame Transition](http://www.igs.org/article/igs14-reference-frame-transition)

[ngs14.atx](https://www.ngs.noaa.gov/ANTCAL/LoadFile?file=ngs14.atx)
[igs14.atx](ftp://www.igs.org/pub/station/general/igs14.atx)


### RabbitMQ
sudo apt install rabbitmq-server
systemctl status  rabbitmq-server.service
systemctl is-enabled rabbitmq-server.service
sudo rabbitmq-plugins enable rabbitmq_management
ss -tunelp | grep 15672 
sudo ufw allow proto tcp from any to any port 5672,15672

https://computingforgeeks.com/how-to-install-latest-rabbitmq-server-on-ubuntu-linux/

https://www.rabbitmq.com/tutorials/tutorial-one-python.html
pip3 install pika --upgrade

We use javascript to send the processing request.
https://www.rabbitmq.com/tutorials/tutorial-one-javascript.html

You must install npm and node
https://www.how2shout.com/how-to/how-to-install-node-js-on-ubuntu-19-04.html
npm install amqplib

