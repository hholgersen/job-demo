# Launch a k8s Job

This repo consists of 3 things:
- a python-script `main.py` that spins up a k8s job on the current cluster
- a `Dockerfile` that builds the docker image with the python script
- a deployment spec, `deployment.yaml` that launches the image built from the `Dockerfile`.

Currently, the deployment refers to a pre-built openly available version of the docker image that was built from the Dockerfile. You may want to build this yourself, instead of just running random containers found on the internet.

If you change namespace, remember to change the python-script as well.