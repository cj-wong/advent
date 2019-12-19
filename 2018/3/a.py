import sys

try:
	with open(sys.argv[1], 'r') as f:
		a = f.read()
except:
	sys.exit('Could not read file')

a = a.strip().split('\n')

fabric = [[0 for x in range(1000)] for y in range(1000)]

for _a in a:
	_a = _a.split()
	_a.remove('@')
	x, y = _a[1].rstrip(':').split(',')
	x = int(x) - 1
	y = int(y) - 1
	w, h = _a[-1].split('x')
	w = int(w)
	h = int(h)
	for _h in range(h):
		for _w in range(w):
			fabric[y+_h][x+_w] += 1

_fabric = [__f for _f in fabric for __f in _f]
print(len([_f for _f in _fabric if (_f > 1)]))