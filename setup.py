from setuptools import setup, find_packages

setup(
    name='corecli',
    version='0.0.1a1',
    url='http://github.com/werwty/corecli/',
    description='A CLI client for Core API.',
    author='',
    author_email='',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'coreapi',
        'click'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'corecli=corecli.main:client'
        ],
    },
)
