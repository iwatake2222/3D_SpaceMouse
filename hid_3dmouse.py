#!/usr/bin/python

# print HID value from 3D connexion space mouse (space navigator) on ubuntu
# e.g:
#  button: 0
#  Rx: 0, Ry: 0, Rz: 0
#  Tx: 0, Ty: 0, Tz: 0
# range looks -350 ~ +350
# reference: https://www.3dconnexion.com/forum/viewtopic.php?f=19&t=5642

###
# Main
###
def main():
	hid = file('/dev/hidraw6')	# need to be changed depending on environment
	print "\033[2J"		# Clear screen
	while True:
		data = ord(hid.read(1))
		if data == 3:
			button, end = tuple(ord(c) for c in hid.read(2))
			print "\033[1;0f \033[2K",	# go to line 1, and clear
			print "button: %d" % button
		if data == 2:
			rx0, rx1 = tuple(ord(c) for c in hid.read(2))
			ry0, ry1 = tuple(ord(c) for c in hid.read(2))
			rz0, rz1 = tuple(ord(c) for c in hid.read(2))
			rx = s16((rx1 << 8) + rx0)
			ry = s16((ry1 << 8) + ry0)
			rz = s16((rz1 << 8) + rz0)
			print "\033[2;0f \033[2K",	# go to line 2, and clear
			print "Rx: %d, Ry: %d, Rz: %d" % (rx, ry, rz)
		if data == 1:
			tx0, tx1 = tuple(ord(c) for c in hid.read(2))
			ty0, ty1 = tuple(ord(c) for c in hid.read(2))
			tz0, tz1 = tuple(ord(c) for c in hid.read(2))
			tx = s16((tx1 << 8) + tx0)
			ty = s16((ty1 << 8) + ty0)
			tz = s16((tz1 << 8) + tz0)
			print "\033[3;0f \033[2K",	# go to line 3, and clear
			print "Tx: %d, Ty: %d, Tz: %d" % (tx, ty, tz)

###
# Sub functions
###
def s16(value):
	return -(value & 0b1000000000000000) | (value & 0b0111111111111111)

###
# Main
###
if __name__ == "__main__":
	main()
