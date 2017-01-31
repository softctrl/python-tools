# Just a simple modification into this great program
# to allow inform what interface should be used.
#
# Telnet Program Example
# Source: http://www.binarytides.com/code-telnet-client-sockets-python/
import socket, select, string, sys
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py [src-interface] [hostname] [port]'
        sys.exit()
     
    source = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(source, 12345)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print 'Connection closed'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
