# 編號：CANDY-002
# 程式語言：Python
# 題目：請寫一小段程式，印出連續串列裡缺少的字元

chars1 = ["a", "b", "c", "d", "f", "g"]
chars2 = ["O", "Q", "R", "S"]


def missing_char(chars):
    # 實作寫在這裡
    uni_data = [ord(n) for n in chars]
    for i, e in enumerate(uni_data, start=0):
        if uni_data[i] - uni_data[i - 1] == 2:
            return chr(e - 1)


print(missing_char(chars1))
# 印出 e
print(missing_char(chars2))
# 印出 P

# 提示：
# 可使用字串的 charCodeAt 方法...
