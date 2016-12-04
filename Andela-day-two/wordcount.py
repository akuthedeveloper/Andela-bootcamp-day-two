def words(phrase):
    # instantiate a collection of words
    collection = {}
    # loop to check if there is any integer
    for i in phrase.split():
        if i.isdigit():
            word=int(i)
            if collection.get(word):
                collection[word] += 1
            else:
                collection[word] = 1
        else:
            if collection.get(i):
                collection[i] += 1
            else:
                collection[i] = 1
            return collection
            # print statement to check variables
print words('olly olly in come free')
print(29)
