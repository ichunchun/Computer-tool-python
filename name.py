import winreg
import subprocess

def modify_name(pc_name):

    # 定义要修改的计算机名称
    new_computer_name = pc_name

    # 修改注册表中的计算机名称
    key_path = r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName"
    value_name = "ComputerName"
    value_type = winreg.REG_SZ

    try:
        # 打开注册表键
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)

        # 写入新的计算机名称
        winreg.SetValueEx(key, value_name, 0, value_type, new_computer_name)

        # 关闭注册表键
        winreg.CloseKey(key)
        # print("成功修改注册表中的计算机名称")
    except Exception as e:
        # print("修改注册表中的计算机名称时出现错误:", str(e))
        pass

    # 执行系统命令来修改计算机名称
    command = f"wmic computersystem where name='%COMPUTERNAME%' call rename name='{new_computer_name}'"
    try:
        subprocess.check_output(command, shell=True)
        # print("成功修改计算机名称")
    except subprocess.CalledProcessError as e:
        # print("修改计算机名称时出现错误:", str(e))
        pass
