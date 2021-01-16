# Info in Dictionaries

## Instructions

##* Create a dictionary to store the following:
  ##* Your pet's name
  ##* Your pet's age
  ##* A list of a few of your pet's hobbies
  ##* A dictionary of a few times you wake up during the week
aisha_pet=dict()
aisha_pet["pet_name"]="Nina"
aisha_pet["pet_age"]=2
aisha_pet["pet_hobby_list"]=["Running","Eating","Scratching","Playing with Toys"]
aisha_pet["wakeup_times_dict"]={"Saturday":"7:00","Sunday":"8:00","Monday":"9:00","Tuesday":"10:00"}
##* Print out the following:
  ##* Your pet's name and age.
  ##* How many hobbies your pet has.
  ##* What your pet's favorite hobby is.
  ##* What time your pet wakes on one of the days of the week.
print(aisha_pet)
print("Aisha's Pets name is: "+ aisha_pet.get("pet_name"))
pet_age=aisha_pet.get("pet_age")
pet_name=aisha_pet.get("pet_name")
print(f"Aisha's pet {pet_name}'s age is: {pet_age}")
fav_hoby=aisha_pet.get("pet_hobby_list.[2]")
print(f"Aisha's pet {pet_name}'s favorite hobby is {fav_hoby}")
wk_up_time=aisha_pet.get("wakeup_times_dict")
print(wk_up_time)
week_day_tim=wk_up_time.get("Monday")
print(week_day_tim)
print(f"Aisha's pet {pet_name} wakes up on Monday at {week_day_tim}) 
