# Syntaxnet Playground
A short and simple python implementation for Google's Syntaxnet.
Written for the class "Natural Language Toolkits" at the Universty of Tübingen in the winter semester 2017/18.

### Getting started

The purpose of this tutorial is to utilize Syntaxnet's ParseyMcParseface within a python script. This is why we are going to use the docker image provided by Brian Low, instead of the official one from Google. Google's official docker release contains also the DRAGNN framework used for training new parsing models.
While this is certainly intriguing to look into, it doubles the image in size to 4.5 GB.

To get started, we need to install docker, which is available for Windows, MacOS and various Linux distributions. After we have done that, we run the following command in the console:

`$ docker pull brianlow/syntaxnet-docker`  

This will pull the image from the docker-hub and let us setup a container with an instance of Syntaxnet. The download make a while, after it is finished however, we will continue with:

`$ docker run --rm --name syntaxnet -i -t brianlow/syntaxnet-docker bash`  

Now, I want to mention, that `--rm` causes docker to setup a temporary container, which will be deleted automatically, after we stop it. If you wish to have a persistent docker-container with Syntaxnet, just ommit `--rm`.
`--name syntaxnet`, as you might already have guessed gives the contaienr the name "syntaxnet". You might choose whatever name feels right to you, it is even possible to omit the `--name` part. Docker will then provide a generated name.
After we ran the above command, we will be automatically logged into the docker container. 

To verify that everything is setup as it is supposed to, we run  
`$ echo "I'm sorry Dave, I'm afraid I can't do that" | syntaxnet/demo.sh`

This should, among a lot of debugging-messages, show us a dependency three of the provided sentence.

### How to receive output to work with in our script



### Copying with docker

You may copy something into or out form a container. Keep in mind that is only possible to do this with a temporary container, while it is running.  

`$ docker cp YOUR_FILE CONTAINER_NAME:/root/models/syntaxnet/`  
This wil copy the file into the directory you will be in, when you start the brianlow/syntaxnet-docker image.

`$ docker cp CONTAINER_NAME:/root/models/syntaxnet/YOUR_FILE .'`  
This will copy YOUR_FILE from the location /root/models/syntaxnet to the current location in your terminal.
