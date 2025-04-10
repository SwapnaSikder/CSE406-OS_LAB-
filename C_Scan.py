def cscan(requests, head, disk_size=200):
    requests.sort()
    total = 0

    right = [r for r in requests if r >= head]
    left = [r for r in requests if r < head]

    for r in right:
        total += abs(head - r)
        head = r

    total += (disk_size - 1 - head) + (disk_size - 1)  # jump to 0
    head = 0

    for r in left:
        total += abs(head - r)
        head = r

    return total

# Example usage
reqs = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
start = 53
print("Total number of seek operations:", cscan(reqs, start))
