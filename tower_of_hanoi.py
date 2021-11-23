def tower_of_hanoi_sol(num_disks, source, auxilary, destinamtion):
    if num_disks ==0:
        return
    if num_disks== 1:
        print('{} {}'.format(source, destinamtion))
        return
    tower_of_hanoi_sol(num_disks-1, source, destinamtion, auxilary)
    print('{} {}'.format(source, destinamtion))
    tower_of_hanoi_sol(num_disks-1, auxilary, source, destinamtion)


def tower_of_hanoi(num_disks):
    return tower_of_hanoi_sol(num_disks, 'S', 'A', 'D')


tower_of_hanoi(2)



