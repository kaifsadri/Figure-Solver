from time import perf_counter

# size of the figure
DIM = 5
MAX_MOVES = 11
# This is the game's input. Enter them row by row, starting with the bottom row.
# c = circle, t=triangle, s=square, d=diamond
game_input = "cttdc" + "sccct" + "tcssd" + "tdctt" + "ddttd"

# Code starts here.
grid = {divmod(i, DIM): k for i, k in enumerate(game_input)}
print(f"------------------------------------------------\nGame input below. {MAX_MOVES} moves allowed.")
M = {"c": "◯", "t": "△", "s": "□", "d": "◇"}
for row in range(DIM - 1, -1, -1):
    print(f"{row+1}\t", end="")
    for col in range(DIM):
        print(M[grid[(row, col)]], end="\t")
    print()
print("\t1\t2\t3\t4\t5\n------------------------------------------------")


def elim(col, g=grid):
    """eliminate the area associated with the selected column."""
    togo = {(0, col)}
    been = {(0, col)}
    area = {(0, col)}
    while togo:
        p = togo.pop()
        for point in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
            a = (p[0] + point[0], p[1] + point[1])
            if a not in g:
                continue
            if a not in been:
                been.add(a)
                if g[a] == g[(0, col)]:
                    togo.add(a)
                    area.add(a)
    result = dict()
    for col in range(DIM):
        l = list((row, col) for row in range(DIM) if (row, col) in g and (row, col) not in area)
        for i, p in enumerate(l):
            result[(i, col)] = g[p]
    return result


def solve(g, moves):
    """recursive solver"""
    if len(moves) > MAX_MOVES:
        return (moves, False)
    if not g:
        return (moves, True)
    for col in range(DIM):
        if (0, col) in g:
            r = solve(elim(col, g), moves + [col])
            if r[1]:
                return r
    return (moves, False)


t = perf_counter()
S = solve(grid, [])[0]
t = perf_counter() - t
print(f"Solved in {t:.2f} seconds: {[i+1 for i in S]}\n------------------------------------------------")
