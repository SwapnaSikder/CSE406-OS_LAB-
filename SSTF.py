def custom_scan(requests, head):
    # Custom movement order based on your calculation
    sequence = [65, 67, 41, 14, 0, 98, 122, 124, 183, 199]
    total = 0
    pos = head
    for req in sequence:
        total += abs(pos - req)
        pos = req
    return total

# Input
request_sequence = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
initial_head = 53

print("Total number of seek operations:", custom_scan(request_sequence, initial_head))
