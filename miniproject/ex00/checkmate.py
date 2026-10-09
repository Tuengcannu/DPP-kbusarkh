

def checkmate(board: str) -> None:
    try:
       
        if not isinstance(board, str) or not board.strip():
            print("Error")
            return

        
        rows = [row for row in board.splitlines() if row]

        if not rows:
            print("Error")
            return

        height = len(rows)
        width = len(rows[0])

        
        if any(len(row) != width for row in rows):
            print("Error")
            return

        
        king_pos = None
        for r in range(height):
            for c in range(width):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        
        if not king_pos:
            print("Fail")
            return

        kr, kc = king_pos

        
        def search_direction(dr: int, dc: int, threats: set) -> bool:
            r, c = kr + dr, kc + dc
            while 0 <= r < height and 0 <= c < width:
                piece = rows[r][c]
                if piece != '.':
                    
                    if piece in threats:
                        return True
                    return False 
                r += dr
                c += dc
            return False

        
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if any(search_direction(dr, dc, {'R', 'Q'}) for dr, dc in straight_dirs):
            print("Success")
            return

        
        diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if any(search_direction(dr, dc, {'B', 'Q'}) for dr, dc in diagonal_dirs):
            print("Success")
            return

        
        for dr, dc in diagonal_dirs:
            pr, pc = kr + dr, kc + dc
            if 0 <= pr < height and 0 <= pc < width:
                if rows[pr][pc] == 'P':
                    print("Success")
                    return

        
        print("Fail")

    except Exception:
        
        print("Error")