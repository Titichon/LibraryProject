# libary นำเข้าฟังก์
from data_handler import save_books # นำเข้าฟังก์ชันบันทึกข้อมูลหนังสือและบันทึกการยืมคืนลงไฟล์

#ฟังก์ชั่นเพิ่มหนังสือ
def add_book(list_book):
    print("\n--- เพิ่มหนังสือ ---")
    print("กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก")
    book_id = input("กรอกข้อมูล book id กรุณาพิมพ์ B นำหน้าตามด้วยหมายเลข: ").strip() # รับค่าที่ผู้ใช้กรอก
    # ท่านผู้ใช้กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก
    if book_id == "exit":
        return

    # ตรวจสอบว่าผู้ใช้กรอก book_id หรือไม่
    if not book_id:
        print("\n<<< กรุณากรอก book id >>>")
        return
    # ตรวจสอบว่าผู้ใช้กรอก book_id ถูกต้องหรือไม่ (ต้องขึ้นต้นด้วย B ตามด้วยตัวเลข)
    if not book_id.startswith("B") or not book_id[1:].isdigit():
        print("\n<<< กรุณาพิมพ์ B นำหน้าตามด้วยหมายเลข >>>")
        return

    # ตรวจสอบว่ามี book_id ซ้ำในระบบหรือไม่
    for book in list_book:
        if book["book_id"] == book_id:
            print(f"book_id: {book_id} มีอยู่แล้วในระบบ")
            return

    # ตรวจสอบว่าผู้ใช้กรอกชื่อหนังสือหรือไม่
    book_name = input("กรอกข้อมูล ชื่อหนังสือ: ").strip()
    if not book_name:
        print("\n<<< กรุณากรอกข้อมูล >>>")
        return
    
    # ตรวจสอบว่าผู้ใช้กรอกชื่อคนเขียนหรือไม่
    book_author = input("กรอกข้อมูล คนเขียน: ").strip()
    if not book_author:
        print("<<< กรุณากรอกข้อมูล >>>")
        return
    
    # ตรวจสอบว่าผู้ใช้กรอกจำนวนเล่มหรือไม่
    while True:
        try:
            book_copies = int(input("กรอกข้อมูล จำนวนเล่มที่เพิ่ม: "))
            if book_copies <= 0:
                print("\n<<< จำนวนเล่มต้องเป็นจำนวนเต็มบวกและมากกว่า 0 >>>")
                continue
            break
        except ValueError:
            print("\n<<< จำนวนเล่มต้องเป็นจำนวนเต็มบวกและมากกว่า 0 >>>")
    
    # สร้าง dictionary สำหรับหนังสือใหม่
    new_book = {
        "book_id": book_id, # กำหนดค่า book_id ของหนังสือใหม่
        "book_name": book_name, # กำหนดค่า book_name ของหนังสือใหม่
        "book_author": book_author, # กำหนดค่า book_author ของหนังสือใหม่
        "book_copies": book_copies, # กำหนดค่า book_copies ของหนังสือใหม่
        "available_copies": book_copies, # กำหนดค่า available_copies ของหนังสือใหม่
    }
    list_book.append(new_book) # เพิ่มหนังสือใหม่ลงใน list_book
    save_books(list_book) # บันทึกข้อมูลหนังสือใหม่ลงในไฟล์

    # แสดงข้อมูลหนังสือที่เพิ่ม
    print("\n<<< ข้อมูลหนังสือที่เพิ่ม >>>")
    print(f"\nbook_id: {book_id}")
    print(f"ชื่อหนังสือ: {book_name}")
    print(f"คนเขียน: {book_author}")
    print(f"จำนวนเล่มที่เพิ่ม: {book_copies}")
    print("\n<<< เพิ่มหนังสือเรียบร้อยแล้ว >>>")

