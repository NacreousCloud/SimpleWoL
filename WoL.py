import socket, struct

def WOL(macAddr, ip):
    sep = macAddr[2]        # get seperlator
    macAddr = macAddr.replace(sep,'')       # remove seperlator
        
    data = b'FFFFFFFFFFFF' + (macAddr * 16).encode()    
    send_data = b''
    
    for i in range(0, len(data), 2):
        send_data += struct.pack('B', int(data[i: i + 2], 16))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, (ip,9))                 # send to port 9
    
WOL('','')