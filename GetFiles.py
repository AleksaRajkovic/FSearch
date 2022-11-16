import os,GetFileSize as gfs,File as f
def GetFileNames(paths):
    i=0
    fileList=[]
    for p in paths:
        for path, dirs, files in os.walk(p, topdown=True):
            for name in files:
                filepath=os.path.join(path, name)
                file=f.File(filepath,gfs.GetSize(filepath),i)
                fileList.append(file)
                i+=1
    return fileList