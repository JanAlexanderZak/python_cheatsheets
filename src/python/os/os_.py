import os

os.path.abspath(".")
os.path.commonprefix(["/home", "/home/h"])      # returns as string
os.path.exists("H")                             # checks in current dir
os.listdir('./')                                # gets all files in dir
os.path.dirname(__file__)                       # path to current file
os.path.exists(os.path.dirname(__file__))       # checks if exists
os.path.getatime('./')                          # last access time
os.path.getmtime('./')                          # last modification time
os.path.getsize('./')                           # get size in bytes
os.path.join('./')                              # joins paths
