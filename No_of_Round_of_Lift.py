def number_of_rounds(people, capacity):
    full_rounds = people // capacity
    leftover = people % capacity

    if leftover == 0:
        return full_rounds
    else:
        return full_rounds + 1


people = int(input("Enter number of people: "))
capacity = int(input("Enter lift capacity: "))

result = number_of_rounds(people, capacity)
print("Number of rounds needed:", result) 
