import unittest

def bubbleSort(numList):
    n = len(numList)
    if n == 0:
        return []
    sortedList = numList.copy()
    for dest in range(n-1, -1, -1):
        swapMade = False
        for idx in range(dest):
            if sortedList[idx] > sortedList[idx+1]:
                sortedList[idx], sortedList[idx+1] = sortedList[idx+1], sortedList[idx] 
                swapMade = True
        if not swapMade:
            break

    return sortedList

def mergeSort(numList):
    n = len(numList)
    if n == 0:
        return []
    
    def mergeLists(list1, list2):
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1+=1
            else:
                result.append(list2[p2])
                p2+=1
        if p1 >= len(list1):
            while p2 < len(list2):
                result.append(list2[p2])
                p2+=1
        else:
            while p1 < len(list1):
                result.append(list1[p1])
                p1+=1

        return result

    def mergeRecursion(currList):
        if len(currList) == 1:
            return currList
        left = mergeRecursion(currList[:len(currList)//2])
        right = mergeRecursion(currList[len(currList)//2:])
        return mergeLists(left, right)
    
    

    return mergeRecursion(numList.copy())




class TestSorts(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.simple_list = [1,2,3,4,5]
        self.reverse_list = [10,7,3,2,1]
        self.scrambled_list = [5, 8, 3, 2, 7, 5, 8, 5, 1, 9, 0, -1, -2]

        self.expected1 = []
        self.expected2 = [1,2,3,4,5]
        self.expected3 = [1,2,3,7,10]
        self.expected4 = [-2, -1, 0, 1, 2, 3, 5, 5, 5, 7, 8, 8, 9]

        

    def test_bubblesort(self):
        self.assertListEqual(self.expected1, bubbleSort(self.empty_list))
        self.assertListEqual(self.expected2, bubbleSort(self.simple_list))
        self.assertListEqual(self.expected3, bubbleSort(self.reverse_list))
        self.assertListEqual(self.expected4, bubbleSort(self.scrambled_list))
    
    def test_mergesort(self):
        self.assertListEqual(self.expected1, mergeSort(self.empty_list))
        self.assertListEqual(self.expected2, mergeSort(self.simple_list))
        self.assertListEqual(self.expected3, mergeSort(self.reverse_list))
        self.assertListEqual(self.expected4, mergeSort(self.scrambled_list))

if __name__ == '__main__':
    unittest.main()
