"""
Placeholder for Rpi.GPIO to test on regular computer
"""


class GPIO:
	BOARD = 'board'
	BCM = 'broadcom'
	IN = 'input'
	OUT = 'output'
	HIGH = True
	LOW = False

	@staticmethod
	def setmode(_):
		pass

	@staticmethod
	def setwarnings(_):
		pass

	@staticmethod
	def setup(_, __, initial):
		pass

	@staticmethod
	def input(_):
		pass

	@staticmethod
	def output(_, state):
		# print('HIGH' if state else 'LOW')
		pass

	@staticmethod
	def cleanup():
		pass
