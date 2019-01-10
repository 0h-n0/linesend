import os
import re
import setuptools
from pathlib import Path

p = Path(__file__)

version = "1.0.2"

setup_requires = [
    'requests',
]
install_requires = [
    'requests',    
]
test_require = [
    '',
    '',
    ''
]

setuptools.setup(
    name="linesend",
    version=version,
    python_requires='>3.6',    
    author="Koji Ono",
    author_email="koji.ono@exwzd.com",
    description=".",
    url='https://github.com/0h-n0/linesend',
    long_description=(p.parent / 'README.md').open(encoding='utf-8').read(),
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=test_require,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts' : ['linesend = linesend:commandline'],
    },
)
