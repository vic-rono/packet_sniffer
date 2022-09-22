import logging
from datetime import datetime
import subprocess
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

# clears the error messages

# supposed to run on a linux distribution...for example this is intended to run on my docker ubuntu image

try:
    from scapy.all import *

except ImportError:
    print("Scapy package for Python is not installed.")
    sys.exit()

print("\n run  as ROOT !\n")

# Asking the user for input - the interface on which to run the sniffer
net_iface = input("Enter the interface (e.g. 'eth0'): ")

# Setting network interface in promiscuous mode


try:
    subprocess.call(["ifconfig", net_iface, "promisc"], stdout=None, stderr=None, shell=False)

# enables promiscous mode that will allow the network device to intercept (seems wrong) and read each network packet
# going through the CPU
except ValueError:
    print("\nFailed to configure interface as promiscuous.\n")

else:
    # Executed if the try clause does not raise an exception
    print("\nInterface %s was set to PROMISC mode.\n" % net_iface)

# Asking the user for the number of packets to sniff (the "count" parameter)
pkt_to_sniff = input("* Enter the number of packets to capture (0 is infinity): ")

# Place zero and will it run to infinity
if int(pkt_to_sniff) != 0:
    print("\nThe program will capture %d packets.\n" % int(pkt_to_sniff))

elif int(pkt_to_sniff) == 0:
    print("\nThe program will capture packets until the timeout expires.\n")

time_to_sniff = input("* Enter the number of seconds to run the capture: ")

# Handling the value entered by the user
if int(time_to_sniff) != 0:
    print("\nThe program will capture packets for %d seconds.\n" % int(time_to_sniff))

#
proto_sniff = input("* Enter the protocol to filter by (arp|bootp|icmp|llc|stp| 0 is all): ")

if (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp") or (proto_sniff == "llc") or (
        proto_sniff == "stp"):
    print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
# 0 means all protocols icmp, bootp, llc , stp , dot3 , uda you name it!!! will be sniffed
elif proto_sniff == "0":
    print("\nThe program will capture all protocols.\n")

file_name = input("* Please give a name to the log file: ")

sniffer_log = open(file_name, "a")


# details of the sniffing activity will be  saved in a file including the timestamp

def packet_log(packet):
    # Getting the current timestamp
    now = datetime.now()

    # Writing the packet information to the log file, also considering the protocol or 0 for all protocols
    if proto_sniff == "0":
        # Writing the data to the log file
        print("Time: " + str(now) + " Protocol: ALL" + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst,
              file=sniffer_log)

    elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp") or (proto_sniff == "llc") or (
            proto_sniff == "stp"):
        print(
            "Time: " + str(now) + " Protocol: " + proto_sniff.upper() + " SMAC: " + packet[0].src + " DMAC: " + packet[
                0].dst, file=sniffer_log)


# Printing an informational message to the screen
print("\n* Starting the capture...")

# Running the sniffing process (with or without a filter)
if proto_sniff == "0":
    sniff(iface=net_iface, count=int(pkt_to_sniff), timeout=int(time_to_sniff), prn=packet_log)

elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp") or (proto_sniff == "llc") or (
        proto_sniff == "stp"):
    sniff(iface=net_iface, filter=proto_sniff, count=int(pkt_to_sniff), timeout=int(time_to_sniff), prn=packet_log)

else:
    print("\nCould not identify the protocol.\n")
    sys.exit()

# Printing the closing message
print("\n* Please check the %s file to see the captured packets.\n" % file_name)

sniffer_log.close()

# Sniffed....DONE!!
