from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='cronotipy',
    version='1.0.0',
    url='https://github.com/jeffrichardchemistry/cronotipy',
    license='GNU GPL 3',
    author='Jefferson Richard',
    author_email='jrichardquimica@gmail.com',
    keywords='Chronometer Timer Scheduler PyQt5 Python3 Linux Gnome Notification',
    description='A simple customizable notification scheduler created using the python language and the pyqt5 framework for Linux systems.',
    long_description = description,
    long_description_content_type = "text/markdown",
    packages=['cronotipy'],
    include_package_data = True,
    install_requires=['PyGObject', 'pycairo' ,'PyQt5'],
	classifiers = [
		'Intended Audience :: Developers',
		'Environment :: X11 Applications :: Qt',
		'Natural Language :: English',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: Unix',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.8']
)
