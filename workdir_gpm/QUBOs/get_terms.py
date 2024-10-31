import ast

# Load the .txt file
with open('new_qubo_0', 'r') as file:
    content = file.read()

# Convert the content to a dictionary
data_dict = ast.literal_eval(content)

# Initialize the lists
linear = []
quadratic = []

keys = list(data_dict.keys())

# Populate the lists based on the keys
for key in keys:
    if key[0] == key[1]:
        linear.append(data_dict[key])
    else:
        quadratic.append(data_dict[key])

    # with open('lists.txt', 'w') as newlist:
    #     newlist.write(str(linear))

# Print the lists and their lengths
#print("Linear List:", linear)
print("Length of Linear List:", len(linear))
print(linear[0:10])
#print("Quadratic List:", quadratic)
print("Length of Quadratic List:", len(quadratic))
print(quadratic[0:10])

