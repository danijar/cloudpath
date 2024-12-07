import pathlib
import re
import setuptools


def parse_requirements(filename):
  requirements = pathlib.Path(filename)
  requirements = requirements.read_text().split('\n')
  requirements = [x for x in requirements if x.strip()]
  return requirements


setuptools.setup(
    name='cloudpath',
    version='0.2.0',
    description='Optimized pathlib backend for Google Cloud',
    url='http://github.com/danijar/cloudpath',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['cloudpath'],
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
