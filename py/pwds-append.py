class dic:
    def __init__(self, t):
        self.t = t
        self.s = 0

    def dic_read(self):
        if self == '':
            s = 1
            self.s = s
            return self.s
        else:
            f = open('../data/pwds.txt', mode='r',
                     encoding='utf-8')  # 以只读方式打开文件。文件的指针将会放在文件的开头。
            num = 1
            for line in f:
                if line.replace('\n', '') == self.t:
                    print('{}  找到了,在第 {} 行'.format(self.t, num))
                    s = 2
                    self.s = s
                num += 1
            print('密码总数：{} 个'.format(num-1))
            print('='*100)
            self.num = num
            f.close()
            return self.s, self.num

    def dic_write(self):
        '''
        mode='a'
        打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
        也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        '''
        if self.s == 0:
            f2 = open('./data/pwds.txt',
                      mode='a', encoding='utf-8')
            print('{} 找不到===》追加写入文件中===》写入成功，现在密码总个数为 {} 个'.format(self.t, self.num))
            print('+'*100)
            f2.write('{}\n'.format(self.t))
            f2.close()


if __name__ == "__main__":
    while True:
        t = input('请输入字符串，进行密码查找：')
        d = dic(t)
        d.dic_read()
        d.dic_write()
