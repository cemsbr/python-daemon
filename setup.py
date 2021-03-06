# -*- coding: utf-8 -*-

# setup.py
# Part of ‘python-daemon’, an implementation of PEP 3143.
#
# Copyright © 2008–2016 Ben Finney <ben+python@benfinney.id.au>
# Copyright © 2008 Robert Niederreiter, Jens Klein
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 3 of that license or any later version.
# No warranty expressed or implied. See the file ‘LICENSE.GPL-3’ for details.

""" Distribution setup for ‘python-daemon’ library. """

from __future__ import (absolute_import, unicode_literals)

import sys
import pydoc

from setuptools import (setup, find_packages)

import version


fromlist_expects_type = str
if sys.version_info < (3, 0):
    fromlist_expects_type = bytes


main_module_name = 'daemon'
main_module_fromlist = list(map(fromlist_expects_type, [
        '_metadata']))
main_module = __import__(
        main_module_name,
        level=0, fromlist=main_module_fromlist)
metadata = main_module._metadata

(synopsis, long_description) = pydoc.splitdoc(pydoc.getdoc(main_module))


setup(
        distclass=version.ChangelogAwareDistribution,
        name=metadata.distribution_name,
        packages=find_packages(exclude=["test"]),
        cmdclass={
            "write_version_info": version.WriteVersionInfoCommand,
            "egg_info": version.EggInfoCommand,
            },

        # Setuptools metadata.
        zip_safe=False,
        setup_requires=[
            "docutils",
            ],
        test_suite="unittest2.collector",
        tests_require=[
            "unittest2 >=0.5.1",
            "testtools",
            "testscenarios >=0.4",
            "mock >=1.3",
            "docutils",
            ],
        install_requires=[
            "setuptools",
            "docutils",
            "lockfile >=0.10",
            ],

        # PyPI metadata.
        author=metadata.author_name,
        author_email=metadata.author_email,
        description=synopsis,
        license=metadata.license,
        keywords="daemon fork unix".split(),
        url=metadata.url,
        long_description=long_description,
        classifiers=[
            # Reference: http://pypi.python.org/pypi?%3Aaction=list_classifiers
            "Development Status :: 5 - Production/Stable",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        )


# Local variables:
# coding: utf-8
# mode: python
# End:
# vim: fileencoding=utf-8 filetype=python :
