#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:49:32 2023

@author: adam
"""

from netpyne import specs
from netpyne.batch import Batch

#froam neuron import h
#h.nrnmpi_init()

def batchTauWeight():

    params = specs.ODict() 
    numprocs = 12
    seedbase = 576521
   
    params['seedval'] = list(range(0 + seedbase, 100 + seedbase, 100)) 
    #params['alvsomaclampampoff'] =  [0.00001 + 0.00001*x for x in range(0,30,2)]
    params['alvsomaclampampoff'] =  [0.00001]
    #params['msn_msn_basewei'] = [x*0.0001 for x in [0.25,0.5,1,1.5,2,2.5,3,4,5]]
        
      
    
    b = Batch(params=params, cfgFile='t42_cfg.py', netParamsFile='t42_netParams.py',)

        # Set output folder, grid method (all param combinations), and run configuration
    b.batchLabel = 't42'
    b.saveFolder = 't42_data'
    b.method = 'grid'
    
    doslurm = False
    if doslurm:
    
        b.runCfg = {    'type': 'hpc_slurm',
                        #'type': 'mpi_bulletin',
                            'mpiCommand': 'srun',
                            'custom': '#SBATCH --constraint=mc\n#SBATCH --partition=normal',
                            'allocation': 'ich002',
                            'nodes': 1,
                            'coresPerNode': 35,
                            'script': 't42_init.py',
                            'walltime': '23:30:00',
                            'skip': True}
    else:
   
# =============================================================================
#     b.runCfg = {  'type': 'mpi_bulletin',
#                         'script': 't2_init.py',
#                         'skip': True}
# =============================================================================
      
        b.runCfg = {  'type': 'mpi_direct',
                'cores': numprocs,
                'mpiCommand': 'mpiexec --use-hwthread-cpus',
                        'script': 't42_init.py',
                        'skip': True}
    
    

    # Run batch simulations
    b.run()
    #h.quit()
# Main code
if __name__ == '__main__':
        batchTauWeight()
        import sys
        sys.exit()
