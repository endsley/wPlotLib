#!/usr/bin/env python

import os

os.system('rm -r dist/')
os.system('python setup.py sdist')
os.system('twine upload dist/*')
os.system('pip install wplotlib -U')

