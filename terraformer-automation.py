import os
import subprocess
import fileinput
import sys
import logging
import re
logging.basicConfig(level=logging.INFO)
print("Hello! Welcome to the AWS Configuration and Login tool!")

# Prompt user for input
aws_input = input("Would you like to configure your AWS account or login to SSO? (configure/login/notrequired): ")

# Process user input for aws login
if aws_input == "configure":
    print("You have selected to configure your AWS account!")
    subprocess.run("aws configure sso", shell=True)
elif aws_input == "login":
    print("You have selected to login to SSO!")
    subprocess.run("aws sso login" ,shell=True)
elif aws_input == "notrequired":
    print("Please proceed with the next steps")

try:
    print("Please enter the following inputs")
    provider = input('Enter the provider: ')
    region = input('Enter the region: ')
    resource = input('Enter the resource name: ')
    string_add_variable = 'terraformer import ' + provider + ' --resources=' + resource + ' --regions=' + region
    os.system(string_add_variable)
except:
    print("terraformer command not found")

# Prompt user for input
resource_name = input ("Enter the name of resource which you want to automate: ")
base_dir =  os.getcwd()
final_path = os.path.join(base_dir, 'generated', 'aws', resource_name)
os.chdir(final_path)
os.system('ls -l')

final_file = input("enter the name of the file you want to variablize(with .tf extention): ")
final_path2 = os.path.join(base_dir, 'generated', 'aws')
os.chdir(final_path2)
os.system('mkdir module')

final_path3 = os.path.join(base_dir, 'generated', 'aws', 'module')
os.chdir(final_path3)
os.system("mkdir "+resource_name)

def create_module():
    f = open(base_dir+'/generated/aws/module/'+resource_name+'/resource.tf','w')
    f.write('module "'+resource_name+'" { \n source = "../../'+resource_name+'" \n ')
    f.close()
create_module()

def identify1(line):
    replace_string ="default = "+ line.split('=')[1]
    return replace_string

def replace1(replace_string,i):
    with open(base_dir+'/generated/aws/module/'+resource_name+'/variable.tf', 'r') as file:
        data = file.read()
        data = data.replace(' default = "'+var+str(i)+'"',replace_string+"\n")

    with open( base_dir+'/generated/aws/module/'+resource_name+'/variable.tf', 'w') as file:
        file.write(data)
def variable(var,i):
    f = open(base_dir+'/generated/aws/module/'+resource_name+'/variable.tf','a')
    f.write(('variable "'+repr(var)+ str(i)+'" { \n default = "'+repr(var)+ str(i) +'" \n}').replace("'","")+'\n')
    f.close()

file = open(base_dir+'/generated/aws/'+resource_name+'/'+final_file).readlines()
def identify(line):
    replace_string = line.split('=')[1]
    return replace_string

def replace(replace_string,i):
    with open( base_dir+'/generated/aws/'+resource_name+'/'+final_file, 'r') as file:
        data = file.read()
        data = data.replace(replace_string," var."+var+str(i)+"\n")
    with open( base_dir+'/generated/aws/'+resource_name+'/'+final_file, 'w') as file:
        file.write(data)
def create_var(var,i):
    f = open(base_dir+'/generated/aws/'+resource_name+'/variables.tf','a')
    f.write(('variable "'+repr(var)+str(i)+'" {  }').replace("'","")+'\n')
    f.close()

def modify_modules(var,i):
    f = open(base_dir+'/generated/aws/module/'+resource_name+'/resource.tf','a')
    f.write((''+repr(var)+str(i)+' = var.'+repr(var)+str(i)).replace("'","")+'\n ')
    f.close()
def closure():
    f = open(base_dir+'/generated/aws/module/'+resource_name+'/resource.tf','a')
    f.write('}')
    f.close()
if resource_name == "ec2_instance":
    list = ['ami','instance_type','vpc_id','cidr_block','subnet_id','availability_zone']
elif resource_name == "vpc":
    list = ['assign_generated_ipv6_cidr_block','cidr_block','instance_tenancy','Name']
elif resource_name == "subnet":
    list = ['cidr_block','Name','vpc_id']
elif resource_name == "ebs":
    list = ['availability_zone','size','type']
elif resource_name == "rds":
    list = ['subnet_ids']
elif resource_name == "cloudwatch":
    list = ['description','event_pattern','name']
replacements = []
i=1
for var in list:
    for line in file:
        if var in line:
            replace_string = identify1(line)
            variable(var,i)
            replace1(replace_string,i)
            replace_string = identify(line)
            replace(replace_string,i)
            modify_modules(var,i)
            create_var(var,i)
            i+=1
            replacements.append(var)
closure()
print('Attributes replaced:', replacements)
