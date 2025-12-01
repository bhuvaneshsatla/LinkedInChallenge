num = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 84, 44, 35, 49, 38, 92, 70, 92, 9, 24, 65, 92, 0],
    [0, 9, 1, 49, 52, 22, 44, 94, 51, 6, 20, 26, 17, 0],
    [0, 78, 54, 21, 64, 53, 90, 20, 26, 27, 20, 69, 46, 0],
    [0, 32, 20, 46, 67, 25, 96, 32, 35, 65, 26, 8, 17, 0],
    [0, 86, 26, 37, 73, 7, 31, 20, 31, 20, 26, 3, 42, 0],
    [0, 32, 82, 13, 69, 35, 86, 26, 64, 21, 18, 14, 30, 0],
    [0, 20, 30, 36, 20, 26, 2, 63, 20, 26, 3, 41, 42, 0],
    [0, 26, 20, 77, 94, 3, 29, 44, 20, 20, 26, 50, 71, 0],
    [0, 11, 26, 50, 19, 20, 26, 62, 26, 58, 90, 44, 84, 0],
    [0, 37, 49, 43, 81, 65, 15, 31, 60, 15, 8, 1, 8, 0],
    [0, 99, 58, 52, 1, 69, 37, 88, 76, 97, 47, 14, 48, 0],
    [0, 59, 59, 7, 94, 17, 75, 65, 11, 34, 43, 66, 86, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

]

side = len(num)
count = 0
pos = []
product = []

for i in range(side):
    for j in range(side):

        if num[i][j] == 20:
            if num[i + 1][j] == 26:
                pos.append([i - 1, j - 1])
                count += 1
                prod = 1

                for x in range(i - 1, i + 3):
                    for y in range(j - 1, j + 2):

                        if num[x][y] != 0:
                            prod *= num[x][y]

                product.append((prod / (20 * 26)))

        if num[i][j] == 20:
            if num[i][j + 1] == 26:
                pos.append([i - 1, j - 1])
                count += 1
                prod = 1
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 3):

                        if num[x][y] != 0:
                            prod *= num[x][y]

                product.append((prod / (20 * 26)))

print("2026 found at:\n")

for i in range(count):
    print("position: " + str(pos[i]) + ", product: " + str(product[i]) + "\n")

print("maximum product: " + str(max(product)))