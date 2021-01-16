# Create a Python list to store your grocery list
grocery_list=["Milk",1,"Eggs",12 ,"Cheese",2 ,"Jelly",1,"Chips",3,"Peanut Butter",1]

# Print the grocery list
print(grocery_list)


# Change "Peanut Butter" to "Almond Butter" and print out the updated list
indx=grocery_list.index("Peanut Butter")
grocery_list.pop(indx)
grocery_list.insert(indx, "Almond Butter")
print(grocery_list)
# Remove "Jelly" from grocery list and print out the updated list
grocery_list.remove("Jelly")
print(grocery_list)
# Add "Coffee" to grocery list and print the updated list
grocery_list.append("Coffee")
print(grocery_list)