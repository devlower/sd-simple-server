import Pyro4.naming

def start_nameserver():
    Pyro4.naming.startNSloop()

if __name__ == "__main__":
    start_nameserver()