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

The next thing we are going to do is modify the output of the `demo.sh` script, so that it becomes easy to read into our python-script. As a first step, we will remove the debugging messages by modifying the line we run in the terminal:  

`$ echo "I'm sorry Dave, I'm afraid I can't do that" | syntaxnet/demo.sh 2>/dev/null`

Now we should only receive the sentence we provided and the corresponding dependency tree. The next step will be to change the output of the bash-script from a dependency tree to a table with the CoNLL format. Fortunately, Syntaxnet is already capable of doing that. The demo-script actually consists of a three-parts-pipeline and the last part transforms the CoNLL table into a dependency tree. All we therefore need to do is remove the last part of the pipeline within the demo.

To achieve this, copy the demo-script out of the container. See how to copy from an into a docker-container further down. After we copied the script, we will open it with our favorite text-editor (or IDE) and remove the last part of the pipeline. The resulting script is also part of this repository (`demo-conll.sh`). We will now copy the script back into the container and make it runnable (`chmod u+x demo-conll.sh`). Then we will verify that we achieved the intended result by running it against our example sentence. 

`$ echo "I'm sorry Dave, I'm afraid I can't do that" | ./demo-conll.sh 2>/dev/null`

This should give us the result:

```
1	I	_	PRON	PRP	_	4	nsubj	_	_
2	'm	_	VERB	VBP	_	4	cop	_	_
3	sorry	_	ADJ	JJ	_	4	nn	_	_
4	Dave	_	NOUN	NNP	_	0	ROOT	_	_
5	,	_	.	,	_	4	punct	_	_
6	I	_	PRON	PRP	_	8	nsubj	_	_
7	'm	_	VERB	VBP	_	8	cop	_	_
8	afraid	_	ADJ	JJ	_	4	parataxis	_	_
9	I	_	PRON	PRP	_	12	nsubj	_	_
10	ca	_	VERB	MD	_	12	aux	_	_
11	n't	_	ADV	RB	_	12	neg	_	_
12	do	_	VERB	VB	_	8	ccomp	_	_
13	that	_	DET	DT	_	12	dobj	_	_
```

Which is a table using the [CoNLL-U Format](http://universaldependencies.org/docs/format.html), a result that we should be able to read easily into our python-script.

### Using ParseyMcParseface within a small python-script

The provided python-script should suffice for some small experiments. It is very simple and just reads the CoNLL-table from the command-line into an object. It only supports the parsing of single sentences so far and is able to either print all provided features of the CoNLL-table, or only the pos-tags (both the universal and the language-specific one).
The script itself should, due to its rudimentary state, be pretty self-explanatory.

### Copying with docker

You may copy something into or out form a container. Keep in mind that is only possible to do this with a temporary container, while it is running.  

`$ docker cp YOUR_FILE CONTAINER_NAME:/root/models/syntaxnet/`

This wil copy the file into the directory you will be in, when you start the brianlow/syntaxnet-docker image.

`$ docker cp CONTAINER_NAME:/root/models/syntaxnet/YOUR_FILE .'`

This will copy YOUR_FILE from the location /root/models/syntaxnet to the current location in your terminal.
