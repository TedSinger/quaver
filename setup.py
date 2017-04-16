from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='muse',
    version='0.0.1',

    description='A music composition DSL for Python',
    long_description=long_description,

    url='https://github.com/tedsinger/muse',

    author='Ted Singer',
    author_email='',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='music composing chord stanza DSL',

    packages=['muse'],

    install_requires=['numpy'],

)