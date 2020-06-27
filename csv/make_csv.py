import csv
with open('mask.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["image_names", "mask_or_not"])
    for i in range(0, 816):
        if(i >= 407):
            writer.writerow([str(i) + '.jpg', 0])
        else:
            writer.writerow([str(i) + '.jpg', 1])
