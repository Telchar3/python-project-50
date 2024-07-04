def generate_diff(file1, file2):
    key1 = sorted(file1.keys())
    key2 = sorted(file2.keys())
    total_key = key1 + key2
    setkey = sorted(set(total_key))
    result = {}
    print(setkey)
    for i in setkey:
        if (i in key1 and i in key2):
            if file1[i] == file2[i]:
                print(1)
                result.update({i: file1[i]})
            else:
                print(2)
                result.update({i: file1[i]})
                result.update({i: file2[i]})
        elif (i in key1 and i not in key2):
            result.update({i: file1[i]})
            print(3)
        elif (i not in key1 and i in key2):
            print(4)
            result.update({i: file2[i]})
