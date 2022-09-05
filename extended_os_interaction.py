import os
import json
import platform
from speedtest import Speedtest
import psutil
import sys


os_name = os.name
os_cwd = os.getcwd()
os_listdir = os.listdir()
os_env = os.environ
os_getlogin = os.getlogin()
os_getppid = os.getppid()

platform_version = platform.version()
platform_system = platform.system()
platform_machine = platform.machine()
platform_processor = platform.processor()
platform_win32edition = platform.win32_edition()

inet = Speedtest()
download_speed = float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
upload_speed = float(str(inet.upload())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
cpufreq = psutil.cpu_freq()

sys_getver = sys.getwindowsversion()
sys_pyversion = sys.version

print(f"\n{os_name = }, \n{os_cwd = }, \n{os_listdir = }, \n{os_env = }, \n{os_getlogin = }, \n{os_getppid = },"
      f"\n{platform_version = }, \n{platform_system = }, \n{platform_machine = }, \n{platform_processor = },"
      f"\n{platform_win32edition = }, \n{download_speed = }, \n{upload_speed = }, \n{cpufreq = }, \n{sys_getver = }"
      f"\n{sys_pyversion = },")

obj_for_dump = {
                'sys_pyversion': sys_pyversion,
                'sys_getver': sys_getver,
                'os_name': os_name,
                'os_cwd': os_cwd,
                'os_listdir': os_listdir,
                'os_env': list(os_env),
                'os_getlogin': os_getlogin,
                'os_getppid': os_getppid,
                'platform_version': platform_version,
                'platform_system': platform_system,
                'platform_machine': platform_machine,
                'platform_processor': platform_processor,
                'platform_win32edition': platform_win32edition,
                'download_speed': download_speed,
                'upload_speed': upload_speed,
                'cpufreq': cpufreq
                }
print(obj_for_dump)

with open("os_report_extended.json", "w") as fh:
    json.dump(obj_for_dump, fh, indent=4, sort_keys=True)
