# import the base image from Docker Hub 
# it is a lightweight version of the official Python image
# the slim is a tag that specifies the version of the image

# FROM node:12-slim
FROM python:3.9

# set the working directory in the container

COPY . .

RUN apt update
RUN apt install nodejs npm -y

# install dependencies
# RUN is used to execute any command in a new layer on top of the current image and commit the results

RUN pip install -r requirements.txt

RUN npm start

# the command to run on container start

CMD ["npm" ,"start,""&","python3", "main.py"]
