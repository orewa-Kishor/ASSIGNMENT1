data = input("enter first line : ")

# Writing data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("meri bandi hai chubby \n")
    file.write("she have 2 big soft clouds on her chest \n")


# Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal Content of File:")
    print(file.read())