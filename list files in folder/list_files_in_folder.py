def image_list(path):
    # finds all files in folder (not recursive)
    imgList=[]
    for filename in os.listdir(path):
        if os.path.isdir(filename):
            pass
        else:
            imgList.append(filename)
    return(imgList)
