from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cellulant/__init__.py
from cellulant import __version__ as version

setup(
	name="cellulant",
	version=version,
	description="payment app ",
	author="simon muturi ",
	author_email="simomutu8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
