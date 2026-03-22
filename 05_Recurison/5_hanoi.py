# Tower of Hanoi (important 🔥)

# The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective is to move the entire stack of disks from one rod to another, following these rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a smaller disk.
# The minimum number of moves required to solve the Tower of Hanoi puzzle is 2^n - 1, where n is the number of disks.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
n = 3  # Number of disks 
tower_of_hanoi(n, 'A', 'C', 'B')  # A is the source rod, C is the target rod, B is the auxiliary rod
