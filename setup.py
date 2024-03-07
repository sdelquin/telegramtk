from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()
requirements = ['requests']

setup(
    name='tgutils',
    version='0.0.3',
    url='https://github.com/sdelquin/tgutils.git',
    author='Sergio Delgado Quintero',
    author_email='sdelquin@gmail.com',
    description='Telegram utilities',
    license='MIT',
    packages=['tgutils'],
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
