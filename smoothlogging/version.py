import os

VERSION = '0.1.%s' % os.environ.get('TRAVIS_BUILD_NUMBER', 2)
print("version is: %s" % VERSION)
