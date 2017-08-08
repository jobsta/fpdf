#!/usr/bin/env python
# Always prefer setuptools over distutils
from setuptools import setup
from codecs import open
from os import path
from fpdf import __version__

package_dir = 'fpdf'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == '__main__':
    setup(name='reportbro-fpdf',
          version=__version__,
          description='Simple PDF generation for Python',
          long_description=long_description,
          author='Olivier PLATHEY ported by Max',
          author_email='maxpat78@yahoo.it',
          maintainer="Alex Hartmann",
          maintainer_email="alex@reportbro.com",
          url='https://www.reportbro.com',
          license='LGPLv3+',
          packages=['fpdf', ],
          package_dir={'fpdf': package_dir},
          package_data={'fpdf': ['font/*.ttf', 'font/*.txt']},
          install_requires=[
              'Pillow>=4',
              'six'
          ],
          classifiers=[
              "Development Status :: 5 - Production/Stable",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
              "Programming Language :: Python",
              "Programming Language :: Python :: 2.7",
              "Programming Language :: Python :: 3.5",
              "Programming Language :: Python :: 3.6",
              "Operating System :: OS Independent",
              "Topic :: Software Development :: Libraries :: PHP Classes",
              "Topic :: Software Development :: Libraries :: Python Modules",
              "Topic :: Multimedia :: Graphics",
          ],
          keywords=["pdf", "unicode", "png", "jpg", "ttf"],
          )
