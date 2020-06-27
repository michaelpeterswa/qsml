#!/bin/bash
pip3 install -r requirements.txt
nose2 --plugin nose2.plugins.junitxml --junit-xml tests
