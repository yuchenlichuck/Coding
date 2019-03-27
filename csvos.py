import csv
import shutil
import os
filename = 'H:\\kaggle\\trainLabels.csv'

arr=[]

def mkdir(path):
    '''
    创建不存在的文件夹
    '''
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False
i=0
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        i=i+1
        if i==1:
            continue
        if len(row)!=0:
            arr.append(row)
            print(i)
    file_name_list = [row[0] for row in arr]
    label = [row[1] for row in arr] 
local_img_dir='H:\\kaggle\\train'
save_dir='H:\\data'
for i in range(len(file_name_list)):
    img_file_path = local_img_dir + '\\' + file_name_list[i]+'.jpeg'
    img_save_path = save_dir + '\\'+ label[i]
    mkdir(img_save_path)
    shutil.copy(img_file_path,img_save_path+ '\\' + file_name_list[i]+'.jpeg')
