# write a python program to enter names of 3 movies and store them in a list

movieDB = []
for i in range(3):
    movieName = input("Enter the name of the movie\n")
    movieDB.append(movieName)

print("This is the list of the movie you entered")
print(movieDB)
