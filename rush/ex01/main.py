"""ไฟล์สำหรับรับค่าชื่อไฟล์ .chess ผ่าน CLI แล้วนำมาตรวจ Checkmate"""

import sys
from checkmate import checkmate

def main():
    # sys.argv จะเก็บค่าคำสั่งทั้งหมดตอนรันโดยจะดึงตั้งแต่ตำแหน่งที่ 1 (.chess) เป็นต้นไปมาใช้งาน
    file_paths = sys.argv[1:]

    # for loop เพื่อดึงชื่อไฟล์มาเช็คทีละไฟล์
    for path in file_paths:
        # try-except เพื่อดักจับ Error
        try:
            # เปิดไฟล์ในโหมดอ่านอย่างเดียว
            with open(path, 'r') as file:
                # อ่านข้อความทั้งหมดในไฟล์มาเก็บไว้ใน board
                board = file.read()
                
                # ลบ \n ที่อาจจะซ่อนอยู่บรรทัดสุดท้ายของไฟล์ทิ้ง
                board = board.rstrip('\n')
                
                # ส่งเนื้อหาที่อ่านได้ไปให้ checkmate เช็ค
                checkmate(board)
                
        except FileNotFoundError:
            # ถ้าหาไฟล์ไม่เจอจะ Error
            print("Error")
        except Exception:
            # ถ้ามี Error อื่นๆ ก็จะ Error เหมือนกัน
            print("Error")

if __name__ == "__main__":
    main()
