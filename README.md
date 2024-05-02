# MSNnetwork
Code for simulation of a striatal MSN network model.

Install the Python NetPyNE environment, as described here:  
https://www.netpyne.org/documentation/installation

In short: 

conda create -n "mynetpyne" python=3.7
conda activate mynetpyne
pip install neuron
pip install netpyne

Download the code into a single directory.
In the same directory compile the mod files on the command line : 
nrnivmodl mechanisms

To execute as mpi process:
Set the number of cores, 'numprocs' in t42_batch.py
Then on the command line : nrniv -python t42_batch.py
Simulations will be started for each of the grid of parameter sets in t42_batch.py
Each simulation will be given numprocs processes. 
A directory 't42_data' will be created with the output files.
Remove or rename this directory to run the code again.

To run a single simulation on a single core:
nrniv -python t42_init.py
In this case output files will be in the same directory.

