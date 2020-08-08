"""
Cover the Border

Air traffic control of one country wants to check how well its radars are
covering the border. There are plenty of radars each covering one contiguous
strip of the border. Some radars' coverage strips overlap. Because of the
numerous overlaps it is hard for the air traffic control managers to compute the
exact length of the border that is covered. This will be your task.

The strip is represented as a line, which is L meters long.

For each radar we know the left and right end of its coverage strip relative to
the left end of the border. Hence, all such coverage strips will begin and end
somewhere in the range [0, L], which means they fall completely within the
border. They will also have an integer length of at least 1.

You will have to write a function, which receives as arguments L and a list of
pairs of integers - the radar coverage strips ends. Your function must return
one integer - the total area of the border that is covered by at least one
radar, in meters.

You can assume that 1 <= L <= 10^9 and there will be no more than 1,000 radars.

SAMPLE INPUT
L = 100
radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]

SAMPLE OUTPUT
77

L 0, 1, 2, 3, 5....100

Radar [5, 10], [3, 25], [46, 99], [39, 40], [45, 50]

Sort the radar list: [3, 25] [5, 10] [39, 40] [45, 50] [46, 99]

is_overlap(list1, list2) == True
    list1 = list1[0], list2[1]
else
    count = list1.length
    new_list = list2
    increment pointer

if done:
    count+ = new_list.length


"""
import time
start_time = time.time()

def cover_the_border(l, radars):
    # Example arguments:
    # l = 100
    # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
    total_radar_coverage = 0

    if len(radars) == 1:
        total_radar_coverage = radars[0][1] - radars[0][0]
        return total_radar_coverage

    radars.sort()
    rdr_idx1 = 0
    rdr_idx2 = 1
    while rdr_idx2 < len(radars):
        if radars_overlap(radars[rdr_idx1], radars[rdr_idx2]):
            radars[rdr_idx1] = [radars[rdr_idx1][0], max(radars[rdr_idx1][1], radars[rdr_idx2][1])]
            rdr_idx2 += 1
        else:
            total_radar_coverage += radars[rdr_idx1][1] - radars[rdr_idx1][0]
            rdr_idx1 = rdr_idx2
            rdr_idx2 += 1


    total_radar_coverage += radars[rdr_idx1][1] - radars[rdr_idx1][0]
    return total_radar_coverage

def radars_overlap(radar1, radar2):
    if radar2[0] >= radar1[0] and radar2[0] <= radar1[1]:
        return True
    else:
        return False


print(cover_the_border(100, [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]))

print(f"----- Total Seconds: {time.time() - start_time} ----")