# ฟังก์ชั่นลบหนังสือ
def delete_book(list_book):
    print("\n--- ลบหนังสือ ---")
    print("กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก")
    book_id = input("กรอกข้อมูล book id: ").strip() # รับค่าที่ผู้ใช้กรอก
    
    # ท่านผู้ใช้กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก
    if book_id == "exit":
        return
    
    # ตรวจสอบว่าผู้ใช้กรอก book_id หรือไม่
    if not book_id:
        print("\n<<< กรุณากรอก book id >>>")
        return

    # หาหนังสือก่อน
    book = next((b for b in list_book if b["book_id"] == book_id), None)
    if book is None:
        print("\n<<< ไม่พบหนังสือที่ต้องการลบ >>>")
        return

    if book["available_copies"] == 0:
        print("\n<<< ไม่มีเล่มว่างให้ลบ (ทุกเล่มถูกยืมอยู่) >>>")
        return

    while True:
        text = input("\nกรอกข้อมูล จำนวนเล่มที่ต้องการลบ: ").strip()
        if text == "exit":
            return
        try:
            delete_copies = int(text)
        except ValueError:
            print("\n<<< จำนวนเล่มต้องเป็นจำนวนเต็มบวกและมากกว่า 0 >>>")
            continue
        if delete_copies <= 0:
            print("\n<<< จำนวนเล่มต้องเป็นจำนวนเต็มบวกและมากกว่า 0 >>>")
            continue
        if delete_copies > book["available_copies"]:
            print("\n<<< จำนวนเล่มที่ต้องการลบเกินจำนวนเล่มที่มีอยู่ >>>")
            print(f"จำนวนเล่มที่มีอยู่: {book['available_copies']}")
            continue
        break
        
    # ลดจำนวนเล่มที่ต้องการลบออกจาก book_copies และ available_copies ของหนังสือ
    book["book_copies"] -= delete_copies # นำจำนวนเล่มที่ต้องการลบ ลบออกจาก book_copies ของหนังสือ
    book["available_copies"] -= delete_copies # นำจำนวนเล่มที่ต้องการลบ ลบออกจาก available_copies ของหนังสือ
        
    # ตรวจสอบว่าจำนวนเล่มที่เหลือเป็น 0 หรือไม่ ถ้าใช่ก็ลบหนังสือออกจาก list_book
    if book["book_copies"] == 0: # ถ้าจำนวนเล่มที่เหลือเป็น 0
        list_book.remove(book) # ลบหนังสือออกจาก list_book
        print("\n<<< ลบหนังสือทั้งหมดออกจากระบบเรียบร้อยแล้ว >>>")
    else: # ถ้าจำนวนเล่มที่เหลือไม่เป็น 0 ให้แสดงข้อมูลหนังสือที่เหลืออยู่
        print("\n<<< ลบหนังสือเรียบร้อยแล้ว >>>")
        print(f"\nbook_id: {book['book_id']}")
        print(f"ชื่อหนังสือ: {book['book_name']}")
        print(f"คนเขียน: {book['book_author']}")
        print(f"จำนวนเล่มทั้งหมด: {book['book_copies']}")
        print(f"จำนวนเล่มที่ยืมได้: {book['available_copies']}")
    save_books(list_book) # บันทึกข้อมูลหนังสือใหม่ลงในไฟล์ data_handler.py และส่งต่อข้อมูลไป book.json


# ฟังก์ชั่นค้นหาหนังสือ
def search_book(list_book):
    print("\n--- ค้นหาหนังสือ ---")
    print("กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก")
    if not list_book:
        print("\n--- ไม่มีหนังสือในระบบ ---")
        return
    # ตรวจสอบว่าผู้ใช้กรอกคำค้นหาหรือไม่
    keyword = input("กรอกชื่อหนังสือที่ต้องการค้นหา: ").strip()
    
    # ท่านผู้ใช้กรอก 'exit' เพื่อย้อนกลับไปหน้าเมนูหลัก
    if keyword == "exit":
        return
    
    # ตรวจสอบว่าผู้ใช้กรอกคำค้นหาหรือไม่
    if not keyword:
        print("กรุณากรอกคำค้นหา")
        return
    
    # ค้นหาหนังสือที่มีชื่อหนังสือที่ตรงกับคำค้นหา
    found = False
    for book in list_book: # วนลูปตรวจสอบหนังสือทั้งหมดใน list_book
        if keyword.lower() not in book["book_name"].lower(): # รับค่าที่กรอกแล้วเปรียบเทียบกับชื่อหนังสือในระบบ มี .lower() เพื่อให้ไม่สนใจตัวพิมพ์ใหญ่หรือตัวพิมพ์เล็ก
            continue # ท่านผู้ใช้กรอกคำค้นหาไม่ตรงกับชื่อหนังสือในระบบ ให้ข้ามไปตรวจสอบหนังสือเล่มถัดไป
        found = True # พบหนังสือที่ค้นหา แสดงผลข้อมูลหนังสือที่ค้นหา
        print("พบรายการหนังสือ:") 
        print(f"ชื่อหนังสือ: {book['book_name']}")
        print(f"book_id: {book['book_id']}")
        print(f"ผู้แต่ง: {book['book_author']}")
        print(f"จำนวนเล่มทั้งหมด: {book['book_copies']}")
        print(f"จำนวนเล่มที่ยืมได้: {book['available_copies']}")
        print("---" * 20)
    if not found: # ถ้าไม่พบหนังสือที่ค้นหาแสดงข้อความแจ้งเตือน
        print("ไม่พบหนังสือที่ค้นหา")
