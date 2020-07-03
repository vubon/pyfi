import os
import re

from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version(package: str) -> str:
    with open(os.path.join(BASE_DIR, f'{package}/__version__.py')) as version:
        version = version.readline()
    match = re.search("__version__ = ['\"]([^'\"]+)['\"]", version)
    assert match is not None
    return match.group(1)


def get_log_description():
    with open('README.md') as readme:
        with open('CHANGELOG.md') as changelog:
            return readme.read() + "\n\n" + changelog.read()


setup(
    name='PyFileSender',
    version=get_version('PyFileSender'),
    author='Vubon Roy',
    author_email='vubon.roy@gmail.com',
    description='This package will help to send file into mobile or other computer',
    url='https://github.com/vubon/pyfi',
    project_urls={
        "Documentation": "https://github.com/vubon/pyfi/blob/master/docs/GUIDE.md"
    },
    packages=find_packages(),
    long_description=get_log_description(),
    long_description_content_type="text/markdown",
    license='MIT',
    platforms='Python',
    install_requires=[
        'qrcode',
        'psutil',
        'pyinstaller',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',  # 2 - Pre-Alpha, 3 - Alpha, 4 - Beta, 5 - Production/Stable
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: FileShare",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ]
)
