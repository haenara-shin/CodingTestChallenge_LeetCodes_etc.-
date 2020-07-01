import sys

def getDist(points) :
    '''
    n개의 점이 주어질 때, 가장 가까운 두 점 사이의 거리의 제곱을 반환하는 함수를 작성하세요.

    예를 들어, 점이 4개가 있고, 각각의 좌표가 (0, 3), (1, 1), (2, 2), (7, 1) 이라면 points에는 다음과 같이 그 정보가 저장됩니다.

    points = [ (0, 3), (1, 1), (2, 2), (7, 1) ]

    이 때, 가장 가까운 두 점 사이의 거리의 제곱은 2입니다.
    '''
    from itertools import combinations
    d = list(combinations(points, 2))
    result = []
    for i in d:
        n1, n2 = zip(*i)
        x_denominator = (n1[0] - n1[1]) ** 2
        y_nominator = (n2[0] - n2[1]) ** 2
        result.append((y_nominator + x_denominator))
#     print(result)
    return min(result)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print(getDist(points))

if __name__ == "__main__":
    main()


