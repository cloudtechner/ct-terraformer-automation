# Terraformer- Write Back your Infrastructure to Code


#### Usage of Terraformer command :
```
terraformer import aws --resources=vpc,subnet,security-group
```
#### Merge state Scipt:

Suppose you have imported the code for 2 resources i.e ec2 and vpc now you have to merge the terraform.tfstate file for both of the resources . You can use the tfstate-merg.sh script to merge the state file. 
##### Script Usage
```
sh tfstate-merge.sh “name of the resource in which you want to merge“  “name of the resource which you want to merge”
```
Example: Run the script from parent directory with ec2 as source and vpc as target

```
sh tfstate-merge.sh ec2_instance vpc
```

#### Terraformer Script :

Once you are done with all the installation steps and pre requisites. Follow the below steps :
1.	Open the terminal
2.  Install all the pre-requisites to run the python script(You can use the requirement.txt file).
3.	Run the terraformer-automation.py script for the resources for which you want the code (script includes the user inputs)
4.	Once the script is complete you will see the directory with the name of the resources. The directory structure will be like the below:
generated/name of the provider e.g aws/resource name/tf files
##### Script Usage :
``` 
python3 terraformer-automation.py
```



