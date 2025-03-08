def sjf(processes):
    processes.sort(key=lambda x: x[2])

    current_time = 0
    completed_processes = []
    remaining_processes = processes.copy()

    print("\nPID\tBT\tAT\tCT\tTAT\tWT")

    while remaining_processes:

        available = [p for p in remaining_processes if p[2] <= current_time]

        if available:

            shortest = min(available, key=lambda x: x[1])
            remaining_processes.remove(shortest)

            P_id, BT, AT = shortest
            WT = max(current_time - AT, 0)
            TAT = WT + BT
            CT = current_time + BT

            print(f"{P_id}\t{BT}\t{AT}\t{CT}\t{TAT}\t{WT}")

            current_time += BT
        else:
            current_time += 1


process_list = [
    (1, 6, 2),
    (2, 2, 5),
    (3, 8, 1),
    (4, 3, 0),
    (5, 4, 4)
]

sjf(process_list)
