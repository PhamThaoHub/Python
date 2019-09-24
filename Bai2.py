with open('../input/input1.txt', 'r') as f:
    lists = set()
    for l in f.readlines():
        lists.extend(l.strip().split())
    print(lists)
    print('Number of words:', len(lists))
