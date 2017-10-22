# TDAForITD
An Implementation of the "Topological Data Analysis for Image Tampering Detection" - Approach in Python.
Originally introduced by Aras Asaad and Sabah Jassim (2017).

## Requirements
You need python3 and it's package-installer tool pip installed on your system.
If you want to use the gpu acceleration on nvdia gpu board, you also need [anaconda](https://www.anaconda.com/download/);
the numba-package (which you can install with the cmd "conda install numba"); the cudatoolkit (which you can install
with the cmd "conda install cudatoolkit").
You can download [Python 3 here](https://www.python.org/) or through your systems package manager.
We also provide a MAKEFILE to install all dependencies, run the unit-test session and the application.
It is not necessary to use this MAKEFILE but nevertheless it is much easier to do so. If you are on an modern unix-like host
the make tool should be integrated in your terminal. On Windows hosts you have to install the GNU Tools first.


## Authors
* Philip Wiegratz
* Jasper Ben Orschulko
* Jonas Hielscher
