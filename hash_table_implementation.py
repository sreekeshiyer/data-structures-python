import random


def display_hash_table(hashTable) -> None:
    """
    Printing the Hash Map
    """
    for i in range(len(hashTable)):
        print(i+1, end=" ")

        for j in hashTable[i]:

            print("-->", end=" ")
            print(j[0], end=" ")

        print()


# Creating a Hashtable as a nested list
HashTable = [[] for _ in range(10)]


def hashedKey(keyvalue, arr):
    return((keyvalue * keyvalue) % len(arr))


def insert(hashTable, key, value):
    """
    Inserting a Key value pair into a Hash Map
    """
    hashed_key = hashedKey(key, HashTable)

    # Trying to avoid hash collisions
    empty_spaces = []

    for i in range(len(hashTable)):
        if len(hashTable[i]) == 0:
            empty_spaces.append(i)

    if len(empty_spaces) > 0:
        hashTable[random.choice(empty_spaces)].append([
            value, key])
        return

    hashTable[hashed_key].append([value, key])


insert(HashTable, 319, "Virender Sehwag")
insert(HashTable, 301, "Karun Nair")
insert(HashTable, 281, "VVS Laxman")
insert(HashTable, 270, "Rahul Dravid")
insert(HashTable, 254, "Virat Kohli")
insert(HashTable, 248, "Sachin Tendulkar")
insert(HashTable, 243, "Mayank Agarwal")
insert(HashTable, 239, "Saurav Ganguly")

display_hash_table(HashTable)
