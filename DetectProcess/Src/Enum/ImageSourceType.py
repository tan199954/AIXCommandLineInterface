from enum import Enum


class ImageSourceType(Enum):
    File="File"
    TcpServer="TcpServer"
    TcpClient="TcpClient"