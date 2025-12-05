temp = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("2024\Day1\data.txt") as file:
    data = file.read() 
    list1 = []
    list2 = []
    for line in data.split('\n'):
       ele1,ele2 =  line.strip().split()
       list1.append(int(ele1))
       list2.append(int(ele2))

    list1.sort()
    list2.sort()

    total_distance = 0
    for ele1,ele2 in zip(list1,list2):
        total_distance += abs(ele1-ele2)
    print(f"{total_distance=}")

    similarity_score = 0
    for ele in list1:
        similarity_score += ele *list2.count(ele)
    print(f"{similarity_score=}")
