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
    choice = input("""\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
                        1. Hiển thị danh sách sản phẩm
                        2. Thêm sản phẩm mới
                        3. Cập nhật thông tin sản phẩm
                        4. Xóa sản phẩm theo mã
                        5. Thoát chương trình
                        
                    Nhập lựa chọn của bạn: """)
    if choice.isdigit():
        choice = int(choice)
        match choice:
            case 1:
                if not len(product_list):
                    print("Danh sách sản phẩm đang trống")
                else:
                    print("Danh sách sản phẩm hiện tại:")
                    for index, name in enumerate(product_list, start=1):
                        print(f"{index}. Mã SP: {name["product_id"]} | Tên: {name["product_name"]} | Giá: {name["price"]} | Số lượng: {name["quantity"]}")
                    
            case 2:
                flag = True
                new_id = input("Nhập mã sản phẩm: ").strip().upper()
                for item in product_list:
                    if item["product_id"] == new_id:
                        print("Sản phẩm đã tồn tại")
                        flag = False
                        
                if flag:
                    new_name = input("Hãy nhập tên sản phẩm: ")
                    while True:
                        new_price = input("Hãy nhập giá sản phẩm: ")
                        if new_price.isdigit():
                            new_price = int(new_price)
                            break
                        else:
                            print("Hãy nhập số không âm")

                    while True:
                        new_quantity = input("Hãy số lượng sản phẩm: ")
                        if new_quantity.isdigit():
                            new_quantity = int(new_quantity)
                            break
                        else:
                            print("Hãy nhập số không âm")
                    new_product = {
                        "product_id": new_id,
                        "product_name": new_name,
                        "price": new_price,
                        "quantity": new_quantity
                    }
                    product_list.append(new_product)
                    print("Thêm sản phẩm thành công")

            case 3:
                found = True
                update_id = input("Hãy nhập mã sản phẩm: ").upper().strip()
                for item in product_list:
                    if item["product_id"] == update_id:
                        found = False
                        item["product_name"] = input("Mời bạn cập nhật tên: ").strip()
                        while True:
                            new_price = input("Hãy nhập giá sản phẩm: ")
                            if new_price.isdigit():
                                new_price = int(new_price)
                                item["price"] = new_price
                                break
                            else:
                                print("Hãy nhập số không âm")
                        while True:
                            new_quantity = input("Hãy số lượng sản phẩm: ")
                            if new_quantity.isdigit():
                                new_quantity = int(new_quantity)
                                item["quantity"] = new_quantity
                                break
                            else:
                                print("Hãy nhập số không âm")
                        print("Cập nhật thành công")
                        break
                if found:
                    print("Không tìm thấy mã sản phẩm cần cập nhật")

            case 4:
                tick = True
                search_id = input("Hãy nhập mã sản phẩm bạn muốn xóa: ").strip().upper()
                for item in product_list:
                    if item["product_id"] == search_id:
                        product_list.remove(item)
                        print("Xóa thành công")
                        tick = False
                        break
                if tick:
                    print("Không tìm thấy sản phẩm muốn xóa")

            case 5:
                print("Kết thúc chương trình")
                break
            case _:
                print("Hãy nhập lựa chọn từ (1-5)")
    else:
        print("Hãy nhập số nguyên dương")