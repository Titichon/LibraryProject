# libary ต่างๆที่ใช้ในโปรแกรม
import json # นำเข้าไลบรารี json เพื่อใช้ในการจัดการข้อมูล JSON

# กำหนดชื่อไฟล์สำหรับเก็บข้อมูลหนังสือและประวัติการยืมและคืนหนังสือ
BOOKS_FILE = "book.json"
BORROW_RECORDS_FILE = "borrow_reccord.json"

# ฟังก์ชันสำหรับโหลดข้อมูลหนังสือ
def load_books():
    try:
        # with ช่วยเปิดและปิดไฟล์ให้อัตโนมัติเมื่อทำงานจบ, open(...) ฟังก์ชันสำหรับเปิดไฟล์, BOOKS_FILE ชื่อไฟล์ที่จะเปิด ("book.json"), "r": โหมดอ่านข้อมูล (Read Mode)
        # encoding="utf-8": "urf-8" เป็นรหัสรองรับภาษาไทย
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file) # อ่านข้อความในไฟล์ JSON แล้วแปลงกลับมาเป็นโครงสร้างข้อมูลประเภท List/Dictionary ของ Python
    except FileNotFoundError: # เอาไว้ในกรณีที่ไฟล์ book.json ไม่พบ ให้ return ค่าเป็น list ว่าง
        return []

# ฟังก์ชันสำหรับโหลดประวัติการยืม-คืนหนังสือ
def load_borrow_records():
    try:
        # with ช่วยเปิดและปิดไฟล์ให้อัตโนมัติเมื่อทำงานจบ, open(...) ฟังก์ชันสำหรับเปิดไฟล์, BORROW_RECORDS_FILE ชื่อไฟล์ที่จะเปิด, ("borrow_reccord.json") "r": โหมดอ่านข้อมูล (Read Mode)
        # encoding="utf-8": "urf-8" เป็นรหัสรองรับภาษาไทย
        with open(BORROW_RECORDS_FILE, "r", encoding="utf-8") as file:
            return json.load(file) # อ่านข้อความในไฟล์ JSON แล้วแปลงกลับมาเป็นโครงสร้างข้อมูลประเภท List/Dictionary ของ Python
    except FileNotFoundError: # เอาไว้ในกรณีที่ไฟล์ borrow_reccord.json ไม่พบ ให้ return ค่าเป็น list ว่าง
        return []

# ฟังก์ชันสำหรับบันทึกข้อมูลหนังสือ
def save_books(list_book):
    # with ช่วยเปิดและปิดไฟล์ให้อัตโนมัติเมื่อทำงานจบ, open(...) ฟังก์ชันสำหรับเปิดไฟล์ BOOKS_FILE, ชื่อไฟล์ที่จะเปิด ("book.json"), "w": โหมดเขียนข้อมูล (Write Mode)
    # encoding="utf-8": "urf-8" เป็นรหัสรองรับภาษาไทย
    with open (BOOKS_FILE, "w", encoding="utf-8") as file:
        # json.dump(...) ฟังก์ชันแปลงข้อมูล Python  แล้วบันทึกลงไฟล์ JSON, list_book ชื่อข้อมูลที่ต้องการบันทึก,file ตัวแปรไฟล์ปลายทางที่เปิดรอไว้,
        #ensure_ascii=False: สั่งให้บันทึกเป็นอักขระภาษาไทยตรงๆ, indent=4: สั่งให้จัดรูปแบบไฟล์ JSON ให้สวยงามด้วยการเยื้อง 4 ช่องว่าง
        json.dump(list_book, file, ensure_ascii=False, indent=4)

# ฟังก์ชันสำหรับบันทึกประวัติการยืม-คืนหนังสือ
def save_borrow_records(borrow_records):
    # with ช่วยเปิดและปิดไฟล์ให้อัตโนมัติเมื่อทำงานจบ, open(...) ฟังก์ชันสำหรับเปิดไฟล์ BORROW_RECORDS_FILE, ชื่อไฟล์ที่จะเปิด ("borrow_reccord.json"), "w": โหมดเขียนข้อมูล (Write Mode)
    # encoding="utf-8": "urf-8" เป็นรหัสรองรับภาษาไทย
    with open(BORROW_RECORDS_FILE, "w", encoding="utf-8") as file:
        json.dump(borrow_records, file, ensure_ascii=False, indent=4)
