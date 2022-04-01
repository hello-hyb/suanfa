def insert_sort(array):
    print(f'最初的数组为：{array}')
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            print(f'{array}')
    print(f'最终排好序为：{array}')


insert_sort([2, 4, 6, 1, 7, 5])
