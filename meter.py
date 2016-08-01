import sys, subprocess, time
from proc import *

while True:
	subprocess.call(['clear'])
	loadavg_reading = int(read_loadavg())
	loadavg_used = "\033[1;33m|\033[0m"*loadavg_reading
	loadavg_free = "-"*(100-loadavg_reading)
	print("[", loadavg_used, loadavg_free, "]\n", sep='')
	meminfo_reading = read_meminfo()
	meminfo_reading = [int(i) for i in meminfo_reading]
	meminfo_used = 100-round((meminfo_reading[2]/meminfo_reading[0])*100)
	meminfo_free = "-"*(round((meminfo_reading[2]/meminfo_reading[0])*100))
	print(meminfo_used, "%", sep='')
	print("[", "\033[1;33m|\033[0m"*meminfo_used, meminfo_free, "]", sep='')
	time.sleep(1)
	

