# Syntaxnet Playground
A short and simple python implementation for Google's Syntaxnet.
Written for the class "Natural Language Toolkits" at the Universty of Tübingen in the winter semester 2017/18.


### Copying with docker

You may copy something into or out form a container. Keep in mind that is only possible to do this with a temporary container, while it is running.  

`$ docker cp YOUR_FILE CONTAINER_NAME:/root/models/syntaxnet/`  
This wil copy the file into the directory you will be in, when you start the brianlow/syntaxnet-docker image.

`$ docker cp CONTAINER_NAME:/root/models/syntaxnet/YOUR_FILE .'`  
This will copy YOUR_FILE from the location /root/models/syntaxnet to the current location in your terminal.
