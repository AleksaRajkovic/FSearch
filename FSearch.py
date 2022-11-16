
import FormatFileSize as ffs ,GetFiles as gf,select,utility,re,Add,Remove,FileManipulation as fm,os
paths=[]
filelist=[]
selectlist=[]
difflist=[]
line="-"*119
while True:
    try:
        Nslc=len(selectlist)
    except:
        Nslc=0
    try:
        Nfull=len(filelist)
    except:
        Nfull="Error !"

        Nslc="0?"
    print("Total Files : ",Nfull,"              ","Files Selected : ",Nslc)
    print(line)
    com=input(utility.ListToStr(paths)+">>")
    if (re.search('path/',com,re.IGNORECASE)):
        newpaths=select.ValPath(com)
        if newpaths!=[]:
            paths=newpaths
            filelist=gf.GetFileNames(paths)
    elif (re.search('select/',com,re.IGNORECASE)):
        selectlist=select.Select(com,filelist,selectlist)
        print(line)
    elif (re.search('add/',com,re.IGNORECASE)):
        selectlist=Add.Add(com,filelist,selectlist)
        print(line)
    elif (re.search('remove/',com,re.IGNORECASE)):
        selectlist=Remove.Remove(com,filelist,selectlist)
        print(line)
    elif (re.search('copy/',com,re.IGNORECASE)):
        selectlist=fm.Copy(com,selectlist)
        print(line)
    elif (re.search('delete/',com,re.IGNORECASE)):
        selectlist=fm.Delete(com,selectlist)
        print(line)
    elif (re.search('show:',com,re.IGNORECASE)):
        command=select.Val(com)
        if (re.search('full',command,re.IGNORECASE)):
            utility.Show(filelist)
            print(line)
        if (re.search('slc',command,re.IGNORECASE)):
            utility.Show(selectlist)
            print(line)
        if (re.search('diff',command,re.IGNORECASE)):
            difflist=utility.Diff(filelist,selectlist)
            utility.Show(difflist)
            print(line)
        if (re.search('path',command,re.IGNORECASE)):
            print(utility.ListToStr(paths))
            print(line)
        if (re.search('size',command,re.IGNORECASE)):
            if (re.search('-total',command,re.IGNORECASE)):
                utility.CalcSize(paths,filelist)
                print(line)
            if (re.search('-sl',command,re.IGNORECASE)):
                utility.CalcSize(paths,selectlist)
                print(line)
            


    

   

