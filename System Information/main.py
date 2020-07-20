import cpuinfo
import platform
from psutil import virtual_memory




def details():
    print("\n\t[ System Information ]\n")
    print(f"System: \t\t{platform.system()} ")
    print(f"System Version: \t\t{platform.platform()}")
    print(f"Archictecture: \t\t{platform.machine()}")
    print(f"Processor: \t\t {cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"Ram: {round(virtual_memory().total / 1_000_000, 2)}Mb")
    print(f"Python: \t\t{platform.python_version()}")


if __name__=="__main__":
    details()