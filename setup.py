#!/usr/bin/env python
# Always prefer setuptools over distutils
from setuptools import setup
import re

package_dir = 'fpdf'

def read(path):
    """Read a file's contents."""
    with open(path, 'r') as f:
        return f.read()

version = re.findall(r"Version:\s*(\d+.\d+.\d+)", read('./fpdf/fpdf.py'))[0]

if __name__ == '__main__':
    setup(name='reportbro-fpdf',
          version=version,
          description='Simple PDF generation for Python',
          long_description=read('./README.rst'),
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
