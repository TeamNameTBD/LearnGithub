# For loops
# for loop goes through each value in an iterable (such as a list) and does something for each item

list1 = ["Jonathan", "Andrew", "Devin"]
for person in list1:
    print(person + " is a good guy")

for i in range(15):
    print(i)

# While Loops
# Will loop forever until condition is changed

count = 0
while count < 15:
    count += 1
    print(count)

# Can set an infinite loop
# i = 0
# while True:
#     i += 1
#     print(i)

# manually break a while loop with break
i = 0
while True:
    i += 1
    print(i)
    if i > 100:
        break

