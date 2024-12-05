print ("Hà Mạnh Dũng")
print("235752021610006")
# main.py
import search_utils

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị của danh sách và đảm bảo danh sách được sắp xếp
lst = []
for _ in range(n):
    value = int(input("Nhập giá trị: "))
    lst.append(value)
lst.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Sử dụng hàm binary_search từ module search_utils
found = search_utils.binary_search(lst, value)

# In kết quả
if found:
    print(f"Phần tử {value} được tìm thấy trong danh sách.")
else:
    print(f"Phần tử {value} không được tìm thấy trong danh sách.")
