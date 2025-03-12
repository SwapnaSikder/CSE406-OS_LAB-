def fcfs_disk_scheduling(requests, head):
    total_seek_time = 0
    current_position = head

    for request in requests:
        total_seek_time += abs(request - current_position)
        current_position = request

    return total_seek_time


request_sequence = [176, 79, 41, 11]
initial_head = 50

seek_time = fcfs_disk_scheduling(request_sequence, initial_head)

print("Total Seek Time:", seek_time)
