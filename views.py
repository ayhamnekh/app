from array import array
from flask import Flask, redirect, url_for, render_template, request, session, flash
import random
import sys
from app import app


from create_user import createuser
from run_playbooks import run_playbook, check_if_exist
from list_available_playbooks import list_available_playbooks
from generate_playbooks import playbook_1_generator,adding_to_host,check_playbook_name


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return render_template("generate.html")

@app.route("/playbook1", methods=["POST","GET"])
def playbook1():
    if request.method == "POST":
        ccoid = request.form["ccoid"]
        ipaddress_1 = request.form["ipaddress_1"]
        ipaddress_2 = request.form["ipaddress_2"]
        ipaddress_3 = request.form["ipaddress_3"]
        ipaddress_4 = request.form["ipaddress_4"]
        int_SA_LA = request.form["int_SA_LA"]
        int_LA_SA = request.form["int_LA_SA"]
        int_SA_LB = request.form["int_SA_LB"]
        int_LB_SA = request.form["int_LB_SA"]
        int_SB_LA = request.form["int_SB_LA"]
        int_LA_SB = request.form["int_LA_SB"]
        int_SB_LB = request.form["int_SB_LB"]
        int_LB_SB = request.form["int_LB_SB"]
        playbook_name = request.form["playbook_name"]
        lab_name = request.form["lab_name"]
        defaultP = request.form["defaultP"]
        if defaultP == "no":
            login = request.form["login"]
            password = request.form["password"]
        else:
            login = "admin"
            password = "cisco!123"
        ipaddress_list = [ipaddress_1,ipaddress_2,ipaddress_3,ipaddress_4]
        device_list = ['SPINE-A','SPINE-B','LEAF-A','LEAF-B']
        interface_list = [int_SA_LA,int_LA_SA,int_SA_LB,int_LB_SA,int_SB_LA,int_LA_SB,int_SB_LB,int_LB_SB]
        
        
        adding_to_host(ccoid,playbook_name,device_list,ipaddress_list,2,2,login,password)
       
        playbook_1_generator(playbook_name,interface_list,ipaddress_list,ccoid)
        isUnique = check_playbook_name(ccoid,playbook_name)
        if isUnique == True:
            playbook_generated = open("var/www/webApp/webApp/files/playbook_generated.txt","a")
            playbook_generated.write("VxLAN BGP - 2 SPINES 2 LEAFS;"+ccoid+";"+lab_name+";"+ccoid+"/"+playbook_name+"-LEAFS.yml\n")
            playbook_generated.write("VxLAN BGP - 2 SPINES 2 LEAFS;"+ccoid+";"+lab_name+";"+ccoid+"/"+playbook_name+"-SPINES.yml\n")
            playbook_generated.close()
        else:
            playbook_generated = open("var/www/webApp/webApp/files/playbook_generated.txt","a")
            number = "2"
            playbook_name = playbook_name+"("+number+")"
            playbook_generated.write("VxLAN BGP - 2 SPINES 2 LEAFS;"+ccoid+";"+lab_name+";"+ccoid+"/"+playbook_name+"-LEAFS.yml\n")
            playbook_generated.write("VxLAN BGP - 2 SPINES 2 LEAFS;"+ccoid+";"+lab_name+";"+ccoid+"/"+playbook_name+"-SPINES.yml\n")
            playbook_generated.close()
        flash("You created new template!","info")
        return render_template("playbook1.html")
        
    else: 
        return render_template("playbook1.html")
    

@app.route("/user", methods=["POST","GET"])
def user():
    if request.method == "POST":
        ccoid = request.form["ccoid"]
        isCreated = createuser(ccoid)
        if isCreated:
            flash("You created new user!","info")
            return render_template("user.html")
        else:
            flash("This user already exist!","info")
            return render_template("user.html")
    else: 
        return render_template("user.html")

@app.route("/run", methods=["POST","GET"])
def run():
    list, length = list_available_playbooks();
    if request.method == "POST":
        playbook_name = request.form["playbook"]
        exist = check_if_exist(playbook_name)
        if exist == "Playbook":
            flash("This playbook do not exist!","info")
        elif exist == "Playbook":
            flash("There is a problem with the HOST.yml!","info")
        else:
            flash("Prerun checks - passed","info")
            run_playbook(playbook_name)
        return redirect(url_for("runned"))
    else:
        return render_template("run.html",list = list, length = length)

@app.route("/runned",methods=["POST","GET"])
def runned():
    file_array =[]
    file = open('/var/www/webApp/webApp/files/tmp2.txt', 'r')
    counter = 100
    for line in file:
        line = line.replace("*","")
        file_array.append(line)
        counter = counter + 1.78
    counter = str(counter)+"%"
    return render_template("runned.html", text=file_array, size =  counter)

