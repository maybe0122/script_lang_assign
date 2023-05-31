def solution(id_list, report, k):
    # dict 생성 및 초기화 중복된 id가 없으니까 이렇게 만들어도 될듯
    # dict 말고 list로 하고 중복 제거하고 그냥 출력하는게 쉬을듯

    D = dict()
    answer = [0 for _ in range(len(id_list))]

    for i in range(len(id_list)):
        D[id_list[i]] = [0, []] # 신고 받은 횟수, 누가 신고했는가

    # 신고 받은 횟수
    for i in set(report): # set 하면 정렬된다. 안에서 자르자.
        i = i.split()
        for j in range(len(id_list)):
            if i[1] == id_list[j]:
                D[id_list[j]][0] += 1 # 신고 받은 횟수 증가
                D[id_list[j]][1].append(i[0]) # 누가 신고했는지 추가

    for i in range(len(id_list)):
        print("i =", i)
        print(type(D[id_list[i]][0]))
        if D[id_list[i]][0] >= k: # 신고 받은 횟수가 k번을 넘어간다면
            print("IN")
            print(i, D[id_list[i]][0])
            for j in D[id_list[i]][1]:
                # print(j)
                for a in range(len(id_list)):
                    if id_list[a] == j:
                        # print(id_list[k], j)
                        answer[a] += 1

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)