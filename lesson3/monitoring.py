import threading
import psutil
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

interval = int(config["common"]["interval"])
output_format = config["common"]["output"]

def foo():
    if (output_format == "text"): 
        with open('test.txt', 'a') as file:
            file.write("CPU usage: ")
            file.write(str(psutil.cpu_percent()))
            file.write("\n")
            file.write("RAM total: ")
            file.write(str(psutil.virtual_memory().total))
            file.write("\n")
            file.write("SWAP total: ")
            file.write(str(psutil.swap_memory().total))
            file.write("\n")
            file.write("Network information: \n")
            for key, val in psutil.net_if_addrs().items():
                file.write('{}: {}\n'.format(key, val))
            file.write("\n")
    elif (output_format == "json"):
        with open('test.json', 'a') as file:
            file.write("{\n")
            file.write("\tCPU_usage: ")
            file.write(str(psutil.cpu_percent()))
            file.write("\n")
            file.write("\tRAM_total: ")
            file.write(str(psutil.virtual_memory().total))
            file.write("\n")
            file.write("\tSWAP_total: ")
            file.write(str(psutil.swap_memory().total))
            file.write("\n")
            file.write("\tNetwork_information: {\n")
            for key, val in psutil.net_if_addrs().items():
                file.write('\t\t{}: {}\n'.format(key, val))
            file.write("\n")
            file.write("\t}")
            file.write("\n")
            file.write("}")
    else:
        print("Nothing log file")
    threading.Timer(interval * 60, foo).start()

foo()


