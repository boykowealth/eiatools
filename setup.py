from setuptools import setup, find_packages

setup(
    name='eiatools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'pandas>=1.0',
        'numpy>=1.0'

    ],
)
