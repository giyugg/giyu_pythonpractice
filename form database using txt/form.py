import os

# Function to generate a unique filename
def get_new_filename(base_name="inputs", extension=".txt"):
    i = 1
    new_filename = f"{base_name}{extension}"
    while os.path.exists(new_filename):
        i += 1
        new_filename = f"{base_name}{i}{extension}"
    return new_filename

# Get a new file name
filename = get_new_filename()

# Writing to the new file
with open(filename, "w") as file:
    while True:
        user_input = input("Enter some text (or press enter to stop): ")
        if user_input == "":
            break
        file.write(user_input + "\n")

print(f"Data written to {filename}")
