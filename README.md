# MSNnetwork
Code for simulation of a striatal MSN network model.

Install the Python NetPyNE environment, as described here:  
https://www.netpyne.org/documentation/installation

Download the code into a single directory.
In the same directory compile the mod files : nrnivmodl *mod

Then : nrniv -python t42_batch.py

A directory 't42_data' will be created with the output files.
Remove or rename this directory to run the code again.
