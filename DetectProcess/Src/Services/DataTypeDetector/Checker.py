from typing import List
import os
from ...Exceptions.TcpException import TcpDictionaryFormatError, TcpIpAdressError
from ..Common.TCPIPManager.TCPIPManager import TCPIPManager

class TcpIPFormatChecker:
     @staticmethod
     def checkTcpIPDictionary(tcpIPDictionary:dict):
          if "ip" not in tcpIPDictionary.keys() or "port" not in tcpIPDictionary.keys():
               raise TcpDictionaryFormatError("Tcp dictionary is not contains 'ip' key or 'port' key")
          ipAdress=tcpIPDictionary["ip"]
          if not TCPIPManager.isIpv4Format(ipAdress):
               raise TcpIpAdressError(f"{ipAdress} is not Ipv4 Format")
          port=tcpIPDictionary["port"]
          if not TCPIPManager.isValidPortRange(port):
               raise ValueError(f"{port} is out of port range from {TCPIPManager.MIN_PORT_NUM} to {TCPIPManager.MAX_PORT_NUM}")


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