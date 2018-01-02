[![Build Status](https://travis-ci.org/Jiaxigu/sleepsort.svg?branch=master)](https://travis-ci.org/Jiaxigu/sleepsort)


# sleepsort

Python implementation of sleepsort.

Mainly serves as a minimal template of distributable Python package.

## Install

	>>> python setup.py install

## Test

	>>> python test.py -v
	
## Use

Sometimes it works

	>>> sleepsort([2, 1, 3], interval=0.1)
	<<< [1, 2, 3]
	
And sometimes it doesn't...

	>>> sleepsort([6, 5, 2, 1, 4, 3, 9, 7, 8], interval=0.001)
	<<< [1, 2, 3, 4, 5, 7, 6, 8, 9]
	
## Reference

- More on sleepsort: [https://www.quora.com/What-is-sleep-sort](https://www.quora.com/What-is-sleep-sort)
- More on python package template: [https://github.com/kennethreitz/samplemod](https://github.com/kennethreitz/samplemod)