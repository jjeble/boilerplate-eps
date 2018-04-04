#!/usr/bin/env python

import subprocess

# executables = ['tf03.java']
executables = []
compiler = 'javac'

for exe in executables:
	subprocess.call([compiler, exe])
