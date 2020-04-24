# STA9760_bigdata1 - Part 1


## Project Overview

In this project, we are building docker container which contains python code to pull data from NYC Opendata.
- (NYC parking and Camera Violations)

### Requirements

* Github Account
* Dockerhub Account
* AWS account -- to test on EC2 machine
* App_key  ---> https://data.cityofnewyork.us/login


#### To run container from DockerHub, run the commands below in terminal:

* ~$ apt install docker.io -> (install)
* ~$ docker login --username={your username} -> (login)
* ~$ docker pull cemdavran/bigdata1:3.0  (Pulling container from Dockerhub)
* ~$ docker run -e APP_KEY={App_key} -v $(pwd):/app/outputs -it cemdavran/bigdata1:3.0 python main.py --page_size={input for number of records per page} --num_page={input for number of pages per run} --output=./outputs/{output filename with format} -> (run docker)

To run our commands in EC2, we need to add "sudo" to beginning of our commands. 

  * App_key     -  App token from NYC OpenData 
  * --page_size -  Number of Records per page -> required input
  * --num_page  -  Number of page calls per run. It will run till the last record per run if we don't give this input -> optional input
  * --output    -  Output file (name.format) to save the result data to a file. If not given, output will be written to stdout. -> optional

#### Running container from Github;
Download copy of all files to local folder and run the commands below,

* ~$ docker build -t {Dockername}:version (to build docker container)
* ~$ docker run -e APP_KEY={App_key} -v $(pwd):/app/outputs -it {Dockername}:version python main.py --page_size={input for number of records per page} --num_page={input for number of pages per run} --output=./outputs/{filename.format} (run container)
