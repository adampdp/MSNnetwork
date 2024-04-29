#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:38:47 2023

@author: adam
"""
from netpyne import specs
import numpy as np
import random


try:
    from __main__ import cfg  # import SimConfig object with params from parent module
except:
    from t42_cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module


netParams = specs.NetParams()  
    

np.random.seed(int(cfg.seedval))
random.seed(int(cfg.seedval))
somator=True

if cfg.msnpopsize>0:

    netParams.importCellParams(label='MSN_rule', 
                               conds= {'cellType': 'MSN', 'cellModel': 'MSN'},
                               cellName = 'mahonCell',
          	fileName='mahonCell.py',    
              somaAtOrigin=somator)
    
    netParams.popParams['MSN_pop'] = {'cellType': 'MSN', 
                                       'numCells': cfg.msnpopsize, 
                                       'cellModel': 'MSN'}

netParams.synMechParams['eckgaba'] = {'mod': 'DetGABAAB', 
                                      'tau_d_GABAA': cfg.tau_gaba, 
                                          'Use': cfg.eckgaba_use, 
                                          'Dep': cfg.eckgaba_dep, 
                                          'Fac': cfg.eckgaba_fac,
                                          'e_GABAA' : cfg.gaba_syn_rev,
                                          }

basewei = cfg.msn_msn_basewei*0.25/cfg.msn_msn_conprob 
netParams.wei_hi = basewei*1.5
netParams.wei_lo = basewei*0.5

netParams.connParams['MSNToMSN'] = { 
        'preConds': {'pop': 'MSN_pop'},   
        'postConds': {'pop': 'MSN_pop'},  
        'probability': cfg.msn_msn_conprob,       
        'weight': 'uniform(wei_lo,wei_hi)',            
        'delay': 'uniform(1,3)', 
        'synsPerConn': cfg.msn_msn_synfact,
        'synMech': cfg.msn_msn_synmech}           

netParams.alvsomaclampamp = cfg.alvsomaclampamp
netParams.alvsomaclampampoff = cfg.alvsomaclampampoff

for msn in list(range(cfg.msnpopsize)):

    netParams.stimSourceParams['I1_' + str(msn)] = {'type': 'IClamp', 'del': 0, 
                                            'dur': cfg.duration, 
                                            'amp': 
            'uniform(alvsomaclampamp,alvsomaclampamp + alvsomaclampampoff)' }
            
    netParams.stimTargetParams['I1targ_' + str(msn)] = {'source': 'I1_' + str(msn), 
                                               'conds': {'pop': 'MSN_pop',
                                                         'cellList': [msn]}, 
          									   'sec': 'soma', 'loc': 0.5}
