"""
Brings colors to the console.
See:
- https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
- https://stackoverflow.com/a/287944
"""


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.BOLD = ''
		self.UNDERLINE = ''
		self.ENDC = ''


if __name__ == '__main__':
	print(bcolors.OKGREEN + 'hello, world!' + bcolors.ENDC)
