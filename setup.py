from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quaver',
    version='0.0.1',

    description='A music composition library for Python',
    long_description=long_description,

    url='https://github.com/tedsinger/quaver',

    author='Ted Singer',
    author_email='',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='music composing chord stanza DSL',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['numpy'],

)
