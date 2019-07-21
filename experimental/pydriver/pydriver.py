#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coyright (C) 2019 Niels Joubert
# Contact: Niels Joubert <njoubert@gmail.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
"""

"""
############################
# Python 2to3 Compatibility
############################
from __future__ import print_function

############################
# Python System Packages
############################
import os
import sys
import glob
import math
import cmath
import time
import datetime
import re
import itertools
import functools
import random
import pickle
import json
import csv
import urllib
import requests
import argparse
import socket


import numpy as np
import matplotlib.pyplot as plt

IP = '10.1.32.130'
PORT = 2111
PASS = "client"

BUFFER_SIZE = 4096

[b'sRA', b'LMDscandata', b'1', b'1', b'AB3495', b'0', b'0', b'4CE1', b'DB', b'5CCAA5BC', b'5CCAB4B8', b'0', b'0', b'4', b'0', b'0', b'9C4', 
b'168', b'0', b'2', b'DIST1', b'3F800000', b'00000000', b'0', b'9C4', b'2D1', b'62', b'6E', b'6E', b'67', b'64', b'68', b'68', 
b'67', b'61', b'73', b'5D', b'6F', b'6A', b'70', b'6D', b'60', b'76', b'73', b'6A', b'7A', b'74', b'7E', b'69', b'7E', b'6D', b'77', b'7A', b'7E', b'68', b'75', b'80', b'78', b'80', b'7D', b'7B', b'7E', b'7C', b'80', b'7A', b'80', b'6B', b'70', b'89', b'82', b'7F', b'79', b'88', b'85', b'78', b'90', b'86', b'87', b'8A', b'84', b'7F', b'8B', b'8B', b'9D', b'9D', b'93', b'A5', b'A8', b'AE', b'AF', b'A5', b'AB', b'A4', b'A3', b'9D', b'AA', b'A0', b'B5', b'AF', b'B7', b'B0', b'A8', b'AD', b'B3', b'AD', b'B5', b'98', b'99', b'A0', b'A7', b'AF', b'B1', b'A6', b'B3', b'B0', b'A5', b'9D', b'9C', b'9B', b'88', b'97', b'90', b'95', b'95', b'8D', b'91', b'93', b'92', b'83', b'85', b'8C', b'87', b'83', b'86', b'73', b'83', b'6E', b'7A', b'67', b'78', b'7C', b'7F', b'72', b'7A', b'7F', b'86', b'79', b'78', b'72', b'70', b'70', b'79', b'66', b'78', b'6C', b'76', b'67', b'62', b'8A', b'85', b'78', b'7B', b'7D', b'88', b'94', b'90', b'81', b'8F', b'7D', b'92', b'92', b'9F', b'99', b'A2', b'9A', b'AA', b'BA', b'B6', b'A1', b'AF', b'A9', b'9A', b'B2', b'BE', b'B9', b'C7', b'A9', b'C6', b'D0', b'E3', b'D5', b'DD', b'DF', b'E5', b'EB', b'E3', b'EF', b'EE', b'E9', b'EE', b'DE', b'106', b'EC', b'103', b'FE', b'F5', b'F6', b'104', b'107', b'11A', b'108', b'11D', b'11E', b'129', b'127', b'139', b'13F', b'14C', b'151', b'15D', b'154', b'160', b'162', b'16F', b'167', b'17A', b'167', b'175', b'174', b'17D', b'173', b'177', b'17D', b'17E', b'185', b'187', b'18F', b'195', b'17D', b'192', b'187', b'191', b'17C', b'18E', b'185', b'191', b'187', b'190', b'197', b'19A', b'19A', b'191', b'190', b'19C', b'195', b'187', b'18C', b'198', b'1A4', b'196', b'19F', b'1A7', b'198', b'19F', b'19A', b'1A3', b'19C', b'1A3', b'1A7', b'19F', b'196', b'199', b'1A5', b'1A0', b'1A5', b'1A2', b'1A3', b'1A4', b'1A3', b'1AD', b'19A', b'1A0', b'195', b'18A', b'151', b'136', b'F8', b'ED', b'BE', b'A2', b'85', b'7B', b'73', b'84', b'A1', b'CE', b'EB', b'119', b'139', b'17D', b'1A0', b'1BF', b'1BF', b'1C7', b'1B6', b'1C6', b'1C4', b'1C4', b'1C6', b'1CB', b'1C8', b'1C6', b'1C4', b'1D0', b'1D4', b'1D8', b'1CE', b'1D8', b'1D4', b'1D5', b'1DE', b'1E0', b'1DB', b'1E9', b'1DE', b'1DE', b'1E4', b'1E8', b'1ED', b'1E6', b'1EC', b'1F0', b'1E9', b'1F2', b'1F9', b'1F5', b'1F2', b'1F1', b'1F5', b'203', b'202', b'202', b'1F9', b'202', b'207', b'206', b'20A', b'20B', b'201', b'210', b'216', b'215', b'21A', b'21F', b'219', b'215', b'226', b'225', b'220', b'229', b'224', b'237', b'232', b'240', b'241', b'249', b'234', b'24B', b'245', b'258', b'243', b'24D', b'255', b'25E', b'258', b'25C', b'265', b'270', b'26A', b'26E', b'271', b'272', b'268', b'275', b'27D', b'280', b'289', b'287', b'297', b'293', b'294', b'2A7', b'2A3', b'2A6', b'2A2', b'2B5', b'2C4', b'2C7', b'2C7', b'2DB', b'2C4', b'2DA', b'2D8', b'2E5', b'2E3', b'2EC', b'2E6', b'2EA', b'309', b'302', b'2FE', b'31B', b'302', b'329', b'328', b'330', b'320', b'34A', b'341', b'361', b'34D', b'35A', b'359', b'369', b'36D', b'380', b'380', b'389', b'383', b'396', b'3A9', b'3B6', b'3AF', b'3C7', b'3BD', b'3D4', b'3D5', b'3E7', b'3D1', b'3D9', b'3A8', b'380', b'340', b'340', b'325', b'325', b'326', b'32D', b'329', b'32D', b'32F', b'32B', b'34B', b'39C', b'3B6', b'3BB', b'3A7', b'3A8', b'3A4', b'3A9', b'3A6', b'3B0', b'398', b'39E', b'38C', b'393', b'386', b'353', b'2FB', b'273', b'22B', b'1E9', b'1C8', b'1B8', b'19E', b'1AA', b'19E', b'19C', b'19C', b'1A7', b'19F', b'1AA', b'1A3', b'19A', b'1A6', b'1A6', b'195', b'1AE', b'1A7', b'1A7', b'1A1', b'1AB', b'1AC', b'1B1', b'19F', b'1A5', b'1A9', b'1AA', b'1B2', b'1B8', b'19F', b'1AE', b'1A0', b'1B1', b'1B4', b'1BB', b'1B2', b'1B8', b'1BD', b'1C2', b'1CA', b'1C8', b'1AF', b'1B0', b'1BB', b'1BB', b'1D3', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'1AE', b'185', b'196', b'190', b'187', b'182', b'191', b'17B', b'18F', b'18B', b'196', b'193', b'197', b'186', b'18B', b'18E', b'194', b'1E9', b'265', b'2B2', b'2F5', b'317', b'334', b'324', b'31F', b'321', b'326', b'31E', b'31E', b'30E', b'316', b'311', b'32F', b'32B', b'319', b'0', b'0', b'0', b'2EB', b'2FE', b'300', b'30A', b'31D', b'307', b'31E', b'2FE', b'303', b'31F', b'32B', b'327', b'332', b'32A', b'32E', b'32B', b'32A', b'32C', b'331', b'33F', b'347', b'342', b'33B', b'336', b'345', b'341', b'33E', b'32E', b'33E', b'342', b'354', b'345', b'34D', b'345', b'347', b'342', b'347', b'344', b'341', b'33F', b'353', b'348', b'352', b'34D', b'35B', b'34E', b'363', b'35A', b'35B', b'351', b'35F', b'33E', b'34D', b'333', b'32A', b'311', b'30D', b'31F', b'338', b'337', b'35D', b'35C', b'370', b'35D', b'367', b'37E', b'378', b'369', b'37E', b'37A', b'37A', b'380', b'385', b'379', b'38E', b'372', b'389', b'390', b'38F', b'371', b'393', b'384', b'39A', b'392', b'3A3', b'39E', b'39A', b'3A6', b'3A6', b'3A6', b'3AC', b'3A6', b'3B8', b'3A0', b'3B8', b'3B3', b'3BB', b'3B7', b'3C9', b'3AB', b'3BB', b'3CA', b'3D6', b'3BB', b'3D1', b'3D0', b'3CF', b'3D2', b'3DF', b'3D1', b'3D9', b'3D2', b'3CE', b'3E1', b'3D8', b'3E0', b'3DD', b'3DC', b'3EA', b'3F5', b'3F8', b'3EF', b'3F9', b'407', b'3F3', b'3FE', b'40D', b'412', b'40B', b'411', b'41F', b'412', b'3EE', b'3E5', b'401', b'3F4', b'404', b'425', b'RSSI1', b'3F800000', b'00000000', b'0', b'9C4', b'2D1', b'214', b'215', b'212', b'214', b'213', b'212', b'210', b'20F', b'20D', b'20E', b'20E', b'20B', b'20A', b'209', b'208', b'20A', b'207', b'209', b'207', b'207', b'207', b'208', b'20B', b'20A', b'20E', b'20B', b'20C', b'20A', b'210', b'211', b'20E', b'210', b'212', b'212', b'216', b'218', b'21B', b'21B', b'21C', b'21F', b'21F', b'21B', b'216', b'219', b'216', b'217', b'214', b'213', b'212', b'20A', b'20A', b'209', b'205', b'205', b'203', b'201', b'1FD', b'1F8', b'1F8', b'1F8', b'1F3', b'1F6', b'1F4', b'1FA', b'206', b'214', b'227', b'237', b'240', b'240', b'23E', b'23A', b'234', b'22D', b'229', b'234', b'23D', b'24A', b'256', b'258', b'250', b'23E', b'221', b'20B', b'1F4', b'1E5', b'1DC', b'1D2', b'1CC', b'1CB', b'1CB', b'1C8', b'1C9', b'1CA', b'1CB', b'1CC', b'1CD', b'1CE', b'1CD', b'1CF', b'1CE', b'1D1', b'1D3', b'1D5', b'1D4', b'1D5', b'1D6', b'1D7', b'1D8', b'1D8', b'1DA', b'1D8', b'1DB', b'1D9', b'1D9', b'1DA', b'1DA', b'1DB', b'1D9', b'1D8', b'1DB', b'1DA', b'1DB', b'1D9', b'1D8', b'1D6', b'1D8', b'1D5', b'1D7', b'1D6', b'1D7', b'1D8', b'1D6', b'1D9', b'1D8', b'1D9', b'1D9', b'1D7', b'1D6', b'1D6', b'1D7', b'1D6', b'1D9', b'1D5', b'1D7', b'1D5', b'1D7', b'1D7', b'1DB', b'1E1', b'1DC', b'1D3', b'1CE', b'1CA', b'1CF', b'1D4', b'1D2', b'1D4', b'1D5', b'1D5', b'1D8', b'1D4', b'1D2', b'1CE', b'1D2', b'1D1', b'1D1', b'1D1', b'1D1', b'1D2', b'1D1', b'1D0', b'1D0', b'1CE', b'1D0', b'1CA', b'1C9', b'1C8', b'1C5', b'1C2', b'1C2', b'1BB', b'1B9', b'1B2', b'1AF', b'1AC', b'1AA', b'1AB', b'1AF', b'1AD', b'1B1', b'1B8', b'1C0', b'1C8', b'1D0', b'1DA', b'1E1', b'1E9', b'1F4', b'1FA', b'202', b'204', b'206', b'205', b'204', b'208', b'207', b'208', b'203', b'201', b'1FC', b'1F7', b'1F9', b'1F8', b'1F6', b'1F4', b'1F6', b'1F2', b'1F1', b'1EE', b'1EB', b'1EA', b'1EB', b'1E9', b'1E9', b'1EC', b'1E9', b'1E9', b'1E9', b'1EC', b'1EA', b'1EA', b'1E7', b'1E8', b'1E9', b'1E6', b'1E5', b'1E9', b'1E9', b'1E8', b'1E8', b'1EB', b'1E8', b'1E9', b'1EA', b'1E6', b'1E5', b'1E1', b'1DD', b'1DE', b'1DB', b'1D7', b'1D8', b'1D4', b'1D3', b'1D0', b'1CB', b'1CA', b'1CD', b'1CB', b'1D0', b'1CA', b'1C1', b'1B7', b'1AE', b'1AD', b'1B4', b'1BC', b'1C4', b'1CA', b'1CD', b'1CC', b'1CD', b'1C7', b'1C4', b'1C8', b'1CA', b'1D0', b'1D6', b'1DA', b'1DE', b'1E1', b'1E6', b'1EB', b'1EF', b'1EF', b'1F0', b'1F3', b'1F3', b'1F4', b'1F5', b'1F6', b'1F5', b'1F8', b'1F5', b'1F9', b'1FB', b'1FA', b'1F9', b'1FC', b'1FE', b'1FE', b'1FF', b'201', b'200', b'203', b'202', b'205', b'204', b'203', b'207', b'208', b'209', b'20A', b'20D', b'20D', b'20D', b'210', b'211', b'210', b'210', b'211', b'212', b'214', b'217', b'217', b'21B', b'21A', b'21D', b'21D', b'220', b'220', b'223', b'21F', b'223', b'225', b'229', b'229', b'22C', b'22B', b'22D', b'22D', b'22E', b'231', b'233', b'231', b'234', b'22E', b'21D', b'20A', b'1FF', b'204', b'225', b'23B', b'23C', b'23D', b'23E', b'23E', b'243', b'243', b'245', b'245', b'246', b'246', b'246', b'249', b'24C', b'24B', b'24C', b'24E', b'251', b'251', b'254', b'252', b'255', b'255', b'259', b'25A', b'25A', b'25B', b'25A', b'25B', b'25C', b'25B', b'25F', b'25E', b'262', b'263', b'266', b'265', b'265', b'266', b'266', b'268', b'26A', b'26B', b'26C', b'26C', b'26D', b'26F', b'26F', b'26D', b'271', b'272', b'271', b'273', b'273', b'275', b'277', b'27A', b'284', b'28E', b'298', b'288', b'26E', b'225', b'1E3', b'1EF', b'1FC', b'202', b'206', b'203', b'203', b'1FD', b'1F8', b'1EB', b'1FD', b'249', b'272', b'28B', b'292', b'294', b'293', b'290', b'290', b'290', b'292', b'292', b'28C', b'27F', b'271', b'24B', b'1FB', b'173', b'181', b'1A1', b'1B9', b'1CE', b'1DD', b'1E6', b'1E9', b'1E9', b'1EB', b'1EA', b'1EA', b'1E6', b'1E4', b'1E4', b'1E5', b'1E4', b'1E6', b'1E1', b'1E4', b'1E3', b'1E6', b'1E6', b'1E7', b'1E5', b'1E8', b'1E9', b'1E8', b'1E9', b'1E7', b'1E4', b'1E7', b'1E3', b'1DB', b'1D3', b'1C9', b'1C0', b'1B3', b'1A7', b'197', b'183', b'16A', b'140', b'107', b'E4', b'D3', b'B8', b'AC', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'0', b'B9', b'132', b'16C', b'186', b'190', b'190', b'18D', b'18D', b'18B', b'188', b'186', b'188', b'187', b'185', b'184', b'183', b'17F', b'1AA', b'1FF', b'229', b'239', b'240', b'248', b'256', b'260', b'25C', b'250', b'244', b'231', b'21D', b'200', b'1E3', b'1B6', b'182', b'12C', b'0', b'0', b'0', b'119', b'160', b'18B', b'1AB', b'1BC', b'1CE', b'1C3', b'1C4', b'1C5', b'1DD', b'1E9', b'1F2', b'1FD', b'204', b'20A', b'20D', b'211', b'211', b'1D9', b'1C9', b'1F9', b'20A', b'21B', b'22A', b'230', b'233', b'236', b'238', b'23A', b'240', b'242', b'249', b'249', b'24C', b'24D', b'250', b'256', b'258', b'25D', b'267', b'269', b'265', b'263', b'261', b'25B', b'25B', b'259', b'25D', b'25F', b'260', b'25A', b'24B', b'239', b'223', b'207', b'206', b'1FB', b'1FD', b'218', b'1F9', b'1EE', b'1D7', b'21D', b'24C', b'261', b'26E', b'270', b'271', b'271', b'270', b'270', b'272', b'272', b'270', b'26E', b'271', b'26E', b'26E', b'26E', b'26F', b'26F', b'271', b'26F', b'270', b'270', b'26D', b'26C', b'26F', b'26D', b'270', b'26F', b'273', b'272', b'274', b'272', b'271', b'26E', b'26E', b'26C', b'270', b'271', b'26F', b'263', b'23E', b'23B', b'24A', b'264', b'274', b'271', b'264', b'240', b'240', b'251', b'26C', b'271', b'26B', b'26D', b'26B', b'26C', b'270', b'26D', b'26E', b'26B', b'26B', b'26A', b'26B', b'268', b'268', b'268', b'268', b'264', b'261', b'257', b'251', b'24B', b'24B', b'249', b'247', b'0', b'0', b'0', b'0', b'1', b'7E3', b'6', b'2', b'0', b'6', b'23', b'55F00', b'0']


