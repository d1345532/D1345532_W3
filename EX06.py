a = float(input('輸入係數 a：'))
b = float(input('輸入係數 b：'))
c = float(input('輸入係數 c：'))
delta = b**2 - 4*a*c
sqrt_delta = delta**0.5
ans1 = (-b + sqrt_delta) / (2*a)
ans2 = (-b - sqrt_delta) / (2*a)
print(f"方程的根為：x1 = {ans1}, x2 = {ans2}")