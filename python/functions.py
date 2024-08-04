import glob

def read_profile(path):
    ret = glob.glob(path+r"\*")
    for i in range(len(ret)):
        ret[i] = ret[i].split("\\")[-1].replace(".txt","")
    return ret

def read_profile_full(path):
    ret = glob.glob(path+"\*")
    return ret
