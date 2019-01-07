import os


def create_directories(ckpt_list):
    print("create executed")
    
    for i in range(len(ckpt_list)):
        folder = ckpt_list[i].zfill(5)
        folder = 'train/results/results-ckpt'+ str(folder)
        ckpt_folder.append(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)    
    return ckpt_folder
    print("folder creation complete")
