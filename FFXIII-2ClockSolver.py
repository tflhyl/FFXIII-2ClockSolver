CLOCK_SIZE = 12

def get_input():
    input = raw_input("Enter clocks (12 values from top-most clockwise): ").strip()
    if len(input) != CLOCK_SIZE*2 - 1:
        print 'Invalid size!'
        return None
    else:
        return input.split(" ")     

#idx - index of current node
#val - value of current node    
#d - direction (1 clockwise, -1 anticlockwise)
def solve(clock, solution, idx, val, d):
    new = (idx + d*val)%CLOCK_SIZE
    if new in solution:
        return 0
    solution.append(new)

    if len(solution) == CLOCK_SIZE:
        return 1
    else:
        if solve(clock, solution, new, clock[new], 1) == 0:
            if solve(clock, solution, new, clock[new], -1) == 0:
                solution.pop()
                return 0
    return 1
    

def main():
    clock = get_input()
    
    if clock == None:
        return None

    try:
        clock = map(int, clock)
    except ValueError:
        print 'Invalid clock!'
        return None
    
    solution = []
    for x in range(0, CLOCK_SIZE):
        solution.append(x)
        if solve(clock, solution, x, clock[x], 1) == 0:
            if solve(clock, solution, x, clock[x], -1) == 0:
                solution.pop()
            else:
                break
        else:
            break
    if len(solution) == 0:
        print 'Clock cannot be solved!'
    else:
        print solution
                 

if __name__ == "__main__":
    main()
