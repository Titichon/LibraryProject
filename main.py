# libary นำเข้าฟังก์ชันจัดการหนังสือต่างๆในโปรแกรม
from book_service import add_book, delete_book, search_book # นำเข้าฟังก์ชันจัดการหนังสือ add, delete, search หนังสือ
from borrow_service import borrow_book, return_book # นำเข้าฟังก์ชันยืมและคืนหนังสือ
from data_handler import load_books, load_borrow_records # นำเข้าฟังก์ชันโหลดข้อมูลหนังสือและบันทึกการยืมคืนจากไฟล์

# ฟังก์ชชั่นเมนูหลัก
def main_ui():
    list_book = load_books() # โหลดข้อมูลหนังสือจากไฟล์ book.json และเก็บไว้ในตัวแปร list_book
    borrow_records = load_borrow_records() # โหลดข้อมูลการยืมคืนจากไฟล์ borrow_reccord.json และเก็บไว้ในตัวแปร borrow_records

    # ฟังก์ชันสำหรับการเข้าสู่ระบบผู้ใช้
    while True:
        name = input("\nUser name ('exit' to quit): ").strip() # รับค่าที่ผู้ใช้กรอก
        if name.lower() == "exit": # ตรวจสอบว่าผู้ใช้กรอก exit หรือไม่ ถ้าใช่ก็ออกจากโปรแกรม
            print("\nปิดโปรแกรมแล้ว ขอบคุณที่ใช้บริการ")
            break
        if not name: # ตรวจสอบว่าผู้ใช้กรอกชื่อหรือไม่ ถ้าไม่ก็แจ้งเตือนให้กรอกชื่อ
            print("\nกรุณากรอกชื่อผู้ใช้")
            continue

        print("\n===============================")
        print(f"+ ยินดีต้อนรับคุณ [ {name} ] เข้าสู่ระบบ +")
        print("===============================")

        # ฟังก์ชั่นให้เลือกเมนู
        while True: # วนลูปเมนูหลักจะได้ไม่ต้องกลับไป login
            print("\n--- ระบบจัดการห้องสมุด ---")
            print("1. เพิ่มหนังสือ")
            print("2. ลบหนังสือ")
            print("3. ค้นหาหนังสือ")
            print("4. ยืมหนังสือ")
            print("5. คืนหนังสือ")
            print("6. ออกจากระบบ")
            print("===============================")
            choice = input("กรุณาเลือกเมนู (1-6): ").strip()
            # ตัวเลือกเมนูที่ให้ผู้ใช้เลือกว่าจะทำอะไร
            if choice == "1": # กด 1 เลือกเมนูเพิ่มหนังสือ
                add_book(list_book) # เรียกใช้ฟังก์ชัน add_book จาก book_service.py เพื่อเพิ่มหนังสือ
            elif choice == "2": # กด 2 เลือกเมนูลบหนังสือ
                delete_book(list_book) # เรียกใช้ฟังก์ชัน delete_book จาก book_service.py เพื่อลบหนังสือ
            elif choice == "3": # กด 3 เลือกเมนูค้นหาหนังสือ
                search_book(list_book) # เรียกใช้ฟังก์ชัน search_book จาก book_service.py เพื่อค้นหาหนังสือ
            elif choice == "4": # กด 4 เลือกเมนูยืมหนังสือ
                borrow_book(list_book, borrow_records, name) # เรียกใช้ฟังก์ชัน borrow_book จาก borrow_service.py เพื่อยืมหนังสือ
            elif choice == "5": # กด 5 เลือกเมนูคืนหนังสือ
                return_book(list_book, borrow_records, name) # เรียกใช้ฟังก์ชัน return_book จาก borrow_service.py เพื่อคืนหนังสือ
            elif choice == "6": # กด 6 เลือกเมนูออกจากระบบ
                print("\nออกจากระบบแล้ว ขอบคุณที่ใช้บริการ") # แจ้งเตือนผู้ใช้ว่าออกจากระบบแล้ว
                break # ออกจากลูปเมนูหลักและกลับไปหน้า login
            else:
                print("\n<<< กรุณาเลือกเมนูที่ถูกต้อง >>>") # แจ้งเตือนผู้ใช้ให้เลือกเมนูที่ถูกต้อง

# สั่งรัน main_ui เฉพาะตอนรันไฟล์นี้โดยตรงเท่านั้น
if __name__ == "__main__":
    main_ui()
