[![DOI](https://zenodo.org/badge/281990935.svg)](https://zenodo.org/badge/latestdoi/281990935)

# Cronotipy

<img src="/cronotipy/figs/logo.svg?raw=true" width=75 align="right">

A simple customizable notification scheduler created using the python language and the pyqt5 framework. This application uses tools native to the Linux environment such as "Notify" from the gi repository and the sox package for sound notifications. This application was tested on PopOS 20.04, Ubuntu 20.04, Mint 20 and Elementary OS 5.1.

<img src="/cronotipy/figs/cronotipy.png?raw=true" align="center">

# Installation
This application depends on some dependencies for gi notify and sox works.

```
$ sudo apt-get install python3-setuptools python3-pyqt5 python3-gi python3-gi-cairo gir1.2-notify-0.7 sox
```

<li><b>Install via setuptools</b></li>

```
git clone https://github.com/jeffrichardchemistry/cronotipy
cd cronotipy
sudo python3 setup.py install
```

<li><b>Install in VirtualEnv</b></li>

May not work on VirtualEnvs directly, so install pip dependencies manually.

```
venv$ pip3 install PyGObject pycairo PyQt5
```

and then install cronotipy.
```
venv$ git clone https://github.com/jeffrichardchemistry/cronotipy
venv$ cd cronotipy
venv$ python3 setup.py install
```

<li><b>Install via Deb package</b></li>
This is the easiest way.

[Download deb](https://github.com/jeffrichardchemistry/cronotipy/raw/master/deb/cronotipy_1.0.0-1_all.deb)
and install by double clicking with your preferred installer (gdebi, eddy etc)<br>

Or install via terminal

<b>with gdebi</b>
```
wget https://github.com/jeffrichardchemistry/cronotipy/raw/master/deb/cronotipy_1.0.0-1_all.deb
sudo gdebi cronotipy_1.0.0-1_all.deb
```

<b>Or with dpkg</b>
```
wget https://github.com/jeffrichardchemistry/cronotipy/raw/master/deb/cronotipy_1.0.0-1_all.deb
sudo dpkg -i cronotipy_1.0.0-1_all.deb
sudo apt install -f
```

# Run
To run this application type in a linux terminal:
```
$ cronotipy
```
