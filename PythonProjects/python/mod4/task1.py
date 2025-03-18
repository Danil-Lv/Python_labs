nums = list(map(int, input().split()))
if len(set(nums)) == 1:
    print("Все числа равны")
elif len(set(nums)) == len(nums):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")