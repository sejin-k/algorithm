n = int(input())
numbers = []
numbers = list(map(int, input().split()))

print("{} {}".format(min(numbers), max(numbers)))