import wmi
import subprocess
import configparser
import winreg

cfp = configparser.ConfigParser()
cfp.read("Config.ini")

def read_ini():
    room = cfp.get("Main","room")
    offset = cfp.get("Main","offset")
    start = cfp.get("Main","start")
    row = cfp.get("Main","row").upper()
    return room,offset,start,row


def get_mac_address():
    c = wmi.WMI()
    network_adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    mac_addresses = [adapter.MACAddress for adapter in network_adapters]
    return mac_addresses[0]

def get_computer_name():
    c = wmi.WMI()
    computer_system = c.Win32_ComputerSystem()[0]
    computer_name = computer_system.Name
    return computer_name

def get_ip_addresses():
    c = wmi.WMI()
    network_adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    ip_addresses = []
    for adapter in network_adapters:
        ip_addresses.extend(adapter.IPAddress)
    return ip_addresses[0]


def get_text():
    mac_addresses = get_mac_address().replace(":", "-")
    computer_name = get_computer_name()
    ip_addresses = get_ip_addresses()
    with open('ttt.txt', 'a') as f:
        f.write(computer_name+"   "+ip_addresses+"    "+mac_addresses+"   "+computer_name + '\n')



def calc_ip():

    room,offset,start,row = read_ini()

    # print(ord(row)-64)
    number = ord(row)-65

    IP_Pre3 = "192.168.33"

    if room == '201':
        IP_Pre3 = "192.168.24"
    elif room == '216':
        IP_Pre3 = "192.168.26"
    elif room == '501':
        IP_Pre3 = "192.168.35"
    elif room == '308':
        IP_Pre3 = "192.168.33"

    PC_name = room + row + start
    IP_last = int(start) + int(offset)*number + 100
    Net_IP = IP_Pre3 + "." + str(IP_last)
    Net_gateway = IP_Pre3 + "."+"1"

    return Net_IP,Net_gateway,PC_name

def auto_modify():
    

    room,offset,start,row = read_ini()
    Net_IP,Net_gateway,PC_name = calc_ip()


    NetCard = "以太网"
    Net_MASK = "255.255.255.0"
    Net_DNS1 = "114.114.114.114"
    Net_DNS2 = "8.8.8.8"

    # print(Net_IP+"   "+Net_MASK+"   "+Net_gateway+"   "+Net_DNS1+"   "+Net_DNS2)


    def ModifyIP(NetCard, Net_IP, Net_MASK, Net_gateway, DNS1, DNS2):

        # cmd = f'netsh interface ip set address name={NetCard} static {Net_IP} {Net_MASK} {Net_gateway} 1'
        # dns_cmd = f'netsh interface ip set dns name={NetCard} static {DNS1} primary'
        # dns_backup_cmd = f'netsh interface ip add dns name={NetCard} addr={DNS2} index=2'
        
        # subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # subprocess.Popen(dns_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # subprocess.Popen(dns_backup_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 构建设置 IP 地址的命令
        set_address_command = f"netsh interface ip set address name=\"{NetCard}\" static {Net_IP} {Net_MASK} {Net_gateway}"

        # 构建设置 DNS 的命令
        set_dns_command = f"netsh interface ip set dns name=\"{DNS1}\" static {' '.join(DNS2)}"

        # 使用绝对路径调用命令提示符（CMD）并执行命令
        subprocess.call(["C:\\Windows\\System32\\cmd.exe", "/c", set_address_command])
        subprocess.call(["C:\\Windows\\System32\\cmd.exe", "/c", set_dns_command])

    ModifyIP(NetCard, Net_IP, Net_MASK, Net_gateway, Net_DNS1, Net_DNS2)


    # 打开指定的注册表项
    def change_name(path,value_name):
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, path)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, PC_name)
        winreg.CloseKey(key)

    change_name("System\CurrentControlSet\Control\ComputerName\ComputerName", "ComputerName")
    change_name("System\CurrentControlSet\Control\ComputerName\ActiveComputerName", "ActiveComputerName")
    change_name("System\CurrentControlSet\Services\Tcpip\Parameters", "NV Hostname")
    change_name("System\CurrentControlSet\Services\Tcpip\Parameters", "Hostname")
    change_name("System\CurrentControlSet001\Control\ComputerName\ComputerName", "ComputerName")
    change_name("System\CurrentControlSet001\Control\ComputerName\ActiveComputerName", "ActiveComputerName")

    temp_number = int(start)

    temp_number = temp_number + 1

    cfp.set("Main", "start", str(temp_number))

    cfp.write(open("Config.ini", "w"))
