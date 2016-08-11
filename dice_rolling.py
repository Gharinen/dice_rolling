import random
min=1
max=6

roll_again= "yes"

while roll_again == "yes":
	number= random.randint(min,max)
	print "Rolling the dices...."
	print "Let's see what it is!"
	print "It's a %d" %(number)
	
	roll_again= raw_input("Wanna roll again... yes or no? ")
