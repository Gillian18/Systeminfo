'''
Created on 19 Feb 2018

@author: gilliandonlon
'''
from setuptools import setup

setup (name = "systeminfo",
       version = "0.1",
       description = "Basic system information for COMP30670",
       url = "",
       author = "Gillian Donlon",
       author_email = " gillian.donlon@ucdconnect.ie",
       licence = "GPL3",
       packages = ['systeminfo'],
       entry_points = {
           'console_scripts' : ['comp30670_systeminfo=systeminfo.main:main']
           }
       )