from django.shortcuts import render
from django.http import JsonResponse
import serial
from calls.models import WodoAppuser, WodoWorkers
import redis
import time

from serial.tools import list_ports
# Create your views here.

REDIS_PORT = 6379
REDIS_HOST = '127.0.0.1'

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

ports = list_ports.comports()

def portSearch():
    for x in ports:
        if "USB" in x.name:
            if r.get(x.name).decode("ASCII")=="idle":
                port = x.name
                break
            else:
                return "ports unavailable."
        else:
            return "network hardware shutdown"
    return port

                          

def reader(interface):
    reader = interface.read(1000).decode("ASCII")
    return reader

def custConnect(worker, customer):
    port = portSearch()

    if port !="ports unavailable" & port !="network hardware shutdown":
        

        test = "AT\r"
        initiate = "ATD"+customer+";\r"
        checkState = "AT+CLCC\r"
        connectWork = "ATD"+worker+";\r"
        checkWorker = "AT+CLCC\r"
        connector = "AT+CHLD=3;\r"
        disconnect = "ATH\r"

        interface = serial.Serial("/dev/"+port, baudrate=9600, timeout=2)
        
        time.sleep(1)
        #tester:
        interface.write(test.encode())
        outputs = reader(interface)  
        
        if "OK" in outputs.split():
            
            #check if port is still available:
            if r.get(port).decode("ASCII")=="busy":
                if portSearch() != "ports unavailable":
                    interface = serial.Serial(portSearch(), baudrate=9600, timeout=2)
                else:
                    response = {
                        "status":"Failed",
                        "message":"Servers are busy."
                    }
                    return response

            
            #init call for customer
            interface.write(initiate.encode()) # create a call request to customer

            outputs = reader(interface)
            time.sleep(1)   # wait 1 seconds to transfer request

            if "OK" in outputs.split():
                interface.write(checkState.encode()) # check the status of call after 3 seconds
                outputs = reader(interface)
                if "OK" in outputs.split():
                    time.sleep(1.5) # time lag to cover handshake and connect
                    interface.write(checkState.encode()) # check the status of call after 1.5 seconds
                    outputs = reader(interface)
                    x = 0
                    while "2" in outputs.split() & x<=10:
                        time.sleep(1)
                        x=x+1
                    
                    x=0
                    
                    while "3" in outputs.split() & x<=10:
                        time.sleep(1)
                        x=x+1
                    
                    interface.write(checkState.encode()) # check the status of call after max 10 + 10 seconds
                    outputs = reader(interface)
                    
                    # If user response time or handshake is taking more than 10 seconds
                    if "2" in outputs.split() | "3" in outputs.split():
                        interface.write(disconnect.encode())
                        response = {
                            "status":"Failed",
                            "message":"Connection timed out, unable to reach customer"
                        }
                        return response
                    

                    time.sleep(1)

                    interface.write(checkState.encode()) # check the status of call after 3 seconds
                    outputs = reader(interface)
                    if "BUSY" in outputs.split():
                        interface.write(disconnect.encode())
                        outputs = reader(interface)
                        if "OK" in outputs.split():
                            response = {
                                "status":"Failed",
                                "message":"Connection terminated by customer"
                            }
                            return response
                        else:
                            response = {
                                "status":"Failed",
                                "message":"An Unknown error occured."
                            }
                            return response
                    elif "OK" in outputs.split():
                        # create and handle worker connections here.
                        response = {
                            "status":"success",
                            "message":"connected successfully to customer."
                        }


                    elif "NO CARRIER" in outputs.split():
                        

                else:
                    response = {
                        "status":"Failed",
                        "message":"Communication failed with network hardware"
                    }
            else:
                response = {
                    "status":"Failed",
                    "message":"Server failed to place a call"
                    }

    else:
        if port == "ports unavailable":
            response = {
                "status":"Failed",
                "message":"Servers are busy."
            }
        elif port == "network hardware shutdown":
            response = {
                "status":"Failed",
                "message":"Network hardware disconnected/shutdown."
            }

        return response
            




def getCalls(request):
    cust = request.headers.get("token")
    worker = request.headers.get("workerid")

    if "cust" & "worker" in globals():
        usrObj = WodoAppuser.objects.filter(username=cust)
        wrkObj = WodoWorkers.objects.filter(workerid=worker)

        if usrObj & wrkObj !=0:
            wrkCont = wrkObj[0].contact
            usrCont = usrObj[0].contact
        else:
            response = {
                "Status":"Failed",
                "Data": "Something went wrong, please try again."
            }
        
    
        
        
