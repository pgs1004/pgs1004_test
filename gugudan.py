
array = [ [ 0 for i in xrange(9) ] for j in xrange(9) ]
n = 21
x, y = 0, 0
v = 1, 0
array[y][x] = n
while 1:
    x, y = x+v[0] , y+v[1]
    if x < 0 or x > 8 or y < 0 or y > 7 or array[y][x] != 0:
        x, y = x-v[0] , y-v[1]
        v = -v[1], v[0] # velocity vector +90 degree rotation
        x, y = x+v[0] , y+v[1]
    if n%10 == 9:
    	n+=2
    else :
 		n+=1

    array[y][x] = n
    if n == 99:
        break

for y in xrange(8):
    for x in xrange(9):
    	a = array[y][x]/10
    	b = array[y][x]%10
    	c = a*b
        print "%2d "%  c,
    print

print "====="
for y in xrange(8):
    for x in xrange(9):
    	a = array[y][x]/10
    	b = array[y][x]%10
    	c = a*b
        print "%2d "%  array[y][x],
    print
