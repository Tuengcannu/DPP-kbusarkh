

from checkmate import checkmate

def main():
    
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Test 1 (Expected: Success):")
    checkmate(board1)

    
    board2 = """\
R...
.B..
..K.
....\
"""
    print("\nTest 2 (Expected: Fail):")
    checkmate(board2)

    
    board3 = """\
R..
.K..
....\
"""
    print("\nTest 3 (Expected: Error):")
    checkmate(board3)

if __name__ == "__main__":
    main()