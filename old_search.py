#!/usr/bin/python
"""
Created by: Michael Yanovich
With help from: Morgan Goose

Copyright 2010, Michael Yanovich and Morgan Goose
License: GNU General Public License v3, http://www.gnu.org/licenses/

DESCRIPTION: This script aims to only display items that are searched for that are not currently installed on the current machine. This is originally designed to work only on Fedora 13.
"""

import sys, subprocess

p = subprocess.Popen('yum list installed', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

lopi = [ x.split()[0] for x in p.stdout.readlines() ]

search = "yum search %s" % (" ".join(sys.argv[1:]))

q = subprocess.Popen(search, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for item in q.stdout.readlines():
    installed_item = item[:-1].split(' : ')[0]
    if installed_item not in lopi:
        print item[:-1]
