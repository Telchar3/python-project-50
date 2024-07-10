def generate_diff(file1, file2):
    key1 = sorted(file1.keys())
    key2 = sorted(file2.keys())
    total_key = key1 + key2
    setkey = sorted(set(total_key))
    answer = ''
    for i in setkey:
        if (i in key1 and i in key2):
            if file1[i] == file2[i]:
                answer += f'  {i}: {file1[i]}\n'
            else:
                answer += f'- {i}: {file1[i]}\n'
                answer += f'+ {i}: {file2[i]}\n'
        elif (i in key1 and i not in key2):
            answer += f'- {i}: {file1[i]}\n'
        elif (i not in key1 and i in key2):
            answer += f'+ {i}: {file2[i]}\n'
    return answer[:-1]
