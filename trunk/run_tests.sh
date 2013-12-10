#!/bin/bash

coverage run -m unittest discover -v test "*_test.py"
coverage html
