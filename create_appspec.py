import yaml
import sys
import boto3

#session = boto3.Session(profile_name="Admin", region_name="us-east-1")
session = boto3.Session(region_name="us-east-1")

client = session.client("lambda")

with open("AppSpecTemplate.yaml") as file:
    app = yaml.load(file, yaml.FullLoader)

function_name = sys.argv[1]
function_alias = sys.argv[2]
output_file = sys.argv[3]

response = client.get_alias(FunctionName=function_name,
                 Name=function_alias)

AWS_ACCOUNT_ID = sys.argv[4]
AWS_DEFAULT_REGION = sys.argv[5]
IMAGE_TAG = sys.argv[6]

imageUri = f"{AWS_ACCOUNT_ID}.dkr.ecr.{AWS_DEFAULT_REGION}.amazonaws.com/equation_solver:{IMAGE_TAG}"
target = client.update_function_code(FunctionName=function_name,
                               ImageUri=imageUri,
                               Publish=True)

properties = app["resources"][0]["LambdaFunctionLogicalId"]["properties"]

properties["name"] = function_name
properties["alias"] = function_alias

properties["currentversion"] = int( response["FunctionVersion"] )
properties["targetversion"] = int( target["Version"] )

with open(output_file, "w") as file:    
    yaml.dump(app, file)

