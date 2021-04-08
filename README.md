# zaheeb-shamsi-SDE-Backend-Assignment-Solution
Serverless AWS Instance Scheduler: The solution containes of 3 files: 
1. **aws_lambda_requests.py** : Use the request module to perform action on a pre-deployed API on AWS and fetch the response. 
2. **ec2.json** : The json by the user. 
3. **lambda_function.py** :  The function which will run on AWS and will perform EC2 start and stop function. 

The steps involved for the setup are as follows: 
1. Create an EC2 instance on AWS and get the InstanceID for that instance. 
2. Create a lambda function and copy the code which is in **lambda_function.py**
3. Connect that lambda function with the API Gateway and define the httpMethod type and resource type and then deploy the API.
4. Use the code in **aws_lambda_requests.py** to run from the local machine after preparing inputs in the json. 


