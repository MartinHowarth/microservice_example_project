# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='microservice_example_project',

    version='0.0.1',

    description='Example project using the microservice framework.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/MartinHowarth/microservice_example_framework',

    # Author details
    author='Martin Howarth',
    author_email='howarth.martin@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='microservice',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'flask',
        'microservice',
    ],
)
