#import library

#ตัวฟังก์ชั่นเพิ่มหนังสือ
def add_book():
    print(f"\n--- เพิ่มหนังสือ ---")


#ตัวฟังก์ชั่นลบหนังสือ
def delete_book():
    print(f"\n--- ลบหนังสือ ---")

#ตัวฟังก์ชั่นค้นหาหนังสือ
def search_book():
    print(f"\n--- ค้นหาหนังสือ ---")
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