# Image-Style-Transfer-with-Serverless-API
Serverless API to add the job to the SQS and save Image to S3 waiting to be process by EC2 instance

To compile th docker image your self:

    sudo make build


To push to the docker hub:

    make upload


To run the docker file

    sudo docker run --runtime=nvidia -u $(id -u):$(id -g) -it create_music bash
    python predict.py


If your enviroment does not have NVIDIA GPU:

    sudo docker run -u $(id -u):$(id -g) -it create_music bash
    python predict.py


To take out the file, in an sepreate window run:

    sudo docker ps


find the docker's  CONTAINER ID  and run:

    sudo docker cp -r 'CONTAINER ID':/tmp/result /result

