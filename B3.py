# (1) Phân tích lỗi
# Dictionary employee gồm những key nào?
# Gồm các key: "employee_id", "full_name", "department", "status"

# Vì sao dòng sau gây lỗi?
# employee_id = employee[0]
# Vì dictionary không hỗ trợ truy cập bằng index, chỉ truy cập được bằng key

# Dictionary có truy cập phần tử bằng index giống list không?
# Không. Dictionary truy cập bằng key (tên trường), không phải bằng index

# Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?
# employee_id = employee["employee_id"]

# Vì sao dòng sau gây lỗi?
# full_name = employee["name"]
# Vì key "name" không tồn tại trong dictionary, gây lỗi KeyError

# Key đúng để lấy họ tên nhân viên là gì?
# Key "full_name"

# Vì sao dòng sau chưa cập nhật đúng trạng thái nhân viên?
# employee["employee_status"] = "official"
# Vì key "employee_status" khác với key gốc "status", tạo ra key mới thay vì cập nhật key cũ

# Muốn cập nhật trạng thái nhân viên, cần dùng key nào?
# Key "status"

# Vì sao dòng sau gây lỗi?
# employee.append("base_salary", 15000000)
# Vì dictionary không có phương thức append(); append() chỉ dùng cho list

# Dictionary có phương thức append() không?
# Không

# Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?
# employee["base_salary"] = 15000000

# Vì sao dòng sau gây lỗi?
# del employee["team"]
# Vì key "team" không tồn tại trong dictionary

# Muốn xóa thông tin phòng ban, cần dùng key nào?
# Key "department"

# (2) Sửa lỗi
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")
            for i in range(len(product_list)):
                product = product_list[i]
                ma = product["product_id"]
                ten = product["product_name"]
                gia = product["price"]
                so_luong = product["quantity"]
                print(f"{i + 1}. Mã SP: {ma} | Tên: {ten} | Giá: {gia} | Số lượng: {so_luong}")
    elif choice == "2":
        print("\n--- THÊM SẢN PHẨM MỚI ---")
        ma_sp = input("Nhập mã sản phẩm: ")
        ma_sp = ma_sp.strip()
        ma_sp = ma_sp.upper()
        bi_trung = False
        for product in product_list:
            if product["product_id"] == ma_sp:
                bi_trung = True
                break

        if bi_trung:
            print("Mã sản phẩm bị trùng")
            continue
        ten_sp = input("Nhập tên sản phẩm: ")
        ten_sp = ten_sp.strip()
        gia_str = input("Nhập giá sản phẩm: ")
        if gia_str.isdigit():
            gia = int(gia_str)
        else:
            gia = -1
        so_luong_str = input("Nhập số lượng sản phẩm: ")
        if so_luong_str.isdigit():
            so_luong = int(so_luong_str)
        else:
            so_luong = -1
        if gia > 0 and so_luong > 0:
            san_pham_moi = {
                "product_id": ma_sp,
                "product_name": ten_sp,
                "price": gia,
                "quantity": so_luong
            }
            product_list.append(san_pham_moi)
            print("Thêm sản phẩm thành công")
        else:
            print("Giá/Số lượng không hợp lệ")
    elif choice == "3":
        print("\n--- CẬP NHẬT THÔNG TIN SẢN PHẨM ---")
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ")
        ma_sp = ma_sp.strip()
        ma_sp = ma_sp.upper()
        tim_thay = False
        vi_tri = -1
        for i in range(len(product_list)):
            if product_list[i]["product_id"] == ma_sp:
                tim_thay = True
                vi_tri = i
                break

        if not tim_thay:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            continue
        ten_moi = input("Nhập tên sản phẩm mới: ")
        ten_moi = ten_moi.strip()
        gia_str = input("Nhập giá sản phẩm mới: ")
        if gia_str.isdigit():
            gia_moi = int(gia_str)
        else:
            gia_moi = -1
        so_luong_str = input("Nhập số lượng sản phẩm mới: ")
        if so_luong_str.isdigit():
            so_luong_moi = int(so_luong_str)
        else:
            so_luong_moi = -1
        if gia_moi > 0 and so_luong_moi > 0:
            product_list[vi_tri]["product_name"] = ten_moi
            product_list[vi_tri]["price"] = gia_moi
            product_list[vi_tri]["quantity"] = so_luong_moi
            print("Cập nhật thành công")
        else:
            print("Giá/Số lượng không hợp lệ")
    elif choice == "4":
        print("\n--- XÓA SẢN PHẨM ---")
        ma_sp = input("Nhập mã sản phẩm cần xóa: ")
        ma_sp = ma_sp.strip()
        ma_sp = ma_sp.upper()
        tim_thay = False
        for i in range(len(product_list)):
            if product_list[i]["product_id"] == ma_sp:
                tim_thay = True
                product_list.pop(i)
                break

        if tim_thay:
            print("Xóa sản phẩm thành công")
        else:
            print("Không tìm thấy mã sản phẩm cần xoá!")
    elif choice == "5":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")