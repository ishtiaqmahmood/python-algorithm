def count_ways(symbols, operators):
    """
    Boolean Parenthesization Problem.
    Finds the number of ways to parenthesize the expression so that it evaluates to True.

    Args:
        symbols (str): T or F.
        operators (str): &, |, ^.

    Returns:
        int: Number of ways.
    """
    n = len(symbols)
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        if symbols[i] == 'T': T[i][i] = 1
        else: F[i][i] = 1

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            for k in range(i, j):
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]

                if operators[k] == '&':
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += tik * tkj - T[i][k] * T[k+1][j]
                elif operators[k] == '|':
                    T[i][j] += tik * tkj - F[i][k] * F[k+1][j]
                    F[i][j] += F[i][k] * F[k+1][j]
                elif operators[k] == '^':
                    T[i][j] += T[i][k] * F[k+1][j] + F[i][k] * T[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
    return T[0][n-1]


if __name__ == "__main__":
    symbols = "TTFT"
    operators = "|&^"
    print(f"Number of ways: {count_ways(symbols, operators)}")
