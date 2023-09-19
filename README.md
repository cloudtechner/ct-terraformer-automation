#Terraformer- Write Back your Infrastructure to Code

**Overview**
The Terraformer utility is a tool designed to simplify the process of generating Terraform configuration files from existing cloud resources. With Terraformer, you can easily import cloud resources into your Terraform projects, making it easier to manage your infrastructure as code.

**Features**
1.	Import existing cloud resources into Terraform configuration files.
2.	Supports multiple cloud providers, including AWS, Azure, Google Cloud, and more.
3.	Generate Terraform code for various resource types, such as virtual machines, databases, and networking components.
4.	Automate the creation of Terraform configurations based on existing cloud resources.

**Prerequisites**
Before using Terraformer, ensure that you have the following prerequisites installed:

1.	Support terraform 0.13 (for terraform 0.11 use v0.7.9).
2.	Go (if building from source)

**Installation**
You can install Terraformer using one of the following methods:
Note : Both Terraformer and a Terraform provider plugin need to be installed.

**From Source :**
1. Run git clone <terraformer repo> && cd terraformer/
2. Run go mod download
3. Run go build -v for all providers OR build with one provider go run build/main.go {google,aws,azure,kubernetes,etc}

**From Releases:**
•	**Linux**

    export PROVIDER={all,google,aws,kubernetes}
    curl -LO "https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-${PROVIDER}-linux-amd64"
    chmod +x terraformer-${PROVIDER}-linux-amd64
    sudo mv terraformer-${PROVIDER}-linux-amd64 /usr/local/bin/terraformer

 
•	**MacOS**

    export PROVIDER={all,google,aws,kubernetes}
    curl -LO "https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-${PROVIDER}-darwin-amd64"
    chmod +x terraformer-${PROVIDER}-darwin-amd64
    sudo mv terraformer-${PROVIDER}-darwin-amd64 /usr/local/bin/terraformer


•	**Windows**

1.	Install Terraform - https://www.terraform.io/downloads
2.	Download exe file for required provider from here - https://github.com/GoogleCloudPlatform/terraformer/releases
3.	Add the exe file path to path variable


**Usage of Terraformer command :**

  terraformer import aws --resources=vpc,subnet,security-group

**Usage of Terraformer Script :**

Once you are done with all the installation steps and pre requisites. Follow the below steps :
1.	Open the terminal 
2.	Run the terraformer-automation.py script for the resources for which you want the code (script includes the user inputs)
3.	Once the script is complete you will see the directory with the name of the resources. The directory structure will be like the below:
generatedname of the provider e.g aws  resource name  tf files
        
4.	If you have imported code for more than one resource then you have to merge the state file for both of the resources using the below command.
	Run tfmv.sh file  like the below :
./tfmv.sh “name of the resource in which you want to merge “ “name of the resource which you want to merge”



