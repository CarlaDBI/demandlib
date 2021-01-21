#! /usr/bin/env python

"""Setup information of demandlib.
"""

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='demandlib',
      version='0.1.7dev',
      author='oemof developer group',
      url='https://oemof.org/',
      license='GPL3',
      author_email='contact@oemof.org',
      description='Demandlib of the open energy modelling framework',
      long_description=read('README.rst'),
      packages=find_packages(),
      install_requires=['pandas >= 1.0',
                        'numpy >= 1.7.0'],
      package_data={
          'demandlib': [os.path.join('bdew_data', '*.csv')],
          'demandlib.examples': ['*.csv']},
      )
