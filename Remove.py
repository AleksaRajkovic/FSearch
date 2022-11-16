import re,utility
import FormatFileSize as ffs,GetFiles as gf
def Remove(com,filelist,selectlist):
    attributes=['ext','index','min','max','ref','all']
    if(re.search('remove/',com,re.IGNORECASE)): 
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
                    filelist=RemoveExt(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='index'):
                    #print('ind')
                    filelist=RemoveIndex(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='min'):
                    #print('min')
                    filelist=RemoveMin(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='max'):
                    #print('max')
                    filelist=RemoveMax(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='ref'):
                    filelist=RemoveRef(filelist,selectlist,Val(com))
                elif(attributes[i].lower()=='all'):
                    return []
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

def RemoveExt(filelist,selectlist,extension):
    for i in range(len(filelist)):
        if filelist[i].ext==extension:
            try:
                selectlist.remove(filelist[i])
            except:
                print("Item not found ")
    return utility.RemoveDupes(selectlist)
def RemoveMin(filelist,selectlist,minsize):
    min=ffs.ToBytes(minsize)
    for file in filelist:
        if file.filesize>min:
            try:
                selectlist.remove(file)
            except:
               print("Item not found ")
    return utility.RemoveDupes(selectlist)
def RemoveMax(filelist,selectlist,maxsize):
    newlist=[]
    max=ffs.ToBytes(maxsize)
    for file in filelist:
        if file.filesize<max:
            try:
               selectlist.remove(file)
            except:
               print("Item not found ")
    return utility.RemoveDupes(selectlist)

def RemoveIndex(filelist,selectlist,indexes):
    indexlist=ValIndex(indexes)
    for index in indexlist:
        for file in filelist:
            if file.index==index:
                try:
                   selectlist.remove(file)
                except:
                   print("Item not found ")
    return utility.RemoveDupes(selectlist)
def RemoveRef(filelist,selectlist,refpath):
    reflist=gf.GetFileNames(refpath)
    for reffile in reflist:
        for file in selectlist:
            if file.name==reffile.name:
                try:
                    selectlist.remove(file)
                except:
                    print("Error ")
    return utility.RemoveDupes(selectlist)