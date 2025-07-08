#!/usr/bin/python3
counter = 0
for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            print(f"{i}{j}", end="")
            if counter < 44:
                print(", ", end="")
                counter += 1
print("\n", end="")
