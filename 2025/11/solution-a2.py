
class Connection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Device:
    def __init__(self, device_details):
        self.id = device_details[0]
        self.connections = device_details[1]

class Rack:
    def __init__(self):
        self.devices = []
        self.connection_count = 0

    def add(self, device):
        self.devices.append(device)
        self.connection_count += len(device.connections)

    # unfolds all connections hidden behind the devices
    def get_all_connections(self):
        connections = []
        for device in self.devices:
            for connection in device.connections:
                connections.append([device.id, connection])
        print("All connections:", connections)
        return connections

    # returns the number of paths for a certain route in a given set of connections
    def paths(self, start, end, connections):
        number = 0

        if len(connections) <= 0:
            return 0

        #print("Looking for paths between {} and {} in {}".format(start, end, connections))

        for connection_index in range(len(connections)):
            if connections[connection_index][1] == end:
                if connections[connection_index][0] == start:
                    return 1

                #print("Path found between {} and {}".format(connections[connection_index][0], connections[connection_index][1]))
                number += self.paths(start, connections[connection_index][0], connections[0:connection_index]+connections[connection_index+1:])

        return number

# create a "Rack"
rack = Rack()
with open("input.txt", "r") as file:
    for line in file:
        # device ID
        device = [line.strip("\n\r").split(": ")[0]]

        # connections for this device ID
        connections = line.strip("\n\r").split(": ")[1]
        rack_connections = []
        for connection in connections.split(" "):
            rack_connections.append(connection)
        device.append(rack_connections)

        print("Device", device[0], "connected to", device[1])
        rack.add(Device(device))

# "solve" the Rack
print("Given", rack.connection_count, "connections...")
number_of_paths = rack.paths("you", "out", rack.get_all_connections())
print("Solution:", number_of_paths)
