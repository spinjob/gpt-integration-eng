from setuptools import setup, find_packages

setup(
    name='string-reverser',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'string-reverser=main:main',
        ],
    },
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