def decode(frame):
	frame = frame.strip(b"\x02\x03").split(b" ")
	print(frame)
	assert(frame[1] == b'LMDscandata')
	assert(frame[2] == b'1')
	serial = frame[4]
	assert(frame[5] == b'0')
	assert(frame[6] == b'0')
	freq = int(frame[16],16)
	print("Frequency:", freq/100.0, "Hz")
	channels = int(frame[19],16)
	print("Channels:", channels)
	assert(channels == 2)
	content = str(frame[20], 'ascii')
	print("Content of first channel:", content)
	scalefactor = frame[21]
	assert(scalefactor == b'3F800000')
	scalefactoroffset = frame[22]
	assert(scalefactoroffset == b'00000000')
	startangle = int(frame[23],16)/10000.0
	stepsize = int(frame[24],16)/10000.0
	amount = int(frame[25],16)
	print("From", startangle,"deg in steps of",stepsize,"deg for",amount,"points")
	channel1 = frame[26:26+amount]
	distances = [int(d,16)/1000.0 for d in channel1]
	left = frame[26+amount::]
	return distances

def setup_and_read():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		s.connect((IP, PORT))

		# Log in. 4.1 p12
		MESSAGE = b"\2sMN SetAccessMode 03 F4724744\3" 
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		data = s.recv(BUFFER_SIZE)

		# Set timestamp/data angle. 3.3.1 p86
		MESSAGE = b"\2sMN LSPsetdatetime " + bytes(datetime.datetime.now().strftime('+%Y +%m +%d +%H +%M +%S +%f'),"utf8") + b"\3"
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		data = s.recv(BUFFER_SIZE)

		# Start measurement
		MESSAGE = b"\02sMN LMCstartmeas\03"
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		data = s.recv(BUFFER_SIZE)

		# Log out. 4.2.12 p56
		MESSAGE = b"\2sMN Run\3"
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		data = s.recv(BUFFER_SIZE)


		# Request Last Scan
		MESSAGE = b"\02sRN LMDscandata\03"
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		frame = b""
		while True:
			data = s.recv(BUFFER_SIZE)
			frame += data
			if data[-1:] == b"\x03":
				break
	finally:
		s.close()

	return frame

def read():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		s.connect((IP, PORT))

		# Request Last Scan
		MESSAGE = b"\02sRN LMDscandata\03"
		sent = s.send(MESSAGE)
		assert(sent == len(MESSAGE))
		frame = b""
		while True:
			data = s.recv(BUFFER_SIZE)
			frame += data
			if data[-1:] == b"\x03":
				break
	finally:
		s.close()

	return frame	

frame = setup_and_read()

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='polar')

r = np.linspace(2, 0, 361)
theta = 0.5 * np.pi * r


distances = np.zeros(361)
li, = ax.plot(theta, distances, linewidth=0, marker=".")
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi)

ax.set_rmax(5)
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')

#ax.relim() 
#ax.autoscale_view(True,True,True)
fig.canvas.draw()
plt.ion()
plt.show()

while True:

	try:
		frame = read()
		distances = decode(frame)
		print("Distances decoded:", len(distances))

		#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
		#ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
		li.set_ydata(distances[0:361])		
		fig.canvas.draw()

		#plt.show()
	except AssertionError:
		print ("Assertion woopsies")

	plt.pause(0.001)
	time.sleep(0.1)




