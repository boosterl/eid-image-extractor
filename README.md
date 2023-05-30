# eid-image-extractor

## Introduction

This is a small python script to extract the image from a Belgian electronic
identity card.

## How to install

All the Python dependencies this script has are declared in the
`requirements.txt`-file. The script can be ran in a `venv`:
```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```

## How to use

After you installed the dependencies, you can just run the script inside the
`venv`:
```
python3 eid-image-extractor.py
```
After this, if everything went well, you will see a file with the name
```{NATIONAL_NUMBER}.jpeg``` next to the script.
