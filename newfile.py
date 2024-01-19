import platform
import socket
import psutil
# import speedtest
#import wmi

def get_installed_software():
    software_list = []
    for item in psutil.process_iter(['pid', 'name']):
        software_list.append(item.info['name'])
    return software_list

def get_screen_resolution():
    try:
        import screeninfo
        screen = screeninfo.get_monitors()[0]
        return screen.width, screen.height
    except ImportError:
        return None


def get_cpu_info():
    cpu_info = {}
    cpu_info['model'] = platform.processor()
    cpu_info['cores'] = psutil.cpu_count(logical=False)
    cpu_info['threads'] = psutil.cpu_count(logical=True)
    return cpu_info

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].name
    except ImportError:
        pass
    return None

def get_ram_size():
    return round(psutil.virtual_memory().total / (1024 ** 3), 2)

def get_screen_size():
    try:
        import screeninfo
        screen = screeninfo.get_monitors()[0]
        return screen.width_mm, screen.height_mm
    except ImportError:
        return None

def get_network_info():
    interfaces = psutil.net_if_addrs()
    mac_addresses = {}
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_LINK:
                mac_addresses[interface] = addr.address
    return mac_addresses

def get_public_ip():
    return socket.gethostbyname(socket.gethostname())

def get_windows_version():
    return platform.version()


print("Installed Software:", get_installed_software())
print("Screen Resolution:", get_screen_resolution())
print("CPU Info:", get_cpu_info())
print("GPU Info:", get_gpu_info())
print("RAM Size:", get_ram_size(), "GB")
print("Screen Size:", get_screen_size())
print("Network MAC Addresses:", get_network_info())
print("Public IP Address:", get_public_ip())
print("Windows Version:", get_windows_version())