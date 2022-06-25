import os


def test(dirname, qz):
    """

    """
    FileList = os.listdir(dirname)  # 获取该目录下的文件列表
    nums = 1  # 构造递增的初始变量
    for FileName in FileList:
        hz = os.path.splitext(FileName)[-1]  # 获取文件后缀名
        newname = '{}{}{}'.format(qz, nums, hz)  # 构造新文件名（即重命名后的文件名）
        nums += 1
        os.rename('{}/{}'.format(dirname, FileName),
                  '{}/{}'.format(dirname, newname))  # 文件重命名
        print('{}===正在修改文件名===》{}'.format(FileName, newname))
    print('批量文件重命名完成，总共个重命名了 {} 个文件'.format(nums-1))


if __name__ == "__main__":
    dirname = input('请输入要批量修改文件名的目录路径：')  # 要修改文件名的目录的路径
    qz = input('请设定修改后的文件名的前缀：') + '_'        # 设定修改后的文件名前缀字符串
    test(dirname, qz)
