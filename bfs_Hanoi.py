from bfs import bfs_travesal, predicate_finder

class Hanoi:
    def __init__(self, roots, num_disks):
        self._roots = [HanoiConfiguration(roots)]
        self._num_disks = num_disks
    
    def roots(self):
        return self._roots
    
    def neighbors(self, aHanoiConfiguration):
        neighborsList = []
        # Determine the top disk on each peg
        pegs = {0: [], 1: [], 2: []}
        for disk in reversed(range(self._num_disks)):
            peg = aHanoiConfiguration.pegs[disk]
            pegs[peg].append(disk)
        # For each peg, try to move its top disk to another peg
        for from_peg in range(3):
            if not pegs[from_peg]:
                continue
            disk_to_move = pegs[from_peg][-1]
            for to_peg in range(3):
                if from_peg == to_peg:
                    continue
                if not pegs[to_peg] or disk_to_move < pegs[to_peg][-1]:
                    new_pegs = list(aHanoiConfiguration.pegs)
                    new_pegs[disk_to_move] = to_peg
                    newHanoiConfiguration = HanoiConfiguration(new_pegs)
                    neighborsList.append(newHanoiConfiguration)

        return neighborsList

        

class HanoiConfiguration:
    def __init__(self, pegs):
        self.pegs = tuple(pegs)
    
    def __eq__(self, other):
        if not isinstance(other, HanoiConfiguration):
            return False
        return self.pegs == other.pegs

    def __hash__(self):
        return 1
    
    def __repr__(self):
        return f"HanoiConfiguration(pegs={self.pegs})"

# Example usage with Hanoi
# Let's define a simple Hanoi puzzle with 2 disks starting on peg 0
initial_roots = [0, 0, 0]  # Disk 0 and Disk 1 are on peg 0
num_disks = 3
hanoi_graph = Hanoi(initial_roots, num_disks)

parentTracer = ParentTracer(hanoi_graph)


# Define a predicate to find the configuration where all disks are on peg 2
def is_goal(config):
    return all(peg == 2 for peg in config.pegs)

print("Hanoi predicate finder result:")
result = predicate_finder(hanoi_graph, is_goal)
print("Opaque:", result[0])  # [bool, count, n]
print("Visited Nodes:", result[1])