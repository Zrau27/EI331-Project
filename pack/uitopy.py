import os

"""
ui文件批量转py文件
对单个文件可根据
"cmd = "pyuic5 -o func2_1.py func2_1.ui""
直接在cmd执行
"""

def uitopy(orpa,tapa):
    pathDir =  os.listdir(orpa)  # 获取文件夹下的所有的文件

    for ffn in pathDir:
        fname,ext = os.path.splitext(ffn)
        orfl = orpa+"\\"+fname+".ui"          #原文件
        tgfl = tapa+"\\"+fname+".py"          #生成目标文件
        try:
            cmd = "pyuic5 -o {} {}".format(tgfl,orfl) 
            os.system(cmd)
            print(orfl+" finished")
        except Exception as e:
            print(e)



originpath = r"D:\sigtem\ui_v3"             #ui文件所在根目录,需要仅包含ui文件
targetpath = "D:\sigtem\py"              #生成的py文件根目录

uitopy(originpath,targetpath)
