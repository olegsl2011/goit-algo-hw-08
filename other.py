import itertools


def cost_of_sequential_joining(cables_lengths):
    
    joints = []
    for i in range(len(cables_lengths)):
        joints.append((cables_lengths[i], (cables_lengths[i],)))

    log = []
    cost = 0

    while len(joints) > 1:
        first_cable = joints[0]
        second_cable = joints[1]
        joint_cable_indexes = first_cable[1] + second_cable[1]
        joint_cable_length = first_cable[0] + second_cable[0]
        joint_cable_log_record = (first_cable[1], second_cable[1])
        new_joint = (joint_cable_length, joint_cable_indexes)
        cost += new_joint[0]
        joints = joints[2:]
        joints.insert(0, new_joint)
        log.append(list(joint_cable_log_record))

    return {"order": log, "cost": cost}


def min_cost_of_sequential_joining(cables_lengths):
    perm_cables_lengths_set = list(itertools.permutations(cables_lengths))

    result = cost_of_sequential_joining(perm_cables_lengths_set[0])

    for perm_cables_lengths in perm_cables_lengths_set:
        perm_result = cost_of_sequential_joining(perm_cables_lengths)
        if perm_result["cost"] < result["cost"]:
            result = perm_result

    return result


def cost_of_paired_joining(cables_lengths):
    joints = []
    for i in range(len(cables_lengths)):
        joints.append((cables_lengths[i], (cables_lengths[i],)))

    log = []
    cost = 0

    while len(joints) > 1:
        new_joints = []

        for i in range(0, len(joints) - 1, 2):
            first_cable = joints[i]
            second_cable = joints[i + 1]
            joint_cable_indexes = first_cable[1] + second_cable[1]
            joint_cable_length = first_cable[0] + second_cable[0]
            joint_cable_log_record = (first_cable[1], second_cable[1])
            new_joint = (joint_cable_length, joint_cable_indexes)
            cost += new_joint[0]
            new_joints.append(new_joint)
            log.append(list(joint_cable_log_record))

        if len(joints) % 2 == 1:
            new_joints.append(joints[-1])

        joints = new_joints

    return {"order": log, "cost": cost}


def min_cost_of_paired_joining(cables_lengths):
    perm_cables_lengths_set = list(itertools.permutations(cables_lengths))

    result = cost_of_paired_joining(perm_cables_lengths_set[0])

    for perm_cables_lengths in perm_cables_lengths_set:
        perm_result = cost_of_paired_joining(perm_cables_lengths)
        if perm_result["cost"] < result["cost"]:
            result = perm_result

    return result


def cost_of_shortest_first_joining(cables_lengths):
    joints = []
    for i in range(len(cables_lengths)):
        joints.append((cables_lengths[i], (cables_lengths[i],)))

    log = []
    cost = 0

    while len(joints) > 1:
        joints = sorted(joints, key=lambda x: x[0])
        first_cable = joints[0]
        second_cable = joints[1]
        joint_cable_indexes = first_cable[1] + second_cable[1]
        joint_cable_length = first_cable[0] + second_cable[0]
        joint_cable_log_record = (first_cable[1], second_cable[1])
        new_joint = (joint_cable_length, joint_cable_indexes)
        cost += new_joint[0]
        joints = joints[2:]
        joints.insert(0, new_joint)
        log.append(list(joint_cable_log_record))

    return {"order": log, "cost": cost}
