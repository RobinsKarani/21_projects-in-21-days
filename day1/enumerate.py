fruits = ["apple", "banana", "cherry"]

# for index,fruit in enumerate(fruits):
#     print(f"Index {index} Fruit: {fruit}")
    
    # You can tell enumerate to start counting from 1 (or any number you like) using the start parameter.   
for index, fruit in enumerate(fruits, start=0):
        print(f"Index: {index}, Fruit: {fruit}")


