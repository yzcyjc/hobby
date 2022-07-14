import pandas as pd
from collections import Counter


def deduplication(csv_1_path, csv_2_path):
    df_1 = pd.read_csv(csv_1_path)  # 读取 csv 文件，转成 DataFrame 对象
    df_2 = pd.read_csv(csv_2_path)
    df_3 = pd.concat([df_1, df_2])  # 按行合并（即上下拼接）两个 DataFrame
    ls_1 = []
    for item_2 in df_3.loc[:, 'SHA-256']:  # 指定列名，读取一列数据，并迭代输出
        # print(item)
        ls_1.append(item_2)
    # 统计列表中重复元素出现的次数
    result_2 = dict(Counter(ls_1))
    print([key for key, value in result_2.items() if value > 1])
    print({key: value for key, value in result_2.items() if value > 1})
    print('-----SHA-256-----'*10)
    for it_2 in [key for key, value in result_2.items() if value > 1]:
        print(df_3[df_3['SHA-256'].isin([it_2])])


if __name__ == "__main__":
    # 输出两个文件中相同的行
    csv_1_path = '../data/av.csv'
    csv_2_path = '../data/av-video.csv'
    deduplication(csv_1_path, csv_2_path)
