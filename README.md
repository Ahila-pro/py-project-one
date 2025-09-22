# Number to Words
A simple Python script to convert a number into its corresponding English words.

## Description
This script converts a given number into words. For example, the input 123 will be converted to "One Two Three".

## Required Modules
• Python 3.x
This script uses only the standard library, so no additional installations are necessary.



## ▶️ How to Run the Script
1. Clone the Repository:
   ```
   git clone https://github.com/ShravanDalavi/Simple-Python-Mini-Projects.git
   ```
2. Navigate to Directory:
   ```bash 
          cd Simple-Python-Mini-Projects/Number\ to\ Words
   ```
3. Run the Script:
   ```bash 
       python number_to_words.py
   ```

4. Follow the Prompt: 


Enter a number when prompted, and the script will output the number in words.
---------------------
# LAB STEPS:
1. All files creation , az login,
2. docker build -t numbertoword .
3. docker push ahilashoba/numbertoword:latest
4. docker images
5. docker run -it -p 5000:5000 numbertoword
6. Check in browser
7. create container registry in portal



# Container app needs container environment
8. az containerapp env create --name myContainerEnvtwo --resource-group python-rgp --location SouthIndia
# Authentication ACR
9. az acr login --name pythonahiregistry
10. az acr credential show --name pythonahiregistry --resource-group python-rgp
11. az acr update -n pythonahiregistry --resource-group python-rgp --admin-enabled true


# Push docker image into container registry
12. docker build -t pythonahiregistry.azurecr.io/numbertoword:latest .
13. docker push pythonahiregistry.azurecr.io/numbertoword:latest
14. docker tag numbertoword pythonahiregistry.azurecr.io/numbertoword:latest
15. az acr list  --resource-group python-rgp --output table
# Container App Creation:
13.  az containerapp env list --resource-group python-rgp --output table
# Take pw from step 14.
14. az acr credential show -n pythonahiregistry --resource-group python-rgp

15. az containerapp create --name numbertoword-app --resource-group python-rgp --environment myContainerEnvtwo --image pythonahiregistry.azurecr.io/numbertoword:latest --target-port 5000 --ingress external --registry-server pythonahiregistry.azurecr.io --registry-username pythonahiregistry --registry-password 34tlVzfA9Ay


# ---------------------------
Simple Az login workflow commands
# create application for service principal
1. az ad sp create-for-rbac --name "my-github-sp" --sdk-auth
# Assign role assignment to this service principal at subscription level
2. az role assignment create --assignee <appId-of-your-SP>  --role Contributor --subscription <your-subscription-id>

az role assignment create --assignee 3e1330f1 --role Contributor --scope /subscriptions/8ca97cad

az role assignment create --assignee 3e1330f1 --role Contributor  --scope /subscriptions/8ca97cad


3 . check in azure portal -> entra id -> iam -> select user and check application mapped with user.


