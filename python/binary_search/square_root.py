def square_root(n: int) -> int:
    if n == 0 or n == 1:
        return n

    left, right = 2, n
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


if __name__ == '__main__':
    n = 4
    res = square_root(n)
    print(res)
