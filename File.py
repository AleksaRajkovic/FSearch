import pathlib
import ntpath
class File:
    def __init__(self,filepath,filesize,index):
        self.filepath=filepath
        self.filesize=filesize
        self.index=index
        self.ext=pathlib.Path(filepath).suffix
        self.name=path_leaf(filepath)
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
