# -*- coding: utf-8 -*-

"""
	Adapted from https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
"""

from setuptools import setup


with open('README.rst', 'r') as fh:
	readme = fh.read()

setup(
	name='json_tricks',
	description='Add features to json: en/decoding of numpy arrays, preservation of ordering and ignoring of comments in input',
	long_description=readme,
	url='https://github.com/mverleg/pyjson_tricks',
	author='Mark V',
	maintainer='(the author)',
	author_email='mdilligaf@gmail.com',
	license='Revised BSD License (LICENSE.txt)',
	keywords=['json', 'numpy', 'OrderedDict', 'comments',],
	version='1.0',
	packages=['json_tricks'],
	include_package_data=True,
	zip_safe=False,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires=[
		# pytest for tests
		# sphinx for dodumentation
	],
)

