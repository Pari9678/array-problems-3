def max_zeros(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0
    for x in arr:
        if not x: streak += 1
        else: streak = 0
        if streak > best: best = streak
    return

input("max_zeros(n) finds the longest run of 0 in [1..1, 0, 1..1]. press enter")
print("max_zeros(3) =", max_zeros(3))
print("max_zeros(4) =", max_zeros(4))
n = int(input("enter a number: "))
guess = input("What is max_zeros(" + str(n) + ")? ")
input("streak resets to 0 on each 1 - best keeps the highest streak seen. press enter")
print(" max_zeros(" + str(n) + ") =", max_zeros(n), " your guess:", guess)