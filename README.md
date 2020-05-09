# COLPOS
Online GPS Data Processing Service

This is a collection of python scripts for GPS data processing using PPP or DGPS of RINEX file.

## Processing software - RTKLib

[RTKLib](http://www.rtklib.com/) is an open source program package for standard and precise positioning with GNSS (global navigation satellite system). RTKLIB consists of a portable program library and several APs (application programs) utilizing the library.

**Installation**
```
git clone https://github.com/tomojitakasu/RTKLIB
cd RTKLIB/app/rnx2rtkp/gcc
sudo rnx2rtkp /usr/local/bin
rnx2rtkp -help
```

## Dependencies
[teqc](https://www.unavco.org/software/data-processing/teqc/teqc.html)
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

## Install GCC
Install the GNU Compiler Collection (GCC)
```
sudo apt install build-essential gcc
```

## Config archive access
https://cddis.nasa.gov/Data_and_Derived_Products/CreateNetrcFile.html

## Antenna calibration
[IGS14 Reference Frame Transition](http://www.igs.org/article/igs14-reference-frame-transition)

[ngs14.atx](https://www.ngs.noaa.gov/ANTCAL/LoadFile?file=ngs14.atx)
