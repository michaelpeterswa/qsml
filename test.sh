#!/bin/bash
apt-get install python3-pip
pip3 install -r requirements.txt
nose2 --plugin nose2.plugins.junitxml --junit-xml tests
