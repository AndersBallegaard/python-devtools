#!/bin/bash

#build the package
python3 setup.py sdist

#install localy
pip3 install .

#run tests
python3 tests/run.py

#upload to pypi if user wants it
echo Should this be released to pypi?[y/n]
read upload_ans
if [ $upload_ans == "y" ]
then
    twine upload dist/*
    rm -r dist
fi