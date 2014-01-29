#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['demo_concert'],
    package_dir={'': 'src'},
    requires=['rospy', 'concert_master', 'rocon_utilities']
)

setup(**d)
