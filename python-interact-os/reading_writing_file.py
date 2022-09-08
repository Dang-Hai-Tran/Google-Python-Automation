initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
with open("./guests.txt", "a") as guests:
	for index, guest in enumerate(initial_guests):
		guests.write(f"{index + 1}. {guest}\n")

