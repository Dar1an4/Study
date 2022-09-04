import os
import json


os_name = os.name
os_cwd = os.getcwd()
os_listdir = os.listdir()
os_env = os.environ
os_getlogin = os.getlogin()
os_getppid = os.getppid()

print(f"\n{os_name = }, \n{os_cwd = }, \n{os_listdir = }, \n{os_env = }, \n{os_getlogin = }, \n{os_getppid = } ")

obj_for_dump = {
                'os_name': os_name,
                'os_cwd': os_cwd,
                'os_listdir': os_listdir,
                'os_env': list(os_env),
                'os_getlogin': os_getlogin,
                'os_getppid': os_getppid,
                }
print(obj_for_dump)

with open("os_report.json", "w") as fh:
    json.dump(obj_for_dump, fh, indent=4, sort_keys=True)
