import os
def createuser(ccoid):
    path1 = '/var/www/webApp/webApp/Ansible-Playbooks'
    path2 = '/var/www/webApp/webApp/Ansible-Playbooks/'+ccoid
    path3 = '/var/www/webApp/webApp/Ansible-Playbooks/'+ccoid+"/inventory"
    path4 = '/var/www/webApp/webApp/Ansible-Playbooks/'+ccoid+"/inventory/host_vars"
    path5 = '/var/www/webApp/webApp/Ansible-Playbooks/'+ccoid+"/inventory/group_vars"
    host_file_path = path4+"/HOST.yml"
    ansible_config_path = path2+"/ansible.cfg"
    anyChange = False

    if not os.path.exists(path1):
        os.makedirs(path1)

    if not os.path.exists(path2):
        os.makedirs(path2)
        anyChange = True

    if not os.path.exists(path3):
        os.makedirs(path3)
        anyChange = True

    if not os.path.exists(path4):
        os.makedirs(path4)
        anyChange = True

    if not os.path.exists(path5):
        os.makedirs(path5)
        anyChange = True

    if not os.path.exists(host_file_path):
        host_file = open(host_file_path,'w')
        host_file.close()
        anyChange = True

    if not os.path.exists(ansible_config_path):
        ansible_file = open(ansible_config_path,'w')
        ansible_file.write("[defaults]\ninventory = inventory/host_vars/HOST.yml\nhost_key_checking = false\nstdout_callback = yaml\ncallback_enabled = timer\n[persistent_connection]\ncommand_timeout = 60")
        ansible_file.close()

    if anyChange:
        return True
    else:
        return False