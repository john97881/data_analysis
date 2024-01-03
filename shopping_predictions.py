import random
from itertools import combinations

carthistory = [["chips", "fried chicken", "soda", "candy bar", "energy drink"],
               ["chips", "soda", "candy bar"],
               ["chips", "soda"],
               ["soda", "candy bar", "energy drink"],
               ["fried chicken", "candy bar"],
               ["candy bar", "energy drink"],
               ["fried chicken", "soda", "candy bar", "energy drink"],
               ["soda"],
               ["chips", "fried chicken", "soda", "candy bar"],
               ["soda", "candy bar"]]

#Task1: Count instances of each object and coexistence
item_counts = {item: sum(item in cart for cart in carthistory) for item in set(item for cart in carthistory for item in cart)}
coexistence_counts = {combo: sum(all(item in cart for item in combo) for cart in carthistory) for combo in combinations(item_counts.keys(), 2)}

#Display counts
print("Item Counts:")
print(item_counts)

print("\nCoexistence Counts:")
print(coexistence_counts)

#Task2: Generate random carthistory
unique_items = list(item_counts.keys())
random_carthistory = [random.sample(unique_items, random.randint(1, 5)) for _ in range(10)]

print("\nRandomly Generated Cart History:")
print(random_carthistory)

#Task3: Automate the itemslist
automated_itemslist = list(item_counts.keys())

print("\nAutomated Itemslist:")
print(automated_itemslist)

def get_item_count(item):
    return item_counts.get(item, 0)
chips_count = get_item_count("chips")
soda_count = get_item_count("soda")

print(f"\nNumber of 'chips': {chips_count}")
print(f"Number of 'soda': {soda_count}")

