import sys
import time

for line in sys.stdin:
	print line.swapcase().rstrip()
	time.sleep(3)
