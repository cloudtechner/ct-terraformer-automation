# Terraformer- Write Back your Infrastructure to Code


#### Usage of Terraformer command :
```

  terraformer import aws --resources=vpc,subnet,security-group
```
#### Usage of Merge state Scipt:

Suppose you have imported the code for 2 resources i.e ec2 and vpc now you have to merge the terraform.tfstate file for both of the resources . You can use the tfstate-merg.sh script to merge the state file . 

##### Script Usage
```
sh tfstate-merge.sh “name of the resource in which you want to merge“  “name of the resource which you want to merge”
```
Example: Run the script from parent directory with ec2 as source and vpc as target

```
sh tfstate-merge.sh ec2_instance vpc
```

#### Usage of Terraformer Script :

Once you are done with all the installation steps and pre requisites. Follow the below steps :
1.	Open the terminal 
2.	Run the terraformer-automation.py script for the resources for which you want the code (script includes the user inputs)
3.	Once the script is complete you will see the directory with the name of the resources. The directory structure will be like the below:
generated/name of the provider e.g aws/resource name/tf files
        
4.	If you have imported code for more than one resource then you have to merge the state file for both of the resources using the below command.
	Run tfmv.sh file  like the below :
./tfmv.sh “name of the resource in which you want to merge “ “name of the resource which you want to merge”



