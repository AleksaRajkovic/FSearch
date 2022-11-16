import re
def Format(b, factor=1024, suffix="B"):
   # """
   # Scale bytes to its proper byte format
   # e.g:
   #     1253656 => '1.20MB'
   #     1253656678 => '1.17GB'
   # """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def ToBytes(size):
    factor=1024
    mult=None
    units=['KB','MB','GB','TB']
    for i in range(len(units)):
        try:
            if(re.search(units[i],size,re.IGNORECASE)):
                mult=i
        except:
            print('Error in "ToBytes"')
    if mult is None:
        print("Error! No unit , returned 0")
        return 0
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in size)
    Numbers = [float(i) for i in newstr.split()]
    #print(mult)
    newfactor=factor
    for i in range(mult):
       newfactor*=factor
    #print(newfactor)
    bytes=Numbers[0]*newfactor
    bytes=int(bytes)
    return bytes

    
        
