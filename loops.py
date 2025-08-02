isSuccess = True
for num in range(0, 10, 2):
    # print(f"Attempt {num+1}")
    print("Attempt", num + 1, (num+1) * ".")
    if isSuccess:
        print("Successful")
        break
else:
    print("Did not complete")

for x in range(2):
    for y in range(2):
        print(f"{x}, {y}")

print(type(range(5)))

for x in "python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2
