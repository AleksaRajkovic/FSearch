import re
import numpy as np
#import Cipher_LIb as cl


def IndexSearch(msg=list,searchval=str):
     indexList = (np.where(np.array(msg) == searchval)[0].tolist())
     for i in range(len(indexList)):
         indexList[i]=int(indexList[i])
     return indexList




def CharSplit(msg=str):
    return re.findall('.',msg)

def FourSplit(msg=str):
    return re.findall('....',msg)

def TwelveSplit(msg=str):
    return re.findall('............',msg)

def ListToStr(msg=list):
    str1=''
    for x in range(len(msg)):
        str1+=(str(msg[x])+",")
    return str1
def ListToStrNC(msg=list):
    str1=''
    for x in range(len(msg)):
        str1+=str(msg[x])
    return str1