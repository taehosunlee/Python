import os

for (path,dir,files) in os.walk("C:\") :
                                for file_name in files :
                                ext=os.path.splitext(filename)[-1]
                                if ext==".py" :
                                print("%s/%s" %(path,filename))
