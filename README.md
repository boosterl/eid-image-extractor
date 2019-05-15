# eid-image-extractor
## Introduction
This is a small python script to extract the image from a Belgian electronic identity card.

## How to install
Before running this script you will need a few dependencies, notably, python 3, pip3 and the python module [eidreader](https://github.com/lino-framework/eidreader).

To install eidreader you will also need to have ```swig``` installed. On an Arch system, the installation looks like this:
```
sudo pacman -S python3 swig
sudo pip install eidreader
```

## How to use
After you installed the dependencies, you can just run the script:
```
python3 eid-image-extractor.py
```
After this, if everything went well, you will see a file with the name ```{NATIONAL_NUMBER}.jpeg``` next to the script.
