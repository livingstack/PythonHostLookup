# PythonHostLookup
Short Python Based application that gets and prints the name of the host running inside the container
This application is python code that's "compiled" (not really) into an executable named "main" From here all the necesary python libraries to "build" the container are saved within "/dist/main" You can use these files to build a container using an open source tool like buildah or podman by doing something like the following example below: 

Example: "podman build . -t pythonhostlookup -f Dockerfile"

Assuming you have podman setup with a local registry, this will copy the resulting container into the registry, and can be viewed by running the command: "podman images"

which should result in this output:

"REPOSITORY TAG IMAGE ID CREATED SIZE"

"localhost/pythonhostlookup latest 33b82b0eb89b 4 minutes ago 95.1 MB"
