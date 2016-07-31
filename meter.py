import sys, subprocess, time
from proc import *

while True:
	subprocess.call(['clear'])
	reading = int(read_loadavg())
	print("\033[1;33m|\033[0m"*reading, "-"*(100-reading), sep='')
	time.sleep(1)
	

