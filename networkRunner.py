
import subprocess



def sendNetwork(ip , subnetMask , gateway ):

    bashCommand = "echo 1234 | sudo -S su"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    
    
    bashCommand = "sudo chmod u+x network.sh " 

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print("Error code " , error)

    bashCommand = "sudo ./network.sh " +  ip +" "+ subnetMask +" "+ gateway

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def writedhcp():
    f = open("conf.txt","w")
    f.write("dhcp")
    f.close() 
