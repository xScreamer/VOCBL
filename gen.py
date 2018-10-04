#/usr/lib/python
#kirnath x zerobyte
import random
import string
base = "BLMOIV"
berapa = int(raw_input("Butuh Berapa Boss?: "))
def gene(size=4, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
for i in range(berapa):
	print base+gene()
