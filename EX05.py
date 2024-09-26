num = int(input("輸入三位數字："))
reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
print(f"結果：{reverse}")