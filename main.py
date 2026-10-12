#import library
import keyword


list_book = []

#ตัวฟังก์ชั่นเพิ่มหนังสือ
def add_book():
    print(f"\n--- เพิ่มหนังสือ ---")

    book_id = input(f"กรอกข้อมูล book_id: ").strip()
    
    if not book_id:
        print(f"กรุณากรอกข้อมูลให้ถูกต้อง")
        return
    
    for book in list_book:
        if book["book_id"] == book_id:
            print(f"book_id: {book_id} มีอยู่แล้วในระบบ")
            return
        
    
    book_name = input(f"กรอกข้อมูล ชื่อหนังสือ: ").strip()
    if not book_name:
        print(f"กรุณากรอกข้อมูลให้ถูกต้อง")
        return
    book_author = input(f"กรอกข้อมูล คนเขียน: ").strip()
    if not book_author:
        print(f"กรุณากรอกข้อมูลให้ถูกต้อง")
        return
    while True:
        try:
            book_copies = int(input(f"กรอกข้อมูล จำนวนเล่มที่เพิ่ม:"))
            
            if book_copies <= 0:
                print(f"กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0")
                continue
            
            break
            
        except ValueError:
            print(f"กรุณากรอกข้อมูลที่เป็นตัวเลขจำนวนเต็มบวกเท่านั้นและมากกว่า 0")
    
    newbook = {
        "book_id": book_id,
        "book_name": book_name,
        "book_author": book_author,
        "book_copies": book_copies,
        "available_copies": book_copies
    }
    list_book.append(newbook)

    print(f"\n--- เพิ่มหนังสือเรียบร้อยแล้ว ---")
    print(f"--- ข้อมูลหนังสือที่เพิ่ม ---")
    print(f"book_id: {book_id}")
    print(f"ชื่อหนังสือ: {book_name}")
    print(f"คนเขียน: {book_author}")
    print(f"จำนวนเล่มที่เพิ่ม: {book_copies}")



#ตัวฟังก์ชั่นลบหนังสือ
def delete_book():
    print(f"\n--- ลบหนังสือ ---")

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
    
    if keyword.lower() in list_book[0]["book_name"].lower():
        print("พบรายการหนังสือ:")
    
    found = False
    
    for book in list_book:
        print(book["book_name"])
        if keyword.lower() in book["book_name"].lower():
            found = True
            print(f"ชื่อหนังสือ: {book['book_name']}")
            
    if not found:
        print(f"ไม่พบหนังสือที่ค้นหา")
        return

    print(f"รหัสหนังสือ: {list_book[0]['book_id']}")
    print(f"ชื่อหนังสือ: {list_book[0]['book_name']}")
    print(f"คนเขียน: {list_book[0]['book_author']}")
    print(f"จำนวนเล่มที่มี: {list_book[0]['book_copies']}")
    print("---"*20)


#ตัวฟังก์ชั่นยืมหนังสือ
def borrow_book():
    print(f"\n--- ยืมหนังสือ ---")

#ตัวฟังก์ชั่นคืนหนังสือ
def return_book():
    print(f"\n--- คืนหนังสือ ---")




def main_ui():
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
            print(f"6. ออกจากโปรแกรม")
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