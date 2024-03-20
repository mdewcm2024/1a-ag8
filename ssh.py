import os
if not os.path.exists("/home/runner/.ssh"):
  os.mkdir("/home/runner/.ssh")
os.system("mv ./download/id_rsa.txt /home/runner/.ssh/id_rsa")
os.system("mv ./download/config.txt /home/runner/.ssh/config")
os.system("chmod og-rwx /home/runner/.ssh/id_rsa")
