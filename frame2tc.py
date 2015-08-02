#!/usr/bin/python

import sys

def frames2tc(count, fps):
	f = count % fps
	s = (count / fps) % 60
	m = (count / (60 * fps)) % 60
	h = (count / (3600 * fps)) % 24
		
	print "%02d:%02d:%02d:%02d" % (h, m, s, f)
 
def main():
	if len(sys.argv) < 3:
		print 'usage: frame2tc frame# fps'
		sys.exit(1)
	count = int(sys.argv[1])
	fps = int(sys.argv[2])
	frames2tc(count, fps)
	

if __name__ == '__main__':
	main()