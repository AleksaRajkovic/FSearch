import Standoff as std, FormatFileSize as ffs
def RemoveDupes(xlist):
    return list( dict.fromkeys(xlist))

def Show(filelist):
    length=Length(filelist)
    for file in filelist:
        print(std.NStd(file.index,15) ,str(std.Standoff(file.filepath,length)),ffs.Format(file.filesize))

def Diff(filelist,selectlist):
    for slcfile in selectlist:
        if slcfile in filelist:
            filelist.remove(slcfile)
    return filelist
def Length(list):
    l=0
    try:
        for item in list:
            if(l<len(item.filepath)):
                l=len(item.filepath)
    except:
        print("Length error !")
    return l+20

def CalcSize(paths,filelist):
    length=length=Length(paths)+12
    full=0
    i=0
    for path in paths:
        size=0
        for file in filelist:
            if path in file.filepath:
                size+=file.filesize
        print(path,"        ",ffs.Format(size))
        i+=1
        full+=size
    if i>1:
        print("Full size : ",ffs.Format(full))

def ListToStr(list):
    s=''
    for item in list:
        s=s+item+','
    return s[:-1]