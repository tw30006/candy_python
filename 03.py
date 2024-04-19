# 編號：CANDY-003
# 程式語言：Python
# 題目：完成函數的內容，把陣列裡的 0 都移到最後面

list = [False, 1, 0, -1, 2, 0, 1, 3, "a"]


def move_zeros_to_end(arr):
    # 程式碼寫在這裡
    zero_list = [n for n in arr if n is 0]
    other_list = [i for i in arr if i is not 0]
    return other_list + zero_list


result = move_zeros_to_end(list)
print(result)
# 印出 [false, 1, -1, 2, 1, 3, "a", 0, 0]
