import setuptools
import pathlib


setuptools.setup(
    name='cloudpath',
    version='0.1.0',
    description="Extend pathlib to GCS, S3, HDFS via TensorFlow's GFile.",
    url='http://github.com/danijar/cloudpath',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['cloudpath'],
    install_requires=['tensorflow'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
