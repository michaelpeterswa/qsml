#!/bin/bash

build () {
    sudo rm -rf dist/
    python3 setup.py sdist bdist_wheel
    twine upload dist/*
}

echo "Did you update the version number? (y/n): "
read ans
if [ $ans = "y" ]
then
    echo "Starting up build.sh"
    build
elif [ $ans = "n" ]
then
    echo "Exiting..."
else
    echo "Not a valid answer"
fi

