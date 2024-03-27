# Industry-Safety-Detection-using-Yolov7




[Data Link](https://drive.google.com/file/d/1ncxeLuWEMXkXVI79LXbA38s-Ij0d2q4E/view)

[Yolo Repository](https://github.com/WongKinYiu/yolov7)

## Workflows
1. constants
2. config_entity
3. artifact_entity
4. components
5. pipeline
6. app.py

## AWS Configurations
```bash
#aws cli download link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

aws configure
```


## How to Run
```bash
conda create -n safety python=3.8 -y
```
```bash
conda activate safety
```
```bash
pip install -r requirements.txt
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/yolov7app


## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:


	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade

	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

