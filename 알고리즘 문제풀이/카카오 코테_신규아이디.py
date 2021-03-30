new_id=input()

new_id=list(new_id)
leng=len(new_id)
for i in range (leng) :
    if new_id[i].isupper :
        new_id[i]=new_id[i].lower()

new_id=''.join(new_id)

import re

p=re.compile(r"\w|-|_|[.]")
m=p.findall(new_id)

new_id=''.join(m)

p1=re.compile("[.]+")
new_id=p1.sub(".",new_id)

p2=re.compile('^[.]')
p3=re.compile('[.]$')
new_id=p2.sub("",new_id)
new_id=p3.sub("",new_id)

if new_id=="" :
    new_id="a"

lea=len(new_id)

if lea>15 :
    new_id=new_id[0:15]
    new_id=p3.sub("",new_id)

if lea<3 :
    k=new_id[lea-1]
    new_id=new_id+(k*(3-lea))

print(new_id)