# Docker Equation Solver
We aim to create a Docker image of the [equation solver](https://github.com/MogomotsiFM/equation_solver) repository. The image is meant to be deployed as an AWS 
Lambda function. We use Docker multi-stage builds. This makes for lighter production images pushed in AWS Elastic Container Registry. We install git and other
required packages and then clone the code into the development stage. We also run unit tests in this stage. The built artifacts are then copied into the production 
stage.

Since we started working on the CICD [pipeline](https://github.com/MogomotsiFM/equation-solver-deployment-pipeline) to deploy the resultant image, we have also included buildspec.yaml and appspec.yaml files in this repository.  
