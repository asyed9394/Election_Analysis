# How many votes did you get?
my_votes=int(input("How many votes did you get in the election?"))
# Total votes casted in the election
total_votes=int(input("What is the total votes casted in the election?"))
percentage_votes=(my_votes/total_votes )*100
print(f"I received {percentage_votes}% of total vots {total_votes}")