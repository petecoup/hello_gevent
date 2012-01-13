import gevent
import sys
import time
from gevent import socket

def runconnection(connection_id):
    s = socket.create_connection(('127.0.0.1', 56789))
    s.sendall('Mr %s' % (connection_id,))
    data = s.recv(1024)
    s.close()
    return data

def main():
    if len(sys.argv) == 1:
        raise Exception("Not Enough Arguments.")

    num_connections = int(sys.argv[1])
    jobs = [gevent.Greenlet(runconnection, connid) for connid in range(num_connections)]
    for job in jobs:
        job.start()
    gevent.joinall(jobs, timeout=10)
    total = 0
    for job in jobs:
        total += int(job.value)
    print(str(total))

if __name__=='__main__':
    main()

