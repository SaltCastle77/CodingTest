def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam = routes[0][1]
    answer += 1

    for i in range(1, len(routes)):
        if routes[i][0] > cam:
            cam = routes[i][1]
            answer += 1

    return answer