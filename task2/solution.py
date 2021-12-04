def main():
    data = read_data()
    print("Solution Task1: ", task1(data))
    print("Solution Task2: ", task2(data))

def task2(data):
    forward = 0
    depth = 0
    aim = 0
    for command in data:
        if command[0] == "forward":
            forward += command[1]
            depth += command[1] * aim
        elif command[0] == "down":
            aim += command[1]
        else:
            aim -= command[1]
    return forward * depth

def task1(data):
    forward = 0
    downward = 0
    for command in data:
        if command[0] == "forward":
            forward += command[1]
        elif command[0] == "down":
            downward += command[1]
        else:
            downward -= command[1]
    return forward * downward

def read_data():
    with open('input.txt') as file:
        input = file.read().splitlines()

    input = [x.split(" ") for x in input]
    input = [[x[0], int(x[1])] for x in input]
    
    return input
    
if __name__ == "__main__":
    main()