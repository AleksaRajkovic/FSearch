import re,os,shutil
def Copy(com,selectlist):
    if(re.search('copy/',com,re.IGNORECASE)): 
        split=com.split('/',1)
        com=split[1]
    else:
        print('Error ! Command not recognized !')
        return None
    if(os.path.isdir(com)):
        for file in selectlist:
            try:
                shutil.copy(file.filepath, com)
            except:
                print("Error !")
    else:
        print(com,"     is not dir !")
def Delete(com,selectlist):
    if(re.search('delete/',com,re.IGNORECASE)): 
        split=com.split('/',1)
        com=split[1]
    else:
        print('Error ! Command not recognized !')
        return None
    for file in selectlist:
        try:
            if(os.path.exists(file.filepath)):
                os.remove(file.filepath)
                if(os.path.exists(file.filepath) is False):
                    print(file.filepath,"    ==>>   Deleted")
            else:
                print("Error, file does not exist !")
        except:
            print("Error !")
def Val(com):
    try:
        x=com.split(':',1)
        return x[1]
    except:
        print("Error!")