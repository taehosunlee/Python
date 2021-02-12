#memo

import sys

option= sys.argv[1]
contents = sys.argv[2:]

# -a 를 하면 쓰고
# -v 를 하면 읽게끔 하고싶다.

if option == "-a" :
    with open("C:\doit\memo.txt", 'a') as f :
        f.write(str(contents))
        f.write("\n")

elif option == "-v" :
    with open("C:\doit\memo.txt", 'r') as f :
        
        print(f.read())

else : print("잘못 입력하셨습니다")
