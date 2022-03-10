
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(list(student_marks.keys()))
    if query_name in list(student_marks.keys()):
        res=student_marks[query_name]
    print("%.2f"%(sum(res)/len(res)))
