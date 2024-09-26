num = int(input("請輸入一個三位數："))
sum_of_digits = (num // 100) + ((num // 10) % 10) + (num % 10)
print(f"每位數字的總和：{sum_of_digits}")