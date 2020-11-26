import csv
import numpy as np
import math

correct = 0

# Put the filepath for the csv file here

file_path =

with open(file_path, mode='r')as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        n, a = lines

        n = int(n)
        a = int(a)

        R_original = np.arange(n)
        R_modified = np.mod(a * R_original, n)

        if len(set(R_modified)) == n / math.gcd(n, a):
            correct += 1

print(correct)