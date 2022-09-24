# packet_sniffer
scapy python module script for sniffing packets for specified protocols or all protocols and includes the source mac address and destination mac address.

The code handles Number of packets to be sniffed, The time interval, Protocol considered, Filtering the protocols and logging the information into a txt file.

Running the script in the docker ubuntu linux host machine in the gns3 environment.





![ubuntu_server](https://user-images.githubusercontent.com/61822296/192036041-b2fb5819-107d-4782-9d56-9880e319bf0f.png)






The gns3 topology with network automation container as the host machine.

nano /etc/network/interfaces - to configure network interface and enable assigning dhcp and connectivity to the NAT cloud.

![gns3](https://user-images.githubusercontent.com/61822296/192082096-4fbd9c36-ff75-4ee9-b0c4-80643328a4bb.png)

installing the scapy module for capturing, handling and analyzing network traffic.

pip3 install scapy









![scapy](https://user-images.githubusercontent.com/61822296/192082374-6c8e9361-5f7f-4854-b835-a04ccb67cc3b.png)


run python3 packet_sniffer.py as root


![capture](https://user-images.githubusercontent.com/61822296/192082383-1d440de1-aa63-41c1-8d70-9b9b513e5a33.png)


details of the traffic stored in a file - vic file that includes the timestamp and protocol for example below i specified all protocols together with the SMAC(source mac address) and DMAC(destination mac address) 

![logs](https://user-images.githubusercontent.com/61822296/192082382-ee09f292-7479-42c1-87fd-4dbd576ab2c0.png)





do you smell what the network is cooking? :)
