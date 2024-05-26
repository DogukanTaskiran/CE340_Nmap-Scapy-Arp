from scapy.all import ICMP, IP, sr1, TCP
import logging
import terminalColors;

logging.basicConfig(filename="log.log", level=logging.INFO)

def logResponse(response):
    if response:
        logging.info(response.show(dump=True))
    else:
        logging.info(f"{terminalColors.TerminalColors.FAIL}No response received{terminalColors.TerminalColors.END}")

def icmpEchoRequest(target):
    packet = IP(dst=target) / ICMP()
    response = sr1(packet, timeout=1)
    logResponse(response)

def tcpSynPacket(target, source, destinationPort):
    packet = IP(src=source, dst=target) / TCP(dport=destinationPort, flags='S')
    response = sr1(packet, timeout=1)
    logResponse(response)

if __name__ == "__main__":
    
    print(f"{terminalColors.TerminalColors.BOLD}Scapy, Part 3...{terminalColors.TerminalColors.END}")
    target = input(f"{terminalColors.TerminalColors.OKGREEN} Enter the target IP address: {terminalColors.TerminalColors.END} ") # 192.168.1.3
    source = input(f"{terminalColors.TerminalColors.OKGREEN} Enter the source IP address: {terminalColors.TerminalColors.END} ") # 192.168.1.100
    destinationPort = int(input(f"{terminalColors.TerminalColors.OKGREEN} Enter the destination port : {terminalColors.TerminalColors.END} ")) # 80 
    
    icmpEchoRequest(target)
    tcpSynPacket(target, source, destinationPort)

