from collections import Counter


def tests():
    ls = []
    ls2 = []
    with open('../data/fiction.txt', 'r', encoding='utf-8') as f:
        for line in f:
            a = line.replace('\n', '')
            # print(a.split('|'))
            ls.append(a.split('|'))
    for i in ls:
        ls2.append(i[1])
    result = dict(Counter(ls2))
    print(result)
    print([key for key, value in result.items() if value > 1])
    print({key: value for key, value in result.items() if value > 1})
    # ls3 = set(ls2)
    # print(len(ls2))
    # print(len(ls3))


if __name__ == "__main__":
    tests()
