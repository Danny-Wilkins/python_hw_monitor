import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python proc.py [meminfo] [loadavg] [partitions] [-b] [-v]")
		sys.exit()

	if 'meminfo' in sys.argv:
		read_meminfo()

	if 'loadavg' in sys.argv:
		read_loadavg()

	if 'partitions' in sys.argv:
		read_partitions()

def read_meminfo():
	if '-v' in sys.argv:
		style = 'v'
	elif '-b' in sys.argv:
		style = 'b'
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
	if '-v' in sys.argv:
		style = 'v'
	elif '-b' in sys.argv:
		style = 'b'
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

def read_partitions():
	if '-v' in sys.argv:
		style = 'v'
	elif '-b' in sys.argv:
		style = 'b'
	else:
		style = input("Would you like to read partitions as [b]asic or [v]erbose?\n").lower()

	with open('/proc/partitions', 'r') as partitions:		
		if style == 'b':
			data = partitions.readline().split(' ')
			print('Partition', '\t\t', 'Size', '\n', end='')
			for line in partitions:
				try:
					print(line.split(' ')[-1].strip('\n'), '\t\t',\
						kb_to_gb(int(line.split(' ')[-2])))
				except:
					pass

		if style == 'v':
			print(partitions.readline(), end='')
			for line in partitions:
				print(line, end='')


def gb_to_kb(gb):
	return "{:.0f} KB".format(float(gb)*1048576)	

def kb_to_gb(kb):
	return "{:.4f} GB".format(float(kb)/1048576)

def kb_to_mb(kb):
	return "{:.2f} MB".format(float(kb)/1024)

def mb_to_kb(mb):
	return "{:.3f} KB".format(float(mb)*1024)

def mb_to_gb(mb):
	return "{:.4f} GB".format(float(mb)/1024)

def gb_to_mb(gb):
	return "{:.3f} MB".format(float(gb)*1024)

if __name__ == '__main__':
	main()