from setuptools import setup
setup(
    name='hangman',
    version='0.1.0',
    packages=['hangman'],
    entry_points={
        'console_scripts': [
            'hangman = hangman.__main__:main'
        ]
    })
