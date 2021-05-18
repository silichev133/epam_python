import threading
import psutil

class Monitoring():

    #interval = int(config["common"]["interval"])
    
    def __init__(self, interval, output_format):
        self.interval = interval
        self.output_format = output_format

    def foo(self):
        if (self.output_format == "text"): 
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
        elif (self.output_format == "json"):
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

        threading.Timer(self.interval * 60, Monitoring.foo).start()

text_monitoring = Monitoring(1, "text")
text_monitoring.foo()

json_monitoring = Monitoring(1, "json")
json_monitoring.foo()
