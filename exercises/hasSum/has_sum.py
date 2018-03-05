# As per: https://www.youtube.com/watch?v=XKu_SEDAykw

"""
Return wether a list has a pair that adds to a given number, 8 for example:
[1,2,3,9]->False
[1,2,4,4]->True
"""

# When list is ordered
def hasSumOrdered(set_of_numbers, desired):
    lower = 0
    loop = 1
    higher = set_of_numbers[len(set_of_numbers) - loop]
    for lower in set_of_numbers:
        if lower + higher == desired:
            return True
        higher = set_of_numbers[len(set_of_numbers) - loop]
    return False
    
def hasSumUnordered(set_of_numbers, desired):
    set_of_complementaries = [None] * desired
    for value in set_of_numbers:
        if value <= desired:
            complementary = desired - value
            if set_of_complementaries[complementary] is True:
                return True
            set_of_complementaries[complementary] = True
    return False
        
    
list_ko = [1,2,3,9]
list_ok = [1,2,4,4]

print(hasSumOrdered(list_ko, 8))
print(hasSumOrdered(list_ok, 8))


print(hasSumUnordered(list_ko, 8))
print(hasSumUnordered(list_ok, 8))