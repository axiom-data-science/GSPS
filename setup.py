#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


def version():
    with open('VERSION') as f:
        return f.read().strip()


reqs = [line.strip() for line in open('requirements.txt') if not line.startswith('#')]


setup(
    name='gsps',
    version=version(),
    description='Watches a directory for new *db flight/science files and '
                'publishes the data to a ZeroMQ socket.',
    long_description=readme(),
    author='Michael Lindemuth',
    author_email='mlindemu@usf.edu',
    packages=[
        'gsps',
        'gsps.nc'
    ],
    install_requires=reqs,
    url='https://github.com/axiom-data-science/GSPS',
    entry_points = {
        'console_scripts': [
            'gsps-cli=gsps.cli:main',
            'gsps2nc=gsps.nc.cli:main'
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering'
    ],
)
