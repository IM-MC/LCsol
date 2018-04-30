def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    steps = [0,0]
    dict = {
        "L":[-1,0],
        "R":[1,0],
        "U":[0,1],
        "D":[0,-1]
    }

    for direction in moves:
        steps[0] += dict[direction][0]
        steps[1] += dict[direction][1]

    return True if steps[0] == 0 and steps[1] == 0 else False
