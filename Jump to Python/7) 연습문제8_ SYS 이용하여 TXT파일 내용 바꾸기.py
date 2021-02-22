import sys

src = sys.argv[1]
dst = sys.argv[2]

f=open(src, 'r')
lines = f.readlines()
f.close()

lines_new = []
for i in range(len(lines)) :
    line = lines[len(lines)-i-1]
    lines_new.append(line)

f= open(dst,'w')
for i in lines_new :
    f.write(i)
f.close()
