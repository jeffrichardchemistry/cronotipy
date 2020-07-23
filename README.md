# Cronotipy
A simple customizable notification scheduler created using the python language and the pyqt5 framework. This application uses tools native to the Linux environment such as "Notify" from the gi repository and the sox package for sound notifications.

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
May not work on VirtualEnvs directly, so install pip dependencies manually.
```
venv$ pip3 install PyGObject pycairo PyQt5
```
and then install cronotipy.
```
git clone https://github.com/jeffrichardchemistry/cronotipy
cd cronotipy
python3 setup.py install
```

# Run
To run this application type in a linux terminal:
```
$ python3 -m cronotipy
```
