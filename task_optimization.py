"""
A worker has a set of N tasks to complete. For each task the worker knows the
time in minutes it will take to complete. This is dependent on the difficulty of
the task. So, a task with difficulty D takes D minutes to complete. The worker
has a limited amount of time T during which he wants to complete as many tasks
as possible.

As mentioned above the tasks have different difficulty and when switching from
one task to another with difficulties D1 and D2, the worker needs |D1 - D2|
minutes to prepare for working on the next task.

The number of tasks N is in the range [1, 10,000]. The total time T is in the
range [0, 200,000,000]. The task difficulties are integer numbers in the range
[1, 10,000].

You need to write a function, which computes the maximum number of tasks that
can be completed within the given time T. The function accepts as arguments the
number N and T and a list of the task difficulties. It must return one integer -
the maximum number of tasks that can be completed within the given time limit.

Here is an example test case.

SAMPLE INPUT
N = 5 [1..10K]  T = 65 [1..200M]
Task Difficulties = 24 23 22 10 20 [1..10K]

SAMPLE OUTPUT
3

All five tasks cannot be completed within the allowed 65 minutes, but it is
possible to accomplish three tasks, for example tasks 4, 5, 3 if completed in
this order.

# Algorithm

1. sort the task difficulty queue - O(N log n) O(n) space
10 20 22 23 24

2. run a simple arithmetic operation on the array and return the max task count

"""

import time
start_time = time.time()

def task_optimization(num_tasks, max_time, task_list):
    # Sort task_list (use built in sort or implement my own sort)
    merge_sort(task_list, 0, num_tasks - 1) # Time - O(N Log N); Space - O(N)

    # Loop through sorted list and do a running sum (<=max_time) and return the
    # max count    
    max_task_count = get_max_task_count(task_list, max_time)

    return max_task_count


def merge_sort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        aux = merge_sublists(array, start, mid, mid + 1, end)
        array[start : end+1] = aux

def merge_sublists(array, start1, end1, start2, end2):
    aux = []

    while True:
        if array[start1] > array[start2]:
            aux.append(array[start2])
            start2 += 1
        else:
            aux.append(array[start1])
            start1 += 1

        if (start1 > end1):
            aux += array[start2 : end2+1]
            break
        if (start2 > end2):
            aux += array[start1 : end1+1]
            break

    return aux

def get_max_task_count(task_list, max_time):
    max_task_count = 0
    running_sum_time = 0
    for index, current_task_time in enumerate(task_list):
        if index == 0:
            prev_index = 0
        else:
            prev_index = index - 1

        running_sum_time += abs(task_list[prev_index] - current_task_time) + current_task_time

        if running_sum_time > max_time:
            break

        max_task_count += 1
    return max_task_count

task_list = [24, 23, 22, 10, 20]
print(task_optimization(5, 65, task_list))


print(f"--- Time in seconds: {time.time() - start_time} ----")