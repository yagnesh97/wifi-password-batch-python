import os
ssid = []
passw = []
fh = os.popen("test.bat")
output = fh.read()

for i in range (0, len(output.split())):
    if( output.split()[i]=="Profile" and output.split()[i+1]==":"):
        ssid.append(output.split()[i+2])
        

fh.close()

for i in range(0, len(ssid)):
    fh = open("test2.bat", "w")
    fh.write("netsh wlan show profile \"%s\" key=clear"%ssid[i])
    fh.close()
    fh = os.popen("test2.bat")
    output = fh.read()

    for j in range(0,len(output.split())):
        if(output.split()[j]=="Content" and output.split()[j+1]==":"):
            passw.append(output.split()[j+2])
            break
        
    fh.close()
    
print(len(ssid))
print(len(passw))
print(passw)
