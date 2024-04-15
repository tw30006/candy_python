# 編號：CANDY-001
# 程式語言：Python
# 題目：找出串列裡最小的兩個值的總和
# 例如：
#   [15, 28, 4, 2, 43] 印出 6
#   [23, 71, 33, 82, 1] 印出 24

def sum_of_smallest_values(arr) :
  # 實作程式碼寫在這裡
    sort_nums=sorted(arr)
    return (sort_nums[0]+sort_nums[1])
    

nums1= [19, 5, 42, 2, 77]
nums2 = [23, 15, 59, 4, 17]
print(sum_of_smallest_values(nums1)); # 印出 7
print(sum_of_smallest_values(nums2)); # 印出 19