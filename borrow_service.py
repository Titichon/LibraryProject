from data_handler import save_books, save_borrow_records

#ฟังก์ชันยืมหนังสือ
def borrow_book(list_book, borrow_records, name):
    print("\n--- ยืมหนังสือ ---")
    print("กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก")
    book_id = input("กรอก book_id: ").strip()
    # ท่านผู้ใช้กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก
    if book_id == "exit":
        return

    # ตรวจสอบว่าผู้ใช้กรอก book_id หรือไม่
    if not book_id:
        print("\n<<< กรุณากรอก book_id >>>")
        return

    # ค้นหาหนังสือที่มี book_id ตรงกับที่ผู้ใช้กรอก
    selected_book = None
    for book in list_book:
        if book["book_id"] == book_id:
            selected_book = book #เจอแล้ว เอาข้อมูลหนังสือใส่ลงแทนที่ None
            break

    # ตรวจสอบว่ามีหนังสือที่เลือกหรือไม่
    if selected_book is None:
        print("\n<<< ไม่พบหนังสือเล่มนี้ในระบบ >>>")
        return
    if selected_book["available_copies"] <= 0: # เช็คว่ามีเล่มที่สามารถยืมได้หรือไม่ ไม่มีก็แจ้งเตือนว่าหมด
        print("หนังสือเล่มนี้ถูกยืมหมดแล้ว")
        return

    # คำสั่งกรอกจำนวนเล่มที่ต้องการยืม
    while True:
        try:
            borrow_copies = int(input("กรอกจำนวนเล่มที่ต้องการยืม: ").strip())
            # ตรวจสอบว่าจำนวนที่กรอกต้องมากกว่า 0
            if borrow_copies <= 0:
                print("\n<<< จำนวนหนังสือที่ต้องการยืมต้องมากกว่า 0 >>>")
                continue
            # ตรวจสอบว่าจำนวนที่ยืมไม่เกินจำนวนที่มีอยู่
            if borrow_copies > selected_book["available_copies"]:
                print(f"\n<<< จำนวนหนังสือที่ต้องการยืมเกินจำนวนที่มีอยู่ >>>")
                print(f"จำนวนหนังสือที่มีอยู่: {selected_book['available_copies']}")
                continue

            break # ออกจากลูปถ้ากรอกจำนวนเล่มที่ต้องการยืมถูกต้อง

        except ValueError:
            print("\n<<< กรุณากรอกตัวเลข >>>")

    # ลดจำนวนเล่มที่ยืมออกจาก available_copies ของหนังสือ
    selected_book["available_copies"] -= borrow_copies
    # บันทึกข้อมูลการยืมหนังสือลงใน borrow_records
    borrow_records.append({
        "name": name,
        "book_id": selected_book["book_id"],
        "book_name": selected_book["book_name"],
        "borrow_copies": borrow_copies,
        "status": "borrowed",
    })
    save_borrow_records(borrow_records) # บันทึกข้อมูลการยืมหนังสือลงใน borrow_records
    save_books(list_book) # บันทึกข้อมูลหนังสือหลังจากยืมหนังสือแล้ว
    
    # แสดงผลการยืมหนังสือ
    print("\n<<< สถานะการยืม >>>")
    print(f"\nผู้ใช้ {name}")
    print(f"ยืม {selected_book['book_name']} สำเร็จ")
    print(f"ผู้แต่ง {selected_book['book_author']}")
    print(f"จำนวนหนังสือที่คงเหลือ: {selected_book['available_copies']}")
    print(f"จำนวนหนังสือที่ยืม: {borrow_copies}")
    print("\n<<< ยืมหนังสือเรียบร้อยแล้ว >>>")

