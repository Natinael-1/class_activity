fruits = ["Avocado", "Mango", "Pineapple", "Lemon", "Orange", "Banana"]
print(fruits[0], fruits[5])

new_fruit = input("Please tell me another fruit: ")
fruits.append(new_fruit)
print(fruits)
i = 0
while i < len(fruits):
    print(f"{fruits[i]} , {i}")
    i = i + 1


