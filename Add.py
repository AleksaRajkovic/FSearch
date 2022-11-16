import re,utility
import FormatFileSize as ffs,GetFiles as gf
def Add(com,filelist,selectlist):
    attributes=['ext','index','min','max','ref','all']
    if(re.search('add/',com,re.IGNORECASE)): 
        split=com.split('/',1)
        com=split[1]
    else:
        print('Error ! Command not recognized !')
        return None
    commands=com.split('&')
    for com in commands:
        for i in range(len(attributes)):
            if(re.search(attributes[i],com,re.IGNORECASE)):
                if(attributes[i].lower()=='ext'):
                    #print('ext')
                    filelist=AddExt(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='index'):
                    #print('ind')
                    filelist=AddIndex(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='min'):
                    #print('min')
                    filelist=AddMin(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='max'):
                    #print('max')
                    filelist=AddMax(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='ref'):
                    filelist=AddRef(filelist,selectlist,Val(com))
    return filelist
def Val(com):
    try:
        x=com.split(':',1)
        return x[1]
    except:
        print("Error!")
    
def ValPath(com):
    try:
        x=com.split('/',1)
        return x[1]
    except:
        print("Error!")
def ValIndex(indexes):
    intlist=[]
    try:
        #print(indexes)
        indexlist=indexes.split(',')
        #print(indexlist)
        for i in indexlist:
            try:
                intlist.append(int(i))
            except:
                print("Error! Conversion impossible!")
        return intlist
    except:
        print("Error!")    

def AddExt(filelist,selectlist,extension):
    for i in range(len(filelist)):
        if filelist[i].ext==extension:
            try:
                selectlist.append(filelist[i])
            except:
                print("Error ")
    return utility.RemoveDupes(selectlist)
def AddMin(filelist,selectlist,minsize):
    min=ffs.ToBytes(minsize)
    for file in filelist:
        if file.filesize>min:
            try:
                selectlist.append(file)
            except:
               print("Error ")
    return utility.RemoveDupes(selectlist)
def AddMax(filelist,selectlist,maxsize):
    newlist=[]
    max=ffs.ToBytes(maxsize)
    for file in filelist:
        if file.filesize<max:
            try:
                selectlist.append(file)
            except:
                print("Error ")
    return utility.RemoveDupes(selectlist)

def AddIndex(filelist,selectlist,indexes):
    indexlist=ValIndex(indexes)
    for index in indexlist:
        for file in filelist:
            if file.index==index:
                try:
                    selectlist.append(file)
                except:
                    print("Error ")
    return utility.RemoveDupes(selectlist)
def AddRef(filelist,selectlist,refpath):
    reflist=gf.GetFileNames(refpath)
    for reffile in reflist:
        for file in filelist:
            if file.name==reffile.name:
                try:
                    selectlist.append(file)
                except:
                    print("Error ")
    return utility.RemoveDupes(selectlist)