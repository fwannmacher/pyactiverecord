#!/bin/bash

coverage run -m unittest discover -v test "*_test_case.py"
coverage html
