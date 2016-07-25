import sys

def main():
	if 'meminfo' in sys.argv:
		read_meminfo()

	if 'loadavg' in sys.argv:
		read_loadavg()

def read_meminfo():
	if '-b' in sys.argv:
		style = 'b'
	elif '-v' in sys.argv:
		style = 'v'
	else:
		style = input("Would you like to read meminfo as [b]asic or [v]erbose?\n").lower()

	with open('/proc/meminfo', 'r') as meminfo:
		if style == 'b':
			for i in range(0,3):
				print(meminfo.readline(), end='')

		elif style == 'v':
			for line in meminfo:
				print(line, end='')

		else:
			print("Argument not found. ")
			read_meminfo()

def read_loadavg():
	if '-b' in sys.argv:
		style = 'b'
	elif '-v' in sys.argv:
		style = 'v'
	else:
		style = input("Would you like to read loadavg as [b]asic or [v]erbose?\n").lower()

	with open('/proc/loadavg', 'r') as loadavg:
		data = loadavg.readline().split(' ')

		if style == 'b':
			print("Processor average use (last 1 minute): {:.2f}%".format(float(data[0])*100))

		elif style == 'v':
			print("Processor use (last 1 min): {}%".format(float(data[0])*100))
			print("Processor use (last 5 min): {}%".format(float(data[1])*100))
			print("Processor use (last 10 min): {}%".format(float(data[2])*100))
			print("Processes running: {}".format(data[3]))
			print("Processes total: {}".format(data[4]), end='')
		else:
			print("Argument not found. ")
			read_loadavg()

def gb_to_kb(gb):
	return "{:.0f} KB".format(float(gb)*1048576)	

def kb_to_gb(kb):
	return "{:.4f} GB".format(float(kb)/1048576)

def mb_to_gb(mb):
	return "{:.4f} GB".format(float(mb)/1024)

def gb_to_mb(gb):
	return "{:.3f} MB".format(float(gb)*1024)

if __name__ == '__main__':
	main()