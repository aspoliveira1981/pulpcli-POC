from setuptools import setup, find_packages

setup(
    name="pulpcli",
    version="0.0.1a1",
    url="http://github.com/werwty/pulpcli/",
    description="POC CLI for Pulp",
    author="werwty",
    author_email="bihan.zh@gmail.com",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        "click",
        "click_completion",
        "psutil",
        "progress",
        "pygments",
        "pyswagger",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["pulp=pulpcli.main:client"]},
)
