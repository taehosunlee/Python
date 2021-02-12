# tab을 스페이스 4개로 바꾸기.

import sys

src = sys.argv[1]
dst = sys.argv[2]


f=open(src,'r')
tab_sub=f.read()
f.close()

space4=tab_sub.replace("\t", " "*4)

print(space4)


f=open(dst,'w')
f.write(space4)
f.close()

