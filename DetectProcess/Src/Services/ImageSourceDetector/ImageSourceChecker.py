from typing import List
import os
import ipaddress
from ...Exceptions.TcpException import TcpDictionaryFormatError, TcpIpAdressError

class TcpIPFormatChecker:
     MIN_PORT_NUM=0
     MAX_PORT_NUM=65535
     @staticmethod
     def checkTcpIPDictionary(tcpIPDictionary:dict):
          if "ip" not in tcpIPDictionary.keys() or "port" not in tcpIPDictionary.keys():
               raise TcpDictionaryFormatError("Tcp dictionary is not contains 'ip' key or 'port' key")
          ipAdress=tcpIPDictionary["ip"]
          if not TcpIPFormatChecker.__isIpv4Format(ipAdress):
               raise TcpIpAdressError(f"{ipAdress} is not Ipv4 Format")
          port=tcpIPDictionary["port"]
          if not TcpIPFormatChecker.__isValidPortRange(port):
               raise ValueError(f"{port} is out of port range from {TcpIPFormatChecker.MIN_PORT_NUM} to {TcpIPFormatChecker.MAX_PORT_NUM}")
     def __isIpv4Format(ipAdress:str)->bool:
          try:
               ipaddress.IPv4Address(ipAdress)
               return True
          except ipaddress.AddressValueError:
               return False
     def __isValidPortRange(port:int)->bool:
          if not isinstance(port,int):
               return False
          return port >= TcpIPFormatChecker.MIN_PORT_NUM and port <= TcpIPFormatChecker.MAX_PORT_NUM


class ImageFormatChecker:
     IMAGE_EXTENSIONS = [".png",".jpg",".bmp"]
     @staticmethod
     def checkImageFilePath(imageFilePath:str):
          if not os.path.exists(imageFilePath):
               raise Exception(f"{imageFilePath} is not exists")
          if not ImageFormatChecker.__isEqualExtensison(imageFilePath,ImageFormatChecker.IMAGE_EXTENSIONS):
               raise Exception(f"{imageFilePath} is not png, jpg or bmp format")
     def __isEqualExtensison(filePath:str,fileExtensions:List[str])->bool:
          extension = os.path.splitext(filePath)[1]
          return extension.lower() in fileExtensions