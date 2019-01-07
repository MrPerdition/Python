import os

def filecount(path):
    # finds all files in folder (not recursive)
    aList=[]
    for filename in os.listdir(path):
        if os.path.isdir(filename):
            pass
        else:
            aList.append(filename)
    print('number of files in folder: ', len(aList))
    return(len(aList))
