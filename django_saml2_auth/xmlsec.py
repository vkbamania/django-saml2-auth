import os

def install():
    # proc = subprocess.Popen('apt-get update', shell=True, stdin=None,
    #                         stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
    # proc.wait()
    # proc1 = subprocess.Popen('apt-get install -y xmlsec1', shell=True, stdin=None,
    #                          stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
    # proc1.wait()
    print('started apt update')
    os.system("apt update")
    print('stopped apt update')
    print('started executing apt install -y xmlsec1')
    # subprocess.call("./install_xmlsec1.sh", shell=True)
    os.system('apt install -y xmlsec1')
    print('stoped executing apt install -y xmlsec1')
