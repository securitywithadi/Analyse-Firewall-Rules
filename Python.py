firewall_dict = {}
with open("Sample_Content.txt") as file:
    for line in file:
        ip, port = line.strip().split(":")
        firewall_dict.setdefault(ip, []).append(int(port))

print(firewall_dict)
