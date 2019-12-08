#Part 1 Question 2.1 - Join Lists in O(n^2)

#-----------------------------------------------------------------------


def insertion_sort(unsortedList):
    for slot in range(1, len(unsortedList)):
        value = unsortedList[slot]
        test_slot = slot - 1
        while test_slot > -1 and unsortedList[test_slot] > value:
            unsortedList[test_slot + 1] = unsortedList[test_slot]
            test_slot = test_slot - 1
        unsortedList[test_slot + 1] = value
    return unsortedList

def join_lists(unsortedList,sortedList):

    unsortedList=insertion_sort(unsortedList) #sorts the first unsorted list in O(n^2)
    size_1 = len(unsortedList)
    size_2 = len(sortedList)

    joinedList = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if unsortedList[i] < sortedList[j]:
            joinedList.append(unsortedList[i])
            i += 1

        else:
            joinedList.append(sortedList[j])
            j += 1

    joinedList = joinedList + unsortedList[i:] + sortedList[j:]

    return ("The combined sorted list is : " + str(joinedList))

