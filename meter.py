import sys, subprocess, time
from proc import *

while True:
	subprocess.call(['clear'])
	loadavg_reading = int(read_loadavg())
	print("[", "\033[1;33m|\033[0m"*loadavg_reading, "-"*(100-loadavg_reading), "]\n", sep='')
	meminfo_reading = read_meminfo()
	meminfo_reading = [int(i) for i in meminfo_reading]
	print(100-round((meminfo_reading[1]/meminfo_reading[0])*100), "%", sep='')
	print("[", "\033[1;33m|\033[0m"*(100-round((meminfo_reading[1]/meminfo_reading[0])*100)), \
		"-"*(round((meminfo_reading[1]/meminfo_reading[0])*100)), "]", sep='')
	time.sleep(1)
	

