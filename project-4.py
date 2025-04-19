def count_multiples(nums):
    multiples_count = {i: 0 for i in range(1, 10)}
    for num in nums:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    return multiples_count

# output
if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter a list of integers: ").split()))
        result = count_multiples(nums)
        print("Multiples count:", result)
    except ValueError:
        print("Please enter valid integers only.")
