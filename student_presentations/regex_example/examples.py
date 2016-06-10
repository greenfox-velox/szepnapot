import re

# Avg of 'X-DSPAM-Confidence: 0.6178'
pattern_dspam = re.compile(r'^X-DSPAM-Confidence:\s(\d+.*)')

# h/m/s timestamps 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pattern_receive_hours = re.compile(r'^From\s.+@.+\s[A-za-z]{3}\s+\d\s+(\d+:\d+:\d+)')

with open('mbox-short.txt') as f:
	# pure text
	# for line in f:
	# 	print(line)

	# DSPAM-s
	# for line in f:
	# 	line = line.rstrip()
	# 	spam_number = re.findall(pattern_dspam, line)
	# 	if spam_number:
	# 		print(spam_number)
	# 	continue


	# """From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
	# Return-Path: <postmaster@collab.sakaiproject.org>
	# Received: from murder (mail.umich.edu [141.211.14.90])
	# 	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	# 	 Sat, 05 Jan 2008 09:14:16 -0500"""

	# and just the hour/minute/second timestamp!

	# for line in f:
	# 	line = line.rstrip()
	# 	time = re.findall(pattern_receive_hours, line)
	# 	if time:
	# 		print(time)
	# 	continue
