#TENSORFLOW Docker

#####To Begin

` $ make `

This will build a Docker image with Python 3.6 with name tensor-flow, start a container with tensor-flow, and start the shell in container.

` $ make shell `

This will start container's shell.


### Test file

base on : [http://web.stanford.edu/class/cs20si/lectures/notes_02.pdf](http://web.stanford.edu/class/cs20si/lectures/notes_02.pdf)

To run Test, in container shell,

` root@9612102567b5:/usr/src/app# python test1.py `

To start Tensorboard,

` root@9612102567b5:/usr/src/app# tensorboard --logdir="./graph" `

Navigate to your browser, and enter http://localhost:6006 (or IP address of docker machine)




