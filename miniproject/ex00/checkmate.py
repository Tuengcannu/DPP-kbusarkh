#!/usr/bin/env python3

def checkmate(board: str) -> None:
    try:
        # 1. ตรวจสอบความถูกต้องของข้อมูลนำเข้า (Input Validation)
        if not isinstance(board, str) or not board.strip():
            print("Error")
            return

        # แยกแต่ละแถวออกจากกันและลบบรรทัดว่างทิ้ง
        rows = [row for row in board.splitlines() if row]

        if not rows:
            print("Error")
            return

        height = len(rows)
        width = len(rows[0])

        # ตรวจสอบว่ากระดานเป็นรูปทรงสี่เหลี่ยมที่สมบูรณ์หรือไม่
        if any(len(row) != width for row in rows):
            print("Error")
            return

        # 2. ค้นหาตำแหน่งของ King ('K') บนกระดาน
        king_pos = None
        for r in range(height):
            for c in range(width):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        # ถ้าไม่มี King บนกระดาน
        if not king_pos:
            print("Fail")
            return

        kr, kc = king_pos

        # 3. ฟังก์ชันผู้ช่วย: ยิงเรดาร์ตรวจสอบไปในทิศทางที่กำหนด (Ray-casting)
        def search_direction(dr: int, dc: int, threats: set) -> bool:
            r, c = kr + dr, kc + dc
            while 0 <= r < height and 0 <= c < width:
                piece = rows[r][c]
                if piece != '.':
                    # ถ้าเจอตัวหมาก ให้เช็คว่าเป็นตัวที่สามารถโจมตีในทิศทางนี้ได้หรือไม่
                    if piece in threats:
                        return True
                    return False # ถ้าเป็นตัวอื่น แปลว่าเส้นทางถูกบล็อก (รอดพ้นการโจมตี)
                r += dr
                c += dc
            return False

        # 4. ตรวจสอบการถูกโจมตี (In Check)
        # 4.1 เช็คแนวตั้งและแนวนอน: ตัวที่โจมตีได้คือ Rook (R) และ Queen (Q)
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if any(search_direction(dr, dc, {'R', 'Q'}) for dr, dc in straight_dirs):
            print("Success")
            return

        # 4.2 เช็คแนวทแยง: ตัวที่โจมตีได้คือ Bishop (B) และ Queen (Q)
        diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if any(search_direction(dr, dc, {'B', 'Q'}) for dr, dc in diagonal_dirs):
            print("Success")
            return

        # 4.3 เช็คระยะประชิด 1 ก้าวในแนวทแยง: ตัวที่โจมตีได้คือ Pawn (P)
        # (กติกาไม่ได้ระบุว่าฝั่งไหนคือด้านหน้า จึงเช็คทั้ง 4 มุมทแยงรอบตัว King เพื่อความปลอดภัยสูงสุด)
        for dr, dc in diagonal_dirs:
            pr, pc = kr + dr, kc + dc
            if 0 <= pr < height and 0 <= pc < width:
                if rows[pr][pc] == 'P':
                    print("Success")
                    return

        # ถ้าเช็คทุกทิศทางแล้วปลอดภัย
        print("Fail")

    except Exception:
        # หากเกิด Error ที่ไม่คาดคิด (ป้องกันโปรแกรม Crash ตามข้อบังคับ)
        print("Error")