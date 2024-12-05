print ("Hà Mạnh Dũng")
print("235752021610006")
# main.py
import search_utils

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị của danh sách
dlist = []
for _ in range(n):
    value = int(input("Nhập giá trị: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Sử dụng hàm Sequential_Search từ module search_utils
found, index = search_utils.Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {index}.")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
