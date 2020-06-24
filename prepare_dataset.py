import os
import csv

cat = []
dog = []
# Finding the directory of the images
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        # Example file name: cat.01.jpg
        for i, filename in enumerate(os.listdir(dirname)):
            # Splitting the name of the image and labelling accordingly
            category = filename.split(".")[0]
            if category == "cat":
                cat.append((filename, 0))
            if category == "dog":
                dog.append((filename, 1))

# Writing the names and the category to the csv file
with open('train.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cat)
    writer.writerows(dog)
