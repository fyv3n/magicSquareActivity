def createSquare(n):
    magicSquare = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magicSquare[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magicSquare[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    return magicSquare

def printSquare(magicSquare):
    for row in magicSquare:
        print(" ".join(map(str, row)))

def main():
    n = int(input("Enter the size of the Square: (Odd Number) "))
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    magicSquare = createSquare(n)
    print("Size of the MagicSquare", n)
    printSquare(magicSquare)

if __name__ == "__main__":
  main()