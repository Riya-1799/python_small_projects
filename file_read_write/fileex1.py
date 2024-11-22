
#poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python
# program and find out words with maximum occurance.

wordsfile= {}

with open("poem.txt","r") as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in wordsfile:
                wordsfile[word] +=1
            else:
                wordsfile[word]=1

print(wordsfile)
