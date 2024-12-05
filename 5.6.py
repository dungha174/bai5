print ("Hà Mạnh Dũng")
print("235752021610006")
# main.py
import list_utils

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị của danh sách
lst = []
for _ in range(n):
    value = int(input("Nhập giá trị: "))
    lst.append(value)

# Sử dụng các hàm từ module list_utils
sorted_list = list_utils.sort_list(lst)
max_value = list_utils.find_max(lst)
min_value = list_utils.find_min(lst)

# In kết quả
print("Danh sách sau khi sắp xếp: ", sorted_list)
print("Phần tử lớn nhất: ", max_value)
print("Phần tử nhỏ nhất: ", min_value)


