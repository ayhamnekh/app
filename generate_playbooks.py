# Class which will generate playbook from template 1 using the data from class playbook_1
def playbook_1_generator(playbook_name,interface_list,ipaddress_list,ccoid):
    template_l = open('/var/www/webApp/webApp/Playbooks_Templates/nxos-vxlan-leafs.yml',"r")
    playbook_name_l = "/var/www/webApp/webApp/Ansible-Playbooks/"+ccoid+"/"+playbook_name+"-LEAFS.yml"
    end_file = open(playbook_name_l,'w')
    for line_number, line in enumerate(template_l):
        if line_number == 2:
            end_file.write("  hosts: "+str(playbook_name)+ "-GROUP-2\n")
        elif line_number == 4:
            end_file.write("    leafA: \""+str(playbook_name)+"-LEAF-A\"\n")
        elif line_number == 5:
            end_file.write("    leafB: \""+str(playbook_name)+"-LEAF-B\"\n")
        elif line_number == 6:
            end_file.write("    intLASA: \"Ethernet"+interface_list[1]+"\"\n")
        elif line_number == 7:
            end_file.write("    intLBSA: \"Ethernet"+interface_list[3]+"\"\n")
        elif line_number == 8:
            end_file.write("    intLASB: \"Ethernet"+interface_list[5]+"\"\n")
        elif line_number == 9:
            end_file.write("    intLBSB: \"Ethernet"+interface_list[7]+"\"\n")
        else:
            end_file.write(line)
    template_s = open('/var/www/webApp/webApp/Playbooks_Templates/nxos-vxlan-spines.yml',"r")
    playbook_name_s = "/var/www/webApp/webApp/Ansible-Playbooks/"+ccoid+"/"+playbook_name+"-SPINES.yml"
    end_file = open(playbook_name_s,'w')
    for line_number, line in enumerate(template_s):
        if line_number == 2:
            end_file.write("  hosts: "+str(playbook_name)+ "-GROUP-1\n")
        elif line_number == 4:
            end_file.write("    spineA: \""+str(playbook_name)+"-SPINE-A\"\n")
        elif line_number == 5:
            end_file.write("    spineB: \""+str(playbook_name)+"-SPINE-B\"\n")
        elif line_number == 6:
            end_file.write("    intSALA: \"Ethernet"+interface_list[0]+"\"\n")
        elif line_number == 7:
            end_file.write("    intSALB: \"Ethernet"+interface_list[2]+"\"\n")
        elif line_number == 8:
            end_file.write("    intSBLA: \"Ethernet"+interface_list[4]+"\"\n")
        elif line_number == 9:
            end_file.write("    intSBLB: \"Ethernet"+interface_list[6]+"\"\n")
        else:
            end_file.write(line)

def adding_to_host(ccoid,playbook_name,device_list,ipaddress_list,group_ammount=1,group_count=1,username="admin",password="cisco!123"):
    host_file_name = "/var/www/webApp/webApp/Ansible-Playbooks/"+ccoid+"/inventory/host_vars/HOST.yml"
    host_file = open(host_file_name,"a")
    host_file.write("\n["+str(playbook_name)+"]\n")
    for count, device in enumerate(device_list):
        host_file.write(str(device_list[count])+" ansible_host="+str(ipaddress_list[count])+" ansible_python_interpreter=/opt/envs/ansible/bin/python3\n")
    host_file.write("\n[" + str(playbook_name) + ":vars]\n")
    host_file.write("ansible_connection=ansible.netcommon.network_cli\nansible_network_os=cisco.nxos.nxos\nansible_user="+username+"\nansible_password="+password+"\nansible_become=yes\nansible_become_method=enable\nansible_become_password="+password+"\nansible_ssh_common_args='-o ProxyCommand='ssh -W %h:%p -q bastion01''\n")
    #------- Part in which you devide the host into individual groups --------
    for count, device in enumerate(device_list):
        host_file.write("\n[" + str(playbook_name) + "-"+str(device_list[count])+"]\n")
        host_file.write(str(device_list[count])+" ansible_host="+str(ipaddress_list[count])+" ansible_python_interpreter=/opt/envs/ansible/bin/python3\n")
    #------- Part in which you devide the host into different groups --------
    if group_ammount != 1:
        counter = 0
        first_loop = 0
        second_loop = 0
        while first_loop < group_ammount:
            host_file.write("\n[" + str(playbook_name) + "-GROUP-" + str(first_loop+1) + "]\n")
            while second_loop < group_count:
                host_file.write(str(device_list[counter]) + " ansible_host=" + str(ipaddress_list[counter]) + " ansible_python_interpreter=/opt/envs/ansible/bin/python3\n")
                counter += 1
                second_loop += 1
            second_loop = 0
            first_loop += 1
    host_file.close()

def check_playbook_name(ccoid,playbook_name):
    playbook_name = str(ccoid) + "." + str(playbook_name) + ".yml"
    file_playbook_names = open("/var/www/webApp/webApp/files/playbook_names.txt","r+")
    duplicate = False
    for i in file_playbook_names:
        if i == playbook_name:
            duplicate = True
    if duplicate == True:
        return False
    else:
        file_playbook_names.write('\n'+str(playbook_name))
        return True