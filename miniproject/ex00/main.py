from checkmate import checkmate
def main() -> None:
    board = """\
R...
.K..
..P.
....
"""
    checkmate(board)
if __name__ == "__main__":
    main()