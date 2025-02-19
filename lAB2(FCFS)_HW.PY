data=[]
process_no= int(input("Enter the number of processes:"))
for _ in range(process_no):
    processID=input("Enter Process ID:")
    arrival=int(input("Enter Arrival Time:"))
    burst=int(input("Enter Burst Time:"))

    data.append({"process":processID,"arrival":arrival,"burst":burst})

    data.sort(key=lambda p: p['arrival'])

    cpu_time=0

for process in data:
    cpu_time= max(cpu_time, process['arrival'])
    process['CT']=cpu_time + process['burst']
    process['TAT']= process['CT']- process['arrival']
    process['WT']= process['TAT']-process['burst']
    cpu_time=  process['CT']

print("\nP | A | B | CT | TAT | WT ")
print("_" *26)
for p in data:
    print(f"{p['process']:<3} | {p['arrival']:<2} | {p['burst']:<2} | {p['CT']:<2} | {p['TAT']:<3} | {p['WT']:<2}")