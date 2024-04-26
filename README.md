# WordPress Security Helper

Friendly helper tool to extract intesresting information from a WordPress plugin source code

## Pre-Work:

This script is based on the previous works of WpBullet, by OWASP.

## Setup

Create a python venv
```bash
python3 -m venv venv
```

Activate it
```bash
source venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

## Usage

```python
python3 wpsechelper.py -h
```

```
usage: wpsechelper.py [-h] [-p PATH] [--version]

WPSecHelper - Find WordPress plugins security issues faster

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to plugin to analyze
  --version             Show version number
```