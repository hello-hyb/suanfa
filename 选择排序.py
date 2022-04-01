def select_sort():
    select_list = [10, 25, 15, 20, 13]
    length = len(select_list)
    print(f'初始列表为：{select_list}')
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if select_list[min_index] > select_list[j]:
                min_index = j
        select_list[min_index], select_list[i] = select_list[i], select_list[min_index]
        print(f'第{i+1}轮排序是：{select_list}')
    print(f'最终排好序为:{select_list}')


select_sort()
