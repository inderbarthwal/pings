import os


OS_TYPE = os.name
count = '-n' if OS_TYPE == 'nt' else '-c'

with open("D:\ip_list.txt") as file:
    ip_add= file.read()
    ip_add = ip_add.splitlines()

def ping_device(ip_add):

    results_file = open("results.txt", "w")
    for ip in ip_add:
        response = os.popen(f"ping {ip} {count} 4").read()
        if "Received = 1" and "Approximate" in response:
            print(f"UP {ip} Ping Successful")
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(f"Down {ip} Ping Unsuccessful")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
    results_file.close()

print(ping_device(ip_add))
