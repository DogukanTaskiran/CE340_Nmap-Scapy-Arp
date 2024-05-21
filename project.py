import subprocess

# 1.1
def basic_tcp_syn_scan(target_ip):
    print(f"Performing basic TCP SYN scan on {target_ip}")
    result = subprocess.run(['nmap', '-sS', target_ip], capture_output=True, text=True)
    print(result.stdout)

# 1.2
def service_os_script_scan(target_ip):
    print(f"Performing service detection, OS detection, and script scanning on {target_ip}")
    result = subprocess.run(['nmap', '-A', target_ip], capture_output=True, text=True)
    print(result.stdout)

# 1.3
def all_ports_scan(target_ip):
    print(f"Performing scan on all available ports on {target_ip}")
    result = subprocess.run(['nmap', '-p-', target_ip], capture_output=True, text=True)
    print(result.stdout)



if __name__ == "__main__":

    target_ip = "192.168.1.6"

    #### Part 1 ###
    basic_tcp_syn_scan(target_ip)
    service_os_script_scan(target_ip)
    all_ports_scan(target_ip)

    # 1.4 and 2.1
    # Wireshark filter to check (example) -> ip.src == 192.168.1.7 && ip.dst == 192.168.1.9
    # Capturing all process via Wireshark, then save in .pcapng format

    # 2.2
    # Filter -> tcp, http, dns

    # 2.3 and 2.4 will be in document and also screenshots