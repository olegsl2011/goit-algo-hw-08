import heapq

from other import *


def heap_min_cost_of_joining(cables_lengths):
    
    if len(cables_lengths) < 2:
        return {"order": [], "cost": 0}

    if len(set(cables_lengths)) != len(cables_lengths):
        raise ValueError("Cables lengths must be unique")

    joints = []
    for i in range(len(cables_lengths)):
        joints.append((cables_lengths[i], (cables_lengths[i],)))

    queue = []

    for joint in joints:
        heapq.heappush(queue, joint)

    log = []
    cost = 0

    while len(queue) > 1:
        first_cable = heapq.heappop(queue)
        second_cable = heapq.heappop(queue)
        joint_cable_indexes = first_cable[1] + second_cable[1]
        joint_cable_length = first_cable[0] + second_cable[0]
        joint_cable_log_record = (first_cable[1], second_cable[1])
        new_joint = (joint_cable_length, joint_cable_indexes)
        cost += new_joint[0]
        heapq.heappush(queue, new_joint)
        joints.insert(0, new_joint)
        log.append(list(joint_cable_log_record))

    return {"order": log, "cost": cost}


def main():
    cables_lengths = [73, 61, 45, 31, 23]

    print("Cables lengths:", cables_lengths)

    print("\nSequential joints minimum:")
    print(min_cost_of_sequential_joining(cables_lengths))

    print("\nPaired joints minimum:")
    print(min_cost_of_paired_joining(cables_lengths))

    print("\nShortest first joints:")
    print(cost_of_shortest_first_joining(cables_lengths))

    print("\nMin cost of joints calculated by heap:")
    print(heap_min_cost_of_joining(cables_lengths))


if __name__ == "__main__":
    main()
