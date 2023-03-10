import psutil
from psutil._common import AF_INET
from typing import List
import socket
import random


class WSLManager:
    MIN_PORT_VALUE=1
    MAX_PORT_VALUE=65535
    @staticmethod
    def getIPv4Adress()->str:
          addrs = psutil.net_if_addrs()
          WSL_KEY ="WSL"
          for key in addrs.keys():
               if WSL_KEY in key:
                    for addr in addrs[key]:
                         if addr.family.value ==AF_INET:
                              return addr.address
          return None
    @staticmethod
    def getAvailablePort()->int:
         ipv4Adress=WSLManager.getIPv4Adress()
         usedPorts=WSLManager.getUsedPorst(ipv4Adress)
         while True:
               port = random.randint(WSLManager.MIN_PORT_VALUE, WSLManager.MAX_PORT_VALUE) 
               if port not in usedPorts: 
                    break 
         return port
    @staticmethod
    def getUsedPorst(ipAddress:str)->List[int]:
          connections = psutil.net_connections()
          usedPorts = list()
          for c in connections:
               if c.type == socket.SOCK_STREAM and c.laddr.ip == ipAddress:
                    usedPorts.append(c.laddr.port)
          return usedPorts