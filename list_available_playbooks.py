def list_available_playbooks():
    playbook_generated = open("/var/www/webApp/webApp/files/playbook_generated.txt","r")
    counter = 0
    for line in playbook_generated:
        counter = counter + 1
    w,h = 4,counter
    array_playbook_generated= [[0 for x in range(w)] for y in range(h)]
    playbook_generated = open("/var/www/webApp/webApp/files/playbook_generated.txt","r")
    for count, line in enumerate(playbook_generated):
        split_line = line.split(";")
        for count2, word in enumerate(split_line):
            array_playbook_generated[count][count2] = split_line[count2]
    return array_playbook_generated, counter;
