#!/bin/bash

nosetests -v --with-coverage --cover-erase --cover-package=active_record --cover-html
