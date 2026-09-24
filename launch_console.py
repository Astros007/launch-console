print("Welcome to Sahisnu's Launch Console!")

name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

while True:
    print("\n--- Launch Console ---")
    print("1. About me")
    print("2. My goals")
    print("3. Favorite project")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("I'm Sahisnu Adhikari, and I'm interested in engineering, technology, and building fun games.")

    elif choice == "2":
        print("My goals are to improve my coding skills and create projects that make other people happy through my games.")

    elif choice == "3":
        print("One project I enjoy working on is building a video game on Roblox")

    elif choice == "4":
        print("Goodbye, " + name + "! Thanks for using my Launch Console.")
        break

    else:
        print("Please enter a number from 1 to 4.")
