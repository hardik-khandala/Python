def selectionSort(List):
    for i in range(len(List) - 1):
        min = i
        for j in range(i + 1, len(List)):
            if List[j] < List[min]:
                min = j
        if min != i:
            List[i], List[min] = List[min], List[i]
    return List

list=[4,2,6,8,1,3,5,7,9]
print("Sorted list is:", selectionSort(list))
