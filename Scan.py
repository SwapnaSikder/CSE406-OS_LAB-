def scan_disk_scheduling(requests, head, direction, disk_size):
    requests.sort()
    seek_sequence = []
    seek_count = 0
    left = [i for i in requests if i < head]
    right = [i for i in requests if i >= head]

    if direction == "left":
        # Move left first
        for i in reversed(left):
            seek_sequence.append(i)
            seek_count += abs(head - i)
            head = i
        # Then move to beginning (if not already there)
        if left:
            seek_count += head  # move to 0
            head = 0
        # Then move right
        for i in right:
            seek_sequence.append(i)
            seek_count += abs(head - i)
            head = i
    elif direction == "right":
        # Move right first
        for i in right:
            seek_sequence.append(i)
            seek_count += abs(head - i)
            head = i
        # Then move to end
        if right:
            seek_count += (disk_size - 1 - head)
            head = disk_size - 1
        # Then move left
        for i in reversed(left):
            seek_sequence.append(i)
            seek_count += abs(head - i)
            head = i

    return seek_sequence, seek_count


# Example input
requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head = 53
direction = "right"
disk_size = 200

sequence, total_seek = scan_disk_scheduling(requests, head, direction, disk_size)

print("Seek Sequence:", sequence)
print("Total number of seek operations::", total_seek)
