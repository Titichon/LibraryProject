#import library
import keyword
import json

def load_books():
    try:
        with open("book.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def load_borrow_records():
    try:
        with open("borrow_reccord.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#ตัวแปรต่างๆ
list_book = load_books()
borrow_records = load_borrow_records()

#save หนังสือ
def save_books():
    with open("book.json", "w", encoding="utf-8") as file:
            json.dump(list_book, file, ensure_ascii=False, indent=4)

def save_borrow_records():
    with open("borrow_reccord.json", "w", encoding="utf-8") as file:
            json.dump(borrow_records, file, ensure_ascii=False, indent=4)

#ตัวฟังก์ชั่นเพิ่มหนังสือ
def add_book():
    global book_copies
    global book_id
    global book_author
    global book_name
    global available_copies
    print(f"\n--- เพิ่มหนังสือ ---")
    book_id = input(f"กรอกข้อมูล book id กรุณาพิมพ์ B นำหน้าตามด้วยหมายเลข: ").strip()

    if not book_id.startswith("B") or not book_id[1:].isdigit():
        print("\n<<< กรุณาพิมพ์ B นำหน้าตามด้วยหมายเลข >>>")
        return
    
    if not book_id:
        print(f"\n<<< กรุณากรอก book id >>>")
        return
    
    for book in list_book:
        if book["book_id"] == book_id:
            print(f"book_id: {book_id} มีอยู่แล้วในระบบ")
            return
        
    
    book_name = input(f"กรอกข้อมูล ชื่อหนังสือ: ").strip()
    if not book_name:
        print(f"\n<<< กรุณากรอกข้อมูล >>>")
        return
    book_author = input(f"กรอกข้อมูล คนเขียน: ").strip()
    if not book_author:
        print(f"<<< กรุณากรอกข้อมูล >>>")
        return
    while True:
        try:
            book_copies = int(input(f"กรอกข้อมูล จำนวนเล่มที่เพิ่ม:"))
            
            if book_copies <= 0:
                print(f"\n<<< กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0 >>>")
                continue
            
            break
            
        except ValueError:
            print(f"\n<<< กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0 >>>")
    
    newbook = {
        "book_id": book_id,
        "book_name": book_name,
        "book_author": book_author,
        "book_copies": book_copies,
        "available_copies": book_copies
    }
    list_book.append(newbook)
    save_books()

    print(f"\n<<< ข้อมูลหนังสือที่เพิ่ม >>>")
    print(f"\nbook_id: {book_id}")
    print(f"ชื่อหนังสือ: {book_name}")
    print(f"คนเขียน: {book_author}")
    print(f"จำนวนเล่มที่เพิ่ม: {book_copies}")
    print(f"\n<<< เพิ่มหนังสือเรียบร้อยแล้ว >>>")




#ตัวฟังก์ชั่นลบหนังสือ
def delete_book():
    print(f"\n--- ลบหนังสือ ---")
    book_id = input(f"กรอกข้อมูล book id: ").strip()
    
    try:
        delete_copies = int(input(f"\nกรอกข้อมูล จำนวนเล่มที่ต้องการลบ:"))
        if delete_copies <= 0:
            print(f"\n<<< กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0 >>>")
            return
    except ValueError:
        print(f"\n<<< กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0 >>>")
        return

    if not book_id:
            print(f"\n<<< กรุณากรอก book id >>>")
            return

    found = False

    for book in list_book:
        if book["book_id"] == book_id:
            found = True

            if delete_copies > book["available_copies"]:
                print(f"\n<<< จำนวนเล่มที่ต้องการลบ มีผู้ยืมอยู่ ไม่สามารถลบได้ >>>")
                return

            book["book_copies"] -= delete_copies
            book["available_copies"] -= delete_copies
            
            if book["book_copies"] <= 0:
                list_book.remove(book)
                print(f"\n<<< ลบหนังสือทั้งหมดออกจากระบบเรียบร้อยแล้ว >>>")
                save_books()
            else:
                save_books()
                print(f"\n<<< ลบหนังสือเรียบร้อยแล้ว >>>")
                print(f"\nbook_id: {book['book_id']}")
                print(f"ชื่อหนังสือ: {book['book_name']}")
                print(f"คนเขียน: {book['book_author']}")
                print(f"จำนวนเล่มที่เหลือ: {book['book_copies']}")
                print(f"จำนวนเล่มที่ยืมได้: {book['available_copies']}")
            break

    if not found:
        print(f"\n<<< ไม่พบหนังสือ >>>")




#ตัวฟังก์ชั่นค้นหาหนังสือ
def search_book():
    print(f"\n--- ค้นหาหนังสือ ---")
    
    if not list_book:
        print(f"\n--- ไม่มีหนังสือในระบบ ---")
        return
    
    keyword = input(f"กรอกชื่อหนังสือที่ต้องการค้นหา:").strip()
    
    if not keyword:
        print(f"กรุณากรอกคำค้นหา")
        return
    
    found = False
    
    for book in list_book:
        if keyword.lower() in book["book_name"].lower():
            found = True
            print("พบรายการหนังสือ:")
            print(f"ชื่อหนังสือ: {book['book_name']}")
            print(f"รหัสหนังสือ: {book['book_id']}")
            print(f"ผู้แต่ง: {book['book_author']}")
            print(f"จำนวนเล่มที่มี: {book['book_copies']}")
            print(f"จำนวนเล่มที่ยืมได้: {book['available_copies']}")
            print("---"*20)
            
    if not found:
        print(f"ไม่พบหนังสือที่ค้นหา")
        return



#ตัวฟังก์ชั่นยืมหนังสือ
def borrow_book():
    print(f"\n--- ยืมหนังสือ ---")

    book_id = input("กรอก book_id:").strip()

    if not book_id:
        print("\n<<< กรุณากรอก book_id >>>")
        return 
    selected_book = None

    for book in list_book:
        if book["book_id"] == book_id:
            selected_book = book
            break

    if selected_book is None:
        print("\n<<< ไม่พบหนังสือเล่มนี้ในระบบ >>>")
        return

    if selected_book["available_copies"] <= 0:
        print("หนังสือเล่มนี้ถูกยืมหมดแล้ว")
        return

    selected_book["available_copies"] -= 1

    borrowed = {
        "name": name,
        "book_id": selected_book[ "book_id"],
        "book_name": selected_book["book_name"],
        "status": "borrowed"
    }

    borrow_records.append(borrowed)
    save_borrow_records()
    save_books()

    print(f"\n<<< สถานะการยืม >>>")
    print(f"\nผู้ใช้ {name}")
    print(f"ยืม {selected_book['book_name']} สำเร็จ")
    print(f"ผู้แต่ง {selected_book['book_author']}")
    print(f"จำนวนหนังสือที่คงเหลือ:{selected_book['available_copies']}")
    print(f"\n<<< ยืมหนังสือเรียบร้อยแล้ว >>>")
    


#ตัวฟังก์ชั่นคืนหนังสือ
def return_book():
    print(f"\n--- คืนหนังสือ ---")

    book_id = input("กรอกรหัสหนังสือ:").strip()

    found = False

    for record in borrow_records:
        if record["book_id"] == book_id and record["status"] == "borrowed":
            found = True
            record["status"] = "returned"
            for book in list_book:
                if book["book_id"] == book_id:
                    book["available_copies"] += 1
                    save_borrow_records()
                    save_books()
                    print(f"ผู้ใช้ {name}")
                    print(f"คืนหนังสือ {book['book_name']} สำเร็จ")
                    print(f"ผู้แต่ง {book['book_author']}")
                    print(f"จำนวนหนังสือที่คงเหลือ: {book['available_copies']}")
                    return
    if not found:
        print(f"ไม่พบรายการยืมที่ยังไม่ได้คืน")
        return



def main_ui():
    global name
    while True:
        name = input(f"\nUser name ('exit' to quite): ").strip()
        if name.lower() == "exit":
            print(f"\n ปิดโปรแกรมแล้ว ขอบคุณที่ใช้บริการ")
            break
        if not name:
            print(f"\nกรุณากรอกชื่อผู้ใช้")
            continue
        print(f"\n===============================")
        print(f"+ ยิดีต้อนรับคุณ [ {name} ] เข้าสู่ระบบ +")
        print(f"===============================")
        while True:
            print(f"\n--- ระบบจัดการห้องสมุด ---")
            print(f"1. เพิ่มหนังสือ")
            print(f"2. ลบหนังสือ")
            print(f"3. ค้นหาหนังสือ")
            print(f"4. ยืมหนังสือ")
            print(f"5. คืนหนังสือ")
            print(f"6. ออกจากระบบ")
            print(f"===============================")
            choice = input(f"กรุณาเลือกเมนู (1-6): ").strip()
            if choice == "1":
                add_book()
            elif choice == "2":
                delete_book()
            elif choice == "3":
                search_book()

            elif choice == "4":
                borrow_book()

            elif choice == "5":
                return_book()

            elif choice == "6":
                print(f"\nออกจากระบบแล้ว ขอบคุณที่ใช้บริการ")
                break
    

main_ui()