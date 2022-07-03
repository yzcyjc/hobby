import hashlib
import os
import csv
import pandas as pd
from collections import Counter
# 计算一个文件的 MD5 值


class hash:
    def __init__(self, header, csv_path, dir_path):
        self.header = header
        self.csv_path = csv_path
        self.dir_path = dir_path
        self.Bytes = 8192

    def hash_md5(self, file_path):
        md5_1 = hashlib.md5()
        with open(file_path, 'rb') as f:   # 打开一个文件，必须是'rb'模式打开
            while 1:
                data = f.read(self.Bytes)       # 由于是一个文件，每次只读取固定字节
                if data:                   # 当读取内容不为空时对读取内容进行update
                    md5_1.update(data)
                else:                      # 当整个文件读完之后停止update
                    break
        ret_1 = md5_1.hexdigest()            # 获取这个文件的MD5值
        print(ret_1)
        self.ret_1 = ret_1
        return self.ret_1

    def hash_sha256(self, file_path):
        sha256_1 = hashlib.sha256()
        with open(file_path, 'rb') as f:   # 打开一个文件，必须是'rb'模式打开
            while 1:
                data = f.read(self.Bytes)       # 由于是一个文件，每次只读取固定字节
                if data:                   # 当读取内容不为空时对读取内容进行update
                    sha256_1.update(data)
                else:                      # 当整个文件读完之后停止update
                    break
        ret_2 = sha256_1.hexdigest()            # 获取这个文件的MD5值
        print(ret_2)
        self.ret_2 = ret_2
        return self.ret_2

    def hash_csv_write_header(self):
        with open(self.csv_path, 'w', encoding='utf-8') as f2:
            # 创建对象
            wr = csv.writer(f2)
            # 写表头
            wr.writerow(self.header)

    def hash_csv_write(self):
        FileList = os.listdir(self.dir_path)  # 获取该目录下的文件列表
        for i in FileList:
            file_path = self.dir_path + '\\'+i
            print(i)
            st = i+','+self.hash_md5(file_path)+',' + \
                self.hash_sha256(file_path)+'\n'
            with open(csv_path, 'a', encoding='utf-8') as f3:  # 追加写入文件
                f3.write(st)
            print('-'*100)

    def hash_csv_read(self):
        df = pd.read_csv(self.csv_path)
        # df[df['列名'].isin([相应的值])]   这个命令会输出等于该值的行。
        ls_1 = []
        ls_2 = []
        for item_1 in df.loc[:, 'MD5']:  # 指定列名，读取一列数据，并迭代输出
            # print(item)
            ls_1.append(item_1)
        # 统计列表中重复元素出现的次数
        result_1 = dict(Counter(ls_1))
        print([key for key, value in result_1.items() if value > 1])
        print({key: value for key, value in result_1.items() if value > 1})
        print('-----MD5-----'*10)
        for it_1 in [key for key, value in result_1.items() if value > 1]:
            print(df[df['MD5'].isin([it_1])])
        print('-'*300)
        for item_2 in df.loc[:, 'SHA-256']:  # 指定列名，读取一列数据，并迭代输出
            # print(item)
            ls_2.append(item_2)
        # 统计列表中重复元素出现的次数
        result_2 = dict(Counter(ls_2))
        print([key for key, value in result_2.items() if value > 1])
        print({key: value for key, value in result_2.items() if value > 1})
        print('-----SHA-256-----'*10)
        for it_2 in [key for key, value in result_2.items() if value > 1]:
            print(df[df['SHA-256'].isin([it_2])])


if __name__ == "__main__":
    header = ['Name', 'MD5', 'SHA-256']
    csv_path = '../data/av-video.csv'
    dir_path = 'F:/Git/hobby/video'
    p = hash(header=header, csv_path=csv_path, dir_path=dir_path)

    # 统计在输入的目录中文件的 MD5、SHA-256 值并保存在 av-video.csv 文件中
    p.hash_csv_write_header()
    p.hash_csv_write()
    p.hash_csv_read()  # 计算文件中的 MD5、SHA-256 值是否有重复