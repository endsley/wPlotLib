#!/bin/bash

rm docs/wplotlib.rst 
rm docs/modules.rst
mv __init__.py ..

cd docs
make clean
sphinx-apidoc -o . ..
make html
cd ..

mv ../__init__.py .

