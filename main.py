import math

def calculate_y(x):
    return 9.2 * math.cos(x ** 2) - math.sin(x / (1.2 - x))

def main():
    i = 26
    h = 0.1 * i
    max_num = 0
    x = 0

    while x < i:
        y = calculate_y(x)
        print("______________________")
        print(f"x = {round(x, 2)} | y = {round(y, 3)}")

        if y > max_num:
            max_num = y

        x += h

    print(f"Максимальное число: {max_num}")

if __name__ == "__main__":
    main()