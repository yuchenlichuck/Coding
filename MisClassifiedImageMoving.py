# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:54:12 2019

@author: PC
"""

import csv
import shutil
import os

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

def ReadMisFile(path):
    '''
    生成文件名列表
    :return:
    '''
    local_file_name_list = path
    arr = []
    i=0
    csv_reader = csv.reader(open(local_file_name_list, encoding='utf-8'))
    for row in csv_reader:
        if len(row)!= 0:
            arr.append(row)
            i=i+1
            print(i)
    org_lable = [row[0] for row in arr]
    file_name_list = [row[1] for row in arr]
    pred_lable = [row[2] for row in arr]
    return org_lable, file_name_list, pred_lable

def copy_img():
    '''
    复制、重命名、粘贴文件
    '''
    # 设置目录

    local_img_dir = r'G:\now\all\train'
    # 训练集文件路径，local_img_dir + 原始标签 + 文件名 = 错误分类文件路径
    CSV_file_path = 'E:\\mis_training\\new.csv'  # CSV文件路径

    save_dir = 'G:\\mis_training\\mis\\'  # 错误影像另存的文件夹路径

    org_lable, file_name_list, pred_lable = ReadMisFile(CSV_file_path)
    for i in range(len(file_name_list)):
        img_file_path = local_img_dir + '\\' +  org_lable[i] +'\\'+ file_name_list[i]
        img_save_path = save_dir #+ '\\'+ org_lable[i] +'\\'+ pred_lable[i]
        mkdir(img_save_path)
        shutil.move(img_file_path,img_save_path+ '\\' + file_name_list[i])

if __name__ == '__main__':
    copy_img()