#!/usr/bin/python
from time import perf_counter

# size of the figure
DIM = 5
MAX_MOVES = 11
# This is the game's input. Enter them row by row, starting with the bottom row.
# c = circle, t=triangle, s=square, d=diamond
game_input = "cctct" + "ccssd" + "ssdsd" + "cddtc" + "ttcts"

# Code starts here.
grid = {divmod(i, DIM): k for i, k in enumerate(game_input)}
print(f"------------------------------------------------\nSolving the figure below in {MAX_MOVES} moves or fewer.")
M = {"c": "◯", "t": "△", "s": "□", "d": "◇"}
for row in range(DIM - 1, -1, -1):
    print(f"{row+1}\t", end="")
    for col in range(DIM):
        print(M[grid[(row, col)]], end="\t")
    print()
print("\n\t1\t2\t3\t4\t5\n------------------------------------------------")


def elim(col, g):
    """eliminate the area associated with the selected column."""
    togo = {(0, col)}
    area = {(0, col)}
    while togo:
        p = togo.pop()
        for point in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
            a = (p[0] + point[0], p[1] + point[1])
            if a not in area and g.get(a) == g[(0, col)]:
                togo.add(a)
                area.add(a)
    # this block simulates  elimination of the selected area from the figure
    result = dict()
    for c in range(DIM):
        l = list((r, c) for r in range(DIM) if (r, c) in g and (r, c) not in area)
        for i, p in enumerate(l):
            result[(i, c)] = g[p]
    return result


def solve():
    """recursive solver using backtracking"""
    global DIM, MAX_MOVES, N, g, moves
    if len(moves) > MAX_MOVES:
        # Failure:
        return
    if not g:
        # Have a solution:
        N += 1
        print(f"Solution {N}:\t{[i+1 for i in moves]}")
        return
    # More work to do:
    for col in range(DIM):
        if (0, col) in g and g.get((0, col - 1)) != g[(0, col)]:  # naiive check to speed things up
            old_g = g
            g = elim(col, g)
            moves.append(col)
            solve()
            g = old_g
            moves.pop()
    return


if __name__ == "__main__":
    N = 0
    t = perf_counter()
    moves = []
    g = grid
    solve()
    t = perf_counter() - t
    print(
        f"\n------------------------------------------------\n"
        f"{N} solutions found for {MAX_MOVES} moves in {t:.2f} seconds."
        "\n------------------------------------------------\n"
    )
