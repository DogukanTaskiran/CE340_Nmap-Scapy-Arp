import subprocess
import terminalColors 

def nmapScan(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def tcpSyn(target):
    command = f"sudo nmap -sS {target}"
    print(f"{terminalColors.TerminalColors.HEADER}Running basic TCP SYN scan on {target}{terminalColors.TerminalColors.END}")
    result = nmapScan(command)
    print(f"{terminalColors.TerminalColors.OKBLUE}", result , f"{terminalColors.TerminalColors.END}")

def serviceOs(target):
    command = f"sudo nmap -A {target}"
    print(f"{terminalColors.TerminalColors.HEADER}Running service detection, OS detection, and script scan on {target}{terminalColors.TerminalColors.END}")
    result = nmapScan(command)
    print(f"{terminalColors.TerminalColors.OKBLUE}", result , f"{terminalColors.TerminalColors.END}")


def allPorts(target):
    command = f"sudo nmap -p- {target}"
    print(f"{terminalColors.TerminalColors.HEADER}Running scan on all available ports on {target}{terminalColors.TerminalColors.END}")
    result = nmapScan(command)
    print(f"{terminalColors.TerminalColors.OKBLUE}", result , f"{terminalColors.TerminalColors.END}")


if __name__ == "__main__":
    target = input(f"{terminalColors.TerminalColors.OKGREEN}Enter the target IP address:{terminalColors.TerminalColors.END}")

    print(f"{terminalColors.TerminalColors.BOLD}\n1. Basic TCP SYN scan{terminalColors.TerminalColors.END}")
    tcpSyn(target)

    print(f"{terminalColors.TerminalColors.BOLD}\n2. Service detection, OS detection, and script scan{terminalColors.TerminalColors.END}")
    serviceOs(target)

    print(f"{terminalColors.TerminalColors.BOLD}\n3. All ports scan{terminalColors.TerminalColors.END}")
    allPorts(target)
