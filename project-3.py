def generate_odd_series(a):
    x = a // 2 if a % 2 == 0 else (a + 1) // 2
    return [str(num) for num in range(1, 2 * x, 2)]

def main():
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            raise ValueError("Number must be positive.")
        odds = generate_odd_series(a)
        print("Odd number series:", ", ".join(odds))
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
