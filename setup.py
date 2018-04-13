# installation: pip install boto3-utils
from setuptools import (
  setup,
  find_packages,
)

# read requirements.txt for requires, filter comments and newlines.
sanitize = lambda x : not x.startswith('#') and not x.startswith('\n')
with open('requirements.txt', 'r') as f:
    requires = filter(sanitize, f.readlines())

setup( 
    name = 'boto3-utils',
    version = '0.0.1',
    description = 'boto3-utils: The missing boto3 Utilities.',
    keywords = 'boto3 utilities aws infrastructure',
    long_description = open('README.rst').read(),

    author = 'Russell Ballestrini',
    author_email = 'russell@ballestrini.net',
    url = 'https://github.com/russellballestrini/boto3-utils',

    license = 'BSD 2-Clause "Simplified" License',

    packages = find_packages(),

    install_requires = requires,
   
    classifiers=[
        'Intended Audience :: Developers, Operators, System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

"""
setup()
  keyword args: http://peak.telecommunity.com/DevCenter/setuptools
configure pypi username and password in ~/.pypirc::
 [pypi]
 username:
 password:
build and upload to pypi with this::
 python setup.py sdist bdist_egg register upload
"""
