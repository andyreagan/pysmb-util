#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from pathlib import Path, PurePath

from setuptools import find_packages, setup

from src import pysmb_util


def read(*names, **kwargs):
    with Path(PurePath.joinpath(Path(__file__).parent, *names)).open(
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='pysmb-util',
    version=pysmb_util.__version__,
    license='MIT',
    description='Helper functions for working with SMB via pysmb.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Andy Reagan',
    author_email='andy@andyreagan.com',
    url='https://github.com/andyreagan/pysmb-util',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[PurePath(path).name.suffix[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/andyreagan/pysmb-util/issues',
    },
    keywords=[],
    python_requires='>=3.5',
    install_requires=["pysmb == 1.1.28"],
    extras_require={},
)
