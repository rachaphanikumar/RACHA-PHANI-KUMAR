def generate_odd_series(a: int) -> str:
    series = [str(2 * i + 1) for i in range(a)]
    return ",".join(series)


# output
if __name__ == "__main__":
    try:
        a = int(input("Enter the number of odd numbers to generate: "))
        print("Odd Number Series:", generate_odd_series(a))
    except ValueError as e:
        print("Invalid input:", e)
