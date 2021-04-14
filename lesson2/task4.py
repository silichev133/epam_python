log_name = "access.log"

ip_counts = {}
with open(log_name) as log:
    for line in log:
        ip_counts[line.split()[0]] += 1

ip_counts = ip_counts.items()
ip_counts = sorted(ip_counts, key=lambda x:x[0]) #I found this lambda code on the Internet

for ip in ip_counts[:10]:
    print("{}: {}".format(ip, ip_counts[ip]))
