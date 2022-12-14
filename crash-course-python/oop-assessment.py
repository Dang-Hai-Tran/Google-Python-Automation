# Begin Portion 1 #
import random


class Server:
    def __init__(self):
        """ Creates a new server instance, with no active connections. """
        self.connections = {}

    def add_connection(self, connection_id):
        """ Adds a new connection to this server. """
        connection_load = random.random() * 10 + 1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """ Closes a connection on this server. """
        # Remove a connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """ Calculates the current load for all connections. """
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """ Return a string with the current load of the server. """
        return "{:.2f}%".format(self.load())

# server = Server()
# server.add_connection("192.168.1.1")
# print(server.load())

# server.close_connection("192.168.1.1")
# print(server.load())


class LoadBalancing:
    def __init__(self) -> None:
        """ Initialize the load balancing system with one server. """
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """ Randomly selects a server and adds a connection to it. """
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Add the connection to the server
        server.add_connection(connection_id)
        # Ensure availability
        self.ensure_availability()

    def close_connection(self, connection_id):
        """ Closes the connection on the server corresponding to the connection_id. """
        # Find out the right server
        selected_server = self.connections[connection_id]
        # Close the connection on the server
        selected_server.close_connection(connection_id)
        # Remove the connection from the load balancer
        del self.connections[connection_id]

    def avg_load(self):
        """ Calculates the average load of all servers """
        # Sum the load of each server and divide by the amount of server
        total_load = 0
        num_connected_servers = len(self.servers)
        for connected_server in self.connections.values():
            total_load += connected_server.load()
        return total_load / num_connected_servers

    def ensure_availability(self):
        """ If the average load is higher than 50, spin up a new server """
        if self.avg_load() > 50:
            new_server = Server()
            self.servers.append(new_server)

    def __str__(self) -> str:
        """ Return a string with the load for each server. """
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


l = LoadBalancing()
l.add_connection("fdca:83d2:f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2:f20d")
print(l.avg_load())

for connection in range(100):
    l.add_connection(connection)
print(l)
print(l.avg_load())
