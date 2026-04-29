class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                box_key = (i // 3, j // 3)
                if box_key not in boxes:
                    boxes[box_key] = set()

                if val in boxes[box_key]:
                    return False
                boxes[box_key].add(val)

        return True