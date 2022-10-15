# sum = 0
# nums = []
# print("Enter 5 elements for the list: ")
# for i in range(5):
#     val = int(input())
#     nums.append(val)

# for i in range(5):
#     if nums[i] % 2 == 1:
#         sum = sum + nums[i]

# print("\nSum of Even Numbers is", sum)


# sum = 1
# for i in range(1, 11):
#     sum = sum + i

# print(sum)

# prod = 1
# for i in range(1, 11):
#     prod = prod * i

# print(prod)

# num = int(input("Enter a number to find factorial: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i
#     print(fact)


num = int(input("Enter a number to find factorial: "))
first = 0
second = 1
print(first)
print(second)
for i in range(2, num):
    third = first + second
    print(third)
    first = second
    second = third
