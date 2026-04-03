shopping_list = ["apples (3)"]

# Add bananas (2)
shopping_list.append("bananas (2)")

# Insert milk (1 L) at index 1
shopping_list.insert(1, "milk (1 L)")

# Remove bananas (index 2)
del shopping_list[2]

# Party supplies list
party_supplies = ["balloons", "streamers"]

# Combine lists (extend)
shopping_list.extend(party_supplies)

# Add bread (1 Packet) to the end (append)
shopping_list.append("bread (1 Packet)")

# Convert list to tuple (fixed)
shopping_tuple = tuple(shopping_list)

# Convert tuple back to list (modifiable)
shopping_list_again = list(shopping_tuple)

print("Shopping List:", shopping_list)
print("Shopping Tuple (fixed):", shopping_tuple)
print("Shopping List (from tuple):", shopping_list_again)