from typing import List, Optional, Tuple


Position = Tuple[int, int]
Board = List[str]


class InvalidBoardError(ValueError):
    """Raised when the chessboard does not satisfy the input rules."""


def parse_board(board_text: str) -> Board:
    """Convert multiline text into a normalized chessboard."""
    if not isinstance(board_text, str):
        raise InvalidBoardError("Board must be a string.")

    rows = board_text.strip().splitlines()

    if not rows:
        raise InvalidBoardError("Board cannot be empty.")

    
    rows = [row.strip() for row in rows]

    if any(not row for row in rows):
        raise InvalidBoardError("Board cannot contain empty rows.")

    return rows


def validate_board(board: Board) -> None:
    """Validate board dimensions and King count."""
    size = len(board)

    if size == 0:
        raise InvalidBoardError("Board cannot be empty.")

    if any(len(row) != size for row in board):
        raise InvalidBoardError(
            "Board must be square and every row must have equal length."
        )

    king_count = sum(row.count("K") for row in board)

    if king_count != 1:
        raise InvalidBoardError(
            "Board must contain exactly one King."
        )


def find_king(board: Board) -> Position:
    """Return the King position as (row, column)."""
    for row_index, row in enumerate(board):
        column_index = row.find("K")

        if column_index != -1:
            return row_index, column_index

    
    raise InvalidBoardError("King not found.")


def is_inside(board: Board, row: int, col: int) -> bool:
    """Check whether a position is inside the board."""
    size = len(board)
    return 0 <= row < size and 0 <= col < size


def is_attacked_by_sliding_piece(
    board: Board,
    king_row: int,
    king_col: int,
) -> bool:
    """Check attacks from Rook, Bishop, and Queen."""
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1),    # Right
        (-1, -1),  # Up-left
        (-1, 1),   # Up-right
        (1, -1),   # Down-left
        (1, 1),    # Down-right
    ]

    size = len(board)

    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]

            
            if piece == ".":
                row += dr
                col += dc
                continue

            
            distance = max(
                abs(row - king_row),
                abs(col - king_col),
            )

            is_diagonal = abs(dr) == 1 and abs(dc) == 1

            if piece == "Q":
                return True

            if is_diagonal and piece == "B":
                return True

            if not is_diagonal and piece == "R":
                return True

            
            break

    return False


def is_attacked_by_pawn(
    board: Board,
    king_row: int,
    king_col: int,
) -> bool:
    """Check Pawn attacks using the direction shown in the subject."""
    pawn_row = king_row + 1

    for pawn_col in (king_col - 1, king_col + 1):
        if is_inside(board, pawn_row, pawn_col):
            if board[pawn_row][pawn_col] == "P":
                return True

    return False


def is_in_check(board_text: str) -> bool:
    """Return True when the King is attacked."""
    board = parse_board(board_text)
    validate_board(board)

    king_row, king_col = find_king(board)

    if is_attacked_by_pawn(board, king_row, king_col):
        return True

    if is_attacked_by_sliding_piece(board, king_row, king_col):
        return True

    return False


def checkmate(board_text: str) -> None:
    """Print the result required by the Rush00 subject."""
    try:
        result = is_in_check(board_text)
    except (InvalidBoardError, TypeError):
        print("Error")
        return

    print("Success" if result else "Fail")