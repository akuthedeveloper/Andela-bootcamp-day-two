def find_max_min(numbers):
    # if condition for minimum and maximum numbers and returns length
    if min(numbers) == max(numbers):
        return [len(numbers)]
# returns the array of two element if the array are not the same
    else:
        return [min(numbers), max(numbers)]
    # print statement
print find_max_min([7,7,7,7,7])
