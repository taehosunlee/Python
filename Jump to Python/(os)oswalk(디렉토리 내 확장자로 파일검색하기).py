import os



#디렉토리 내 .py 파일 모두 찾기.
#제 1 방법##

def search(dirname) :
    try :
        filenames=os.listdir(dirname)
        for filename in filenames :
            full_filename = os.path.join(dirname,filename)

            if os.path.isdir(full_filename) :
                search(full_filename)
            else :
                ext=os.path.splitext(full_filename)[-1]
                if ext=='.py' :
                    print(full_filename)
    except PermissionError :
        pass


search("c:\\")




#제 2 방법

for (path,dir,files) in os.walk("c:\\") :
    for filename in files :
        ext= os.path.splitext(filename)[-1]
        if ext=='.py' :
            print("%s/%s" %(path,filename))
            
