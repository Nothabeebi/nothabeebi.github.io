from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dcode/__init__.py
from dcode import __version__ as version

setup(
	name="dcode",
	version=version,
	description="Theme",
	author="Habeeb Abdullah",
	author_email="habeeb@zoserp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
