#!/bin/bash

mv __init__.py ..
rm docs/wplotlib.rst 
rm docs/modules.rst

cd docs
make clean
sphinx-apidoc -o . ..
make html
cd ..

mv ../__init__.py .

