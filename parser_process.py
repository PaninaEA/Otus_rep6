import subprocess
from collections import defaultdict
from datetime import datetime

process = subprocess.Popen(
    ["ps", "aux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
output, error = process.communicate()
lines = output.strip().split("\n")
count_of_processes = len(lines) - 1
count_of_user_processes = defaultdict(int)
sum_memory = 0.0
sum_cpu = 0.0
max_memory = 0.0
max_cpu = 0.0
for line in lines[1:]:
    columns = line.split()
    user = columns[0]
    pid = columns[1]
    cpu = float(columns[2])
    mem = float(columns[3])
    command = columns[10]
    count_of_user_processes[user] += 1
    sum_memory += mem
    if mem > max_memory:
        max_memory = mem
        max_memory_command = command[:20]
    sum_cpu += cpu
    if cpu > max_cpu:
        max_cpu = cpu
        max_cpu_command = command[:20]
print("Отчёт о состоянии системы:")
print(f"Пользователи системы: {', '.join(count_of_user_processes.keys())}")
print(f"Процессов запущено: {count_of_processes}")
print("\nПользовательских процессов:")
for user, count in count_of_user_processes.items():
    print(f"{user}: {count}")
print(f"\nВсего памяти используется: {sum_memory}%")
print(f"Всего CPU используется: {sum_cpu}%")
print(f"Больше всего памяти использует: {max_memory_command}")
print(f"Больше всего CPU использует: {max_cpu_command}")

filename = f"{datetime.now().strftime('%d-%m-%Y-%H:%M')}-scan.txt"
with open(filename, "w") as f:
    f.write("Отчёт о состоянии системы:\n")
    f.write(f"Пользователи системы: {', '.join(count_of_user_processes.keys())}\n")
    f.write(f"Процессов запущено: {count_of_processes}\n")
    f.write("\nПользовательских процессов:\n")
    for user, count in count_of_user_processes.items():
        f.write(f"{user}: {count}\n")
    f.write(f"\nВсего памяти используется: {sum_memory}%\n")
    f.write(f"Всего CPU используется: {sum_cpu}%\n")
    f.write(f"Больше всего памяти использует: {max_memory_command}\n")
    f.write(f"Больше всего CPU использует: {max_cpu_command}")