if __name__ == '__main__':
    list1 = []
    records = []
    sample_list = []
    j_var = 0

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append(([name, score]))
    records.sort()

    for [i, j] in records:
        list1.append(j)

    records_temp = records.copy()
    temp_list1 = list1.copy()

    for [i, j] in records:
        if j == min(list1):
            sample_list += [i,j]
            j_var = j
            records_temp.remove([i,j])
            temp_list1.remove(j)

    records = records_temp
    list1 = temp_list1

    for [i, j] in records:
        if j == min(list1):
            print(i)



