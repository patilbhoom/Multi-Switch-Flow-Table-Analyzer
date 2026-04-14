## Project Title
Multi-Switch Flow Table Analyzer

## Problem Statement
Analyze flow tables in SDN switches and display rule usage.

## Objective
1. Retrieve flow entries
2. Display rule details
3. Identify active vs unused rules
4. Show dynamic updates
   
## Tools Used
1. Mininet
2. POX Controller
3. Open vSwitch
   
## Steps to Run
1. Start controller
./pox.py openflow.of_01 forwarding.l2_learning
2. Start Mininet
sudo mn --topo single,3 --controller remote
3. Generate traffic
pingall
4. View flow table
sudo ovs-ofctl dump-flows s1

## Output
Before traffic:
n_packets=0 → UNUSED

After traffic:
n_packets>0 → ACTIVE

## Conclusion
Flow rules in SDN switches dynamically update based on traffic. Active rules can be identified using packet count.
