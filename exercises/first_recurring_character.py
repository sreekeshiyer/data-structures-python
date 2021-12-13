array = [2, 5, 4, 2, 3, 5, 1, 2, 4]
# array = [2, 3, 4, 5]


def find_recurring_character() -> int:
    '''
    Finding the first Recurring Character (buggy) in a list. 
    Complexity O(n^2)
    '''

    for i in range(len(array)):

        if array[i] in array[i+1:]:
            return array[i]
        if i == len(array)-1:
            return None


def find_recurring_character2() -> int:
    '''
    Finding the first Recurring Character in a list using HASH MAPS. 
    Complexity *O(n)*
    '''

    myHashTable = {}
    for number in array:
        try:
            if myHashTable[number]:
                return number
            else:
                myHashTable[number] = number
        except:
            myHashTable[number] = number
            continue


# print(find_recurring_character2())
print(find_recurring_character())
