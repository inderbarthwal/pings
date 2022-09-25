import os


OS_TYPE = os.name
count = '-n' if OS_TYPE == 'nt' else '-c'

with open("D:\ip_list.txt") as file:
    ip_add= file.read()
    ip_add = ip_add.splitlines()

def ping_device(ip_add):

    results_file = open("results.txt", "w")
    for ip in ip_add:
        response = os.popen(f"ping {ip} {count} 3").read()

        if "Received = 3" in response:
            pass
        else:
            results_file.write(ip + "\n")
    results_file.close()

ping_device(ip_add)
