#!/usr/bin/env python
"""
Created by: Michael Yanovich
With help from: Morgan Goose

Copyright 2010, Michael Yanovich and Morgan Goose
License: GNU General Public License v3, http://www.gnu.org/licenses/

DESCRIPTION: This script aims to only display items that are searched for that 
are not currently installed on the current machine. This is originally designed 
to work only on Fedora 13.
"""
import os, sys
import subprocess


def f_yum():
    '''
    This works on systems with yum installed.
    Provided by: Morgan Goose
    '''
    import yum

    yb = yum.YumBase()
    yb.setCacheDir()

    pl = yb.doPackageLists()
    installed = [x.name for x in pl.installed]
    lopi = set(installed)

    search_terms = sys.argv[1:]
    search_list = ['name', 'summary', 'description', 'packager', 'group',
            'url']

    print '%s Searching %s' % tuple(['-' * 30] * 2)
    res = yb.searchGenerator(search_list, search_terms)
    res = sorted(res, key=lambda x: x[0])

    seen = set()
    for (pkg, values) in res:
        if pkg.name not in seen and pkg.name not in installed:
            # Print name/summary
            print "%s : %s" % (pkg.name, pkg.summary)
            seen.add(pkg.name)

    print '%s COMPLETED %s' % tuple(['-' * 30] * 2)

if __name__ == '__main__':
    '''
    Steps to determine which package-management utility is installed.
    '''
    if len(sys.argv) < 2:
        print "Invalid number of parameters, please enter in the form of './server.py <search terms>'"
    else:
        p = subprocess.Popen('which yum', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
        if not " no " in p.stdout.readlines()[0]:
            f_yum()
        else:
            print "You do not have a supported package-management utility."
