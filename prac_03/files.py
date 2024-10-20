FILENAME = "name.txt"
# Question 1
user_name = str(input("Enter your name: "))
out_file = open(FILENAME, 'w')
print(f"{user_name}", file=out_file)
out_file.close()

# # Question 2
in_file = open(FILENAME, 'r')
for line in in_file:
    print(f"Hi {line}")
in_file.close()

# Question 3, for the purpose of code working without commenting I am aware naming convention is incorrect.
# opened 'with' version
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    result = first_number + second_number
    print(result)
file.close()

# Question 4
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(total)
file.close()
