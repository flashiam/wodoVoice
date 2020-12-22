import serial
import re
import time
import redis

port0 = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=2)
#port1 = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=2)

read0 = port0.read(100).decode("ASCII")
#read1 = port1.read(100).decode("ASCII")

REDIS_PORT = 6379
REDIS_HOST = '127.0.0.1'

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def buffer_chk(port, read):
    n=0
    if read.find("RING")<0:
        for i in range(n):
            if read=="":
                res = read
                return res
            else:
                port.read(100)
                n=n+1
                # return port.read(100)       
    else:
        return read


def checker(read, port):
    read = buffer_chk(port, read)
    if read!="":
        detCall = read.find("RING")
        if detCall>=0:
            if r.get(port)=="0":
                cmd = "ATA \r"
                port.write(cmd.encode())
                time.sleep(2)
                port.write(b"AT+CLIP=1")
                time.sleep(2)
                port.read(100)
                port.write(b"ATH")
            elif r.get(port)=="1":
                port.write(b"ATA")
        else:
            buffer_chk(port, read)

def main():
    while True:
        checker(read0, port0)


if __name__ == "__main__":
    main()




