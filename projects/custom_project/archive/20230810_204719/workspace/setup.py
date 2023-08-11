from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "calculator = main:main",
        ],
    },
    install_requires=[],
    tests_require=["pytest"],
)
