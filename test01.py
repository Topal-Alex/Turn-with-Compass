def direction(facing: str, turn: int) -> str:
    degrees = {"N": 0, "NE": 45, "E": 90, "SE": 135,
               "S": 180, "SW": 225, "W": 270, "NW": 315}

    direction = {0: "N", 45: "NE", 90: "E", 135: "SE",
                 180: "S", 225: "SW", 270: "W", 315: "NW"}

    degree = degrees[facing]
    degree += turn
    degree %= 360

    return direction[degree]





