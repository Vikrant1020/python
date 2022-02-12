def password():
	a=input("Enter X to Exit\nEnter Passward:")
	if "x" in a:
		print("Bhag yaha s")
	elif "Ankur" in a:
		print("Welcome Home")
		b=input("What you like to do with us.")
		if "games" in b:
			print("Not , but sorry we don't do that heare")
			print("anythink else")
			c=input("press Y/N")
			if "y" in c:
				print("Tare baap ka noker ne lg raha m.")
				import skull
			else:
				print("Thanks")
		else:
			print("Not available \nOnly the gamer's hear.")
	else:
		print("Wrong Passward.\nTry Again")
		password()


password()