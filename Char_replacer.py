
#Simple for loop to replace a char for other in a string
phrase = "A bird in the hand..."

for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,
