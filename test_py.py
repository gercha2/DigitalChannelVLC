import pyb

for c in range(100):
	pyb.LED(4).toggle()
	pyb.delay(50)
	pyb.LED(4).toggle()
	pyb.delay(50)
print('Hello world')
