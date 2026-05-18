import math


def baby_step_giant_step(a, b, m):
    """
    Baby-step Giant-step algorithm to solve a^x ≡ b (mod m).
    """
    n = int(math.sqrt(m)) + 1
    baby_steps = {}
    for j in range(n):
        baby_steps[pow(a, j, m)] = j

    giant_step = pow(a, n * (m - 2), m) # a^(-n) mod m using Fermat's Little Theorem (m must be prime)
    # Correct generic giant_step:
    # a_inv_n = pow(modInverse(pow(a, n, m), m), 1, m)

    cur = b
    for i in range(n):
        if cur in baby_steps:
            return i * n + baby_steps[cur]
        cur = (cur * giant_step) % m
    return None


if __name__ == "__main__":
    # 2^x ≡ 3 (mod 11) => 2^8 = 256 ≡ 3 (mod 11)
    print(f"x in 2^x ≡ 3 (mod 11): {baby_step_giant_step(2, 3, 11)}")
