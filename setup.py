# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='djconf',
      version=version,
      description="djconf",
      long_description="""djconf""",
      classifiers=filter(None, map(str.strip, """\
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Programming Language :: Python
""".splitlines())),
      keywords='',
      author='Hunza, Inc.',
      author_email='info@hunza.jp',
      url='https://github.com/csakatoku/djconf',
      license='MIT License',
      platforms=['any'],
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'djconf-generate = djconf.commands:generate',
          ]
      })
