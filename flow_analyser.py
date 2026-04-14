import os

switches = ["s1", "s2"]

print("Checking Flow Usage...\n")

for sw in switches:
    print("\n===== SWITCH:", sw, "=====")

    output = os.popen(f"sudo ovs-ofctl dump-flows {sw}").read()
    print("Flow Table:\n", output)

    lines = output.split("\n")

    for line in lines:
        if "n_packets" in line:
            try:
                packets = int(line.split("n_packets=")[1].split(",")[0])

                if packets == 0:
                    print("UNUSED FLOW")
                else:
                    print("USED FLOW")

            except:
                pass