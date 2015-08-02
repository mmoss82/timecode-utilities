#!/usr/bin/python

import sys, re

def tc2count(tc, fps):
	tc_match = re.match('(\d{2}):(\d{2}):(\d{2})[:,;](\d{2})', tc)
	h = int(tc_match.group(1))
	m = int(tc_match.group(2))
	s = int(tc_match.group(3))
	f = int(tc_match.group(4))

	print int(f) + int(fps)*(s + 60*(m + h*60))

def main():
	if len(sys.argv) < 3:
		print 'usage: tc2frame timecode fps'
		sys.exit(1)
	tc = (sys.argv[1])
	fps = int(sys.argv[2])
	tc2count(tc, fps)
	

if __name__ == '__main__':
	main()