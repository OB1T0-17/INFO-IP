#!/usr/bin/env Python3

import socket
def info():
  rem = "www.google.com"
  
  try:
    print("La direccion IP es: %s" %socket.gethostbyname(rem))
    
  except socket.error, err_msg:
		print("%s: %s" %(rem, err_msg))
if __name__ == '__main__':
		info()
