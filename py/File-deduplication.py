import pandas as pd


def deduplication(csv_1_path, csv_2_path):
    df_1 = pd.read_csv(csv_1_path)  # 读取 csv 文件，转成 DataFrame 对象
    df_2 = pd.read_csv(csv_2_path)
    df_3 = pd.concat([df_1, df_2])  # 按行合并（即上下拼接）两个 DataFrame

    # 平常我们用 pandas 做重复数据处理时，常常调用到 drop_duplicates方法来去除重。
    '''
    方法一：
    重复数据保留一个，duplicate_bool输出的是bool类型值，通过判断bool==True，取出重复行。
    '''
    duplicate_bool = df_3.duplicated(subset=['Name'], keep='first')
    repeat = df_3.loc[duplicate_bool == True]
    # pd.set_option('display.max_rows', None)  # 显示所有行
    # print(df_3)
    print(repeat)

    '''
    方法二：
    采用drop_duplicates对数据去两次重，一次将重复数据全部去除(keep=False)，
    一次将重复数据保留一个(keep=last/first)，将两个去重后的数据做差集，取出重复行。
    
    # 重复数据全部去除
    data1= df.drop_duplicates(subset=['id'], keep=False)
    data1
    
    # 重复数据保留一个
    data2=df.drop_duplicates(subset=['id'], keep='last')
    data2
    
    # 做差集，取出重复行
    repeat=data2.append(data1).drop_duplicates(keep=False)
    repeat
    '''


if __name__ == "__main__":
    # 输出两个文件中相同的行
    csv_1_path = '../data/av.csv'
    csv_2_path = '../data/av-video.csv'
    deduplication(csv_1_path, csv_2_path)
