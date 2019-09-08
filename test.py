import os
path = "pretrained_models/karras2018iclr-lsun-churchoutdoor-256x256.pkl"
print(os.path.exists(path))

with open("samples/requirements-pip.txt", "r") as f:    #打开文件
    data = f.read()   #读取文件
    print(data)