#ฟังก์ชันคืนหนังสือ
def return_book(list_book, borrow_records, name):
    print("\n--- คืนหนังสือ ---")
    print("กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก")
    book_id = input("กรอก book_id: ").strip()
    # ท่านผู้ใช้กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก
    if book_id == "exit":
        return

    # เก็บทุกรายการของผู้ใช้คนนี้ที่ยังยืมหนังสือรหัสเดียวกันอยู่ เช่น ยืมครั้งแรก 2 เล่ม ครั้งที่สอง 1 เล่ม จะได้รายการยืมทั้งหมด 3 เล่ม
    active_records = []
    for record in borrow_records:
        if (
            record["book_id"] == book_id
            and record["name"] == name
            and record["status"] == "borrowed"
        ):
            active_records.append(record)

    #เช่น ถ้าไม่มีรายการยืมที่ยังไม่ได้คืน จะไม่สามารถคืนได้ เช่น ยืมไปแล้วคืนหมดแล้ว หรือ ไม่เคยยืมเลย ก็จะคืนไม่ได้
    if not active_records:
        print("ไม่พบรายการยืมที่ยังไม่ได้คืน")
        return

    # รวมจำนวนที่ยังยืมทั้งหมด และ .get("borrow_copies", 1) คือ ส่วนนี้รองรับข้อมูลเก่าที่บันทึกก่อนเพิ่มฟีเจอร์จำนวนเล่ม ให้มันถือว่ายืม 1 เล่ม
    total_borrowed = sum(record.get("borrow_copies", 1) for record in active_records)
    # คำสั่งกรอกจำนวนเล่มที่ต้องการคืน
    while True:
        try:
            return_copies = int(input("กรอกจำนวนเล่มที่ต้องการคืน: ").strip())
        except ValueError:
            print("\n<<< กรุณากรอกตัวเลข >>>")
            continue
        # ตรวจสอบว่าจำนวนที่กรอกต้องมากกว่า 0
        if return_copies <= 0:
            print("\n<<< จำนวนหนังสือที่ต้องการคืนต้องมากกว่า 0 >>>")
            continue
        # ตรวจสอบว่าจำนวนที่คืนไม่เกินจำนวนที่ยืมอยู่
        if return_copies > total_borrowed:
            print(f"\n<<< คืนได้ไม่เกิน {total_borrowed} เล่ม >>>")
            continue
        break

    # หาหนังสือที่ถูกเลือก
    # กำหนด selected_book เป็น None เพื่อรอเก็บข้อมูลหนังสือ
    selected_book = None
    for book in list_book:
        if book["book_id"] == book_id:
            selected_book = book #เจอแล้ว เอาข้อมูลหนังสือใส่ลงแทนที่ None
            break
    
    # ตรวจสอบว่ามีหนังสือที่เลือกหรือไม่
    if selected_book is None:
        print("ไม่พบข้อมูลหนังสือในระบบ")
        return

    # ตัดยอดคืนจากรายการที่ยืมก่อนตามลำดับ จนคืนครบตามจำนวนที่กรอก เช่น ยืม 3 เล่ม คืน 1 เล่ม = จะเหลือรายการยืม 2 เล่ม และจะครบเมื่อคืนหมด
    remaining_to_return = return_copies
    # โค้ดวนรายการยืมทีละรายการของผู้ใช้คนนี้ที่ยังยืมหนังสือรหัสเดียวกันอยู่ และคืนตามจำนวนที่กรอก จนกว่าจะคืนครบ
    for record in active_records:
        # ดึงจำนวนหนังสือที่ยืมไปใน บิล/รายการยืมนั้นๆ ออกมา และถ้าไม่มีข้อมูลจำนวนเล่ม จะถือว่ายืม 1 เล่ม (รองรับข้อมูลเก่า)ที่เคยทดสอบก่อนเพิ่มฟีเจอร์จำนวนเล่มละไม่ได้ลบข้อมูลเก่าออก
        borrowed_copies = record.get("borrow_copies", 1)
        # คำนวณจำนวนเล่มที่จะหักออกจากรายการยืมปัจจุบัน มี min เพราะ ให้เลือกเอาตัวเลขที่น้อยกว่ามาใช้ เพื่อไม่ให้ตัดยอดคืนเกินกว่าที่ยืมไป
        returned_from_record = min(remaining_to_return, borrowed_copies)
        # แก้ไขจำนวนเล่มที่ยืมอยู่ในรายการยืม
        record["borrow_copies"] = borrowed_copies - returned_from_record
        # ถ้าจำนวนเล่มที่ยืมอยู่เป็น 0 แสดงว่าคืนครบแล้ว
        if record["borrow_copies"] == 0:
            record["status"] = "returned"
        # ลดจำนวนเล่มที่ยังต้องคืนออกจากยอดที่กรอก
        remaining_to_return -= returned_from_record
        # ถ้าคืนครบตามจำนวนที่กรอกแล้ว ก็ออกจากลูป ไม่ต้องวนรายการยืมต่อ
        if remaining_to_return == 0:
            break

    # เพิ่มจำนวนเล่มที่คืนกลับไปยัง available_copies ของหนังสือ
    selected_book["available_copies"] += return_copies
    # บันทึกข้อมูลหลังจากคืนหนังสือ
    save_borrow_records(borrow_records)
    save_books(list_book)
    
    # แสดงผลการคืนหนังสือ
    print("\n<<< สถานะการคืน >>>")
    print(f"ผู้ใช้ {name}")
    print(f"คืนหนังสือ {selected_book['book_name']} สำเร็จ")
    print(f"คืนจำนวน: {return_copies} เล่ม")
    print(f"จำนวนที่ยังยืมอยู่: {total_borrowed - return_copies} เล่ม")
    print(f"จำนวนหนังสือที่คงเหลือ: {selected_book['available_copies']}")
