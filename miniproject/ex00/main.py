#!/usr/bin/env python3

from checkmate import checkmate

def main():
    # บอร์ดทดสอบที่ 1 (กรณีปกติ: Rook กำลังโจมตี)
    board1 = """\
R...
K...
..P.
....\
"""
    print("Test 1 (Expected: Success):")
    checkmate(board1)

    # บอร์ดทดสอบที่ 2 (กรณีมีตัวหมากบล็อกเส้นทาง)
    board2 = """\
R...
.B..
..K.
....\
"""
    print("\nTest 2 (Expected: Fail):")
    checkmate(board2)

    # บอร์ดทดสอบที่ 3 (กรณี Error: กระดานแหว่ง ไม่เป็นสี่เหลี่ยม)
    board3 = """\
R..
.K..
....\
"""
    print("\nTest 3 (Expected: Error):")
    checkmate(board3)

if __name__ == "__main__":
    main()