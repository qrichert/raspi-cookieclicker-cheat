#!/usr/bin/env python3

# import Rpi.GPIO as GPIO
from GPIO import GPIO
import threading
import time
import os
from bcolors import bcolors


class CookieClicker:
	def __init__(self):
		self.PIN = 12
		self.MAX_CPS = int(1000 / 20 * 0.7)  # Typical relays operate in the 5 to 20 ms range. @ 70% to be conservative
		self.cps = 5.0  # default = 5 cps (clicks per second)
		self.timer_interval = 1 / self.cps

		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.PIN, GPIO.OUT, initial=GPIO.LOW)

	def loop(self):
		while True:
			# Click
			GPIO.output(self.PIN, GPIO.HIGH)
			time.sleep(self.timer_interval)

			# Delay
			GPIO.output(self.PIN, GPIO.LOW)
			time.sleep(self.timer_interval)

	def run(self):
		clickThread = threading.Thread(target=self.loop)
		clickThread.daemon = True  # Kill when main program is killed (if not, you'd have to kill it separately)
		clickThread.start()

		os.system('clear')

		while True:
			print(bcolors.BOLD + bcolors.OKBLUE + "Current CPS: {}".format(self.cps) + bcolors.ENDC)
			cps = input("New CPS? (q = quit) ")

			if cps in ['q', 'Q', 'quit', 'exit']:
				return

			os.system('clear')

			try:
				cps = float(cps)
			except ValueError:
				print(bcolors.BOLD + bcolors.FAIL + "Invalid number." + bcolors.ENDC)
				continue

			if cps > self.MAX_CPS:
				cps = self.MAX_CPS
				print(bcolors.WARNING + "CPS is limited to {}. CPS set to {}.".format(self.MAX_CPS, self.MAX_CPS) + bcolors.ENDC)

			self.cps = cps
			self.timer_interval = 1 / cps
			self.timer_interval /= 2  # HIGH and LOW have same duration each cycle


if __name__ == '__main__':
	try:
		cc = CookieClicker()
		cc.run()
	except KeyboardInterrupt:
		pass  # GPIO.cleanup()

