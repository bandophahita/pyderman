import os
from pyderman import install, all_drivers
import subprocess
import unittest


class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		for driver in all_drivers:
			print("Testing %s..." % driver.__name__)
			data = install(browser=driver, verbose=True, chmod=True, overwrite=True, return_info=True)
			path = data['path']
			if not os.path.exists(path):
				raise FileNotFoundError('The %s executable was not properly downloaded.' % driver.__name__)
			output = subprocess.check_output([path, '--version']).decode('utf-8')
			print('Version:', output)
			self.assertIn(data['version'], output.lower(), "Driver %s did not output proper version! ('%s')" % (driver.__name__, data['version']))
			print('%s is installed at: "%s"' % (data['driver'], path))
			print('\n\n\n')


if __name__ == "__main__":
	unittest.main()


"""
TODO:
	https://github.com/operasoftware/operachromiumdriver/releases
	http://phantomjs.org/download.html
		https://bitbucket.org/ariya/phantomjs/downloads/?tab=downloads
		https://api.bitbucket.org/2.0/repositories/ariya/phantomjs/downloads/
"""