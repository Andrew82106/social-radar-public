try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data

import platform
import subprocess
import re
import psutil  # 需要安装 psutil 库


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error: {e}")
        return None


def parse_memory_info(output):
    memory_info = re.findall(r"(\S+):\s+(\d+)\s+(\d+)\s+(\d+)", output)
    return {item[0]: {'total': int(item[1]), 'used': int(item[2]), 'free': int(item[3])} for item in memory_info}


def parse_df_info(output):
    filesystems = re.findall(r"(\S+)\s+(\d+\S+)\s+(\d+\S+)\s+(\d+\S+)\s+(\d+%)\s+(\/\S+)", output)
    return {item[5]: {'size': item[1], 'used': item[2], 'free': item[3], 'usage': item[4]} for item in filesystems}


def get_linux_info():
    system_info = {}

    # 获取 uptime
    uptime_output = run_command("uptime")
    system_info['uptime'] = uptime_output.strip() if uptime_output else None

    # 获取 free
    free_output = run_command("free")
    if free_output:
        system_info['memory'] = parse_memory_info(free_output)

    # 获取 df
    df_output = run_command("df -h")
    if df_output:
        system_info['filesystems'] = parse_df_info(df_output)

    return system_info


def get_macos_info():
    system_info = {}

    # 获取 uptime
    uptime_output = run_command("uptime")
    system_info['uptime'] = uptime_output.strip() if uptime_output else None

    # 获取 df
    df_output = run_command("df -h")
    if df_output:
        system_info['filesystems'] = parse_df_info(df_output)

    # 获取 top 输出
    top_output = run_command("top -l 1 -n 0")
    system_info['top'] = top_output.strip() if top_output else None

    return system_info


def get_windows_info():
    system_info = {}

    # 获取 uptime（Windows 不提供原生的 uptime 命令，可以采用其他方式获取系统运行时间）

    # 获取内存信息
    memory = psutil.virtual_memory()
    system_info['memory'] = {
        'total': memory.total,
        'used': memory.used,
        'free': memory.available
    }

    # 获取磁盘信息
    partitions = psutil.disk_partitions()
    filesystems = {}
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        filesystems[partition.mountpoint] = {
            'size': partition_usage.total,
            'used': partition_usage.used,
            'free': partition_usage.free,
            'usage': partition_usage.percent
        }
    system_info['filesystems'] = filesystems

    return system_info


def get_system_info():
    system_info = {}
    os_type = platform.system()

    if os_type == 'Linux':
        system_info = get_linux_info()
    elif os_type == 'Darwin':  # macOS
        system_info = get_macos_info()
    elif os_type == 'Windows':
        system_info = get_windows_info()
    else:
        print("Unsupported operating system")

    return system_info


class ServerStatus(BaseInfo):
    def __init__(self):
        super().__init__()

    def load_data(self):
        self.data = get_system_info()


if __name__ == "__main__":
    performance_info = get_system_info()
    print(performance_info)
