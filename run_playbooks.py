import ansible_runner
import sys
import os
import random

def check_if_exist(name):
    full_name = "/var/www/webApp/webApp/Ansible-Playbooks/"+name
    spilt = full_name.split("/")
    host = "/var/www/webApp/webApp/Ansible-Playbooks/"+spilt[6]+"/inventory/host_vars/HOST.yml"
    if not os.path.exists(full_name):
        return "Playbook"
    if not os.path.exists(host):
        return "Host"
    return "Good"

def file_gen():
    file = open("/var/www/webApp/webApp/files/tmp.txt","r")
    file2 = open("/var/www/webApp/webApp/files/tmp2.txt","w")
    for count, line in enumerate(file):
        if count != 0 and count != 1 and count !=2:
            newline = line.replace("[0;36m"," ")
            newline = newline.replace("[0;32m"," ")
            newline = newline.replace("[0m"," ")
            newline = newline.replace("[0;33m"," ")
            file2.write(newline)
    file.close()
    file2.close()


def run_playbook(name):
    playbookOk = False
    try:
        full_name = "/var/www/webApp/webApp/Ansible-Playbooks/"+name
        spilt = full_name.split("/")
        host = "/var/www/webApp/webApp/Ansible-Playbooks/"+spilt[6]+"/inventory/host_vars/HOST.yml"
        out, err, rc = ansible_runner.run_command(
            executable_cmd='ansible-playbook',
            cmdline_args=[full_name,"-i",host])
        file = open("/var/www/webApp/webApp/tmp.txt","w")
        file.write("out: {}".format(out))
        file.close()
        file_gen()
        return playbookOk
    except:
        return playbookOk
   