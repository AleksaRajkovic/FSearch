import re,utility
import FormatFileSize as ffs,GetFiles as gf,os
def Select(com,filelist,selectlist):
    attributes=['ext','index','min','max','ref','all']
    if(re.search('select/',com,re.IGNORECASE)): 
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
                    filelist=SelectExt(filelist,Val(com))
                elif(attributes[i].lower()=='index'):
                    #print('ind')
                    filelist=SelectIndex(filelist,Val(com))
                elif(attributes[i].lower()=='min'):
                    #print('min')
                    filelist=SelectMin(filelist,Val(com))
                elif(attributes[i].lower()=='max'):
                    #print('max')
                    filelist=SelectMax(filelist,Val(com))
                elif(attributes[i].lower()=='ref'):
                    filelist=SelectRef(filelist,Val(com))
                elif(attributes[i].lower()=='all'):
                    return filelist
    return filelist
def Val(com):
    try:
        x=com.split(':',1)
        return x[1]
    except:
        print("Error!")
    
def ValPath(com):
    paths=[]
    try:
        x=com.split('/',1)[1]
        try:
            x=x.split(',')
            for path in x:
                if os.path.isdir(path):
                    paths.append(path)
                else:
                    print("Error invalid path !")
            return utility.RemoveDupes(paths)
        except:
            print("Error!")
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


def SelectExt(filelist,extension):
    newlist=[]
    for i in range(len(filelist)):
        if filelist[i].ext==extension:
            try:
                newlist.append(filelist[i])
            except:
                print("Error ")
    return newlist
def SelectMin(filelist,minsize):
    newlist=[]
    min=ffs.ToBytes(minsize)
    for file in filelist:
        if file.filesize>min:
            try:
                newlist.append(file)
            except:
                print("Error ")
    return newlist
def SelectMax(filelist,maxsize):
    newlist=[]
    max=ffs.ToBytes(maxsize)
    for file in filelist:
        if file.filesize<max:
            try:
                newlist.append(file)
            except:
                print("Error ")
    return newlist

def SelectIndex(filelist,indexes):
    newlist=[]
    indexlist=ValIndex(indexes)
    for index in indexlist:
        for file in filelist:
            if file.index==index:
                try:
                    newlist.append(file)
                except:
                    print("Error ")
    return utility.RemoveDupes(newlist)
def SelectRef(filelist,refpath):
    print("ref : ", refpath)
    reflist=gf.GetFileNames(refpath)
    newlist=[]
    for reffile in reflist:
        for file in filelist:
            if file.name==reffile.name:
                try:
                    newlist.append(file)
                except:
                    print("Error ")
    return utility.RemoveDupes(newlist)




