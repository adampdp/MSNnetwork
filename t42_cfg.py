#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:45:59 2023

@author: adam
"""

from netpyne import specs

## Population parameters
cfg = specs.SimConfig()				

cfg.duration = 10000
cfg.starttime = 0
cfg.seedval = 42

cfg.msnpopsize = 100

cfg.cvode_active = True
cfg.dt = 0.025
cfg.hParams = {'v_init': -65, 'celsius': 34} #, 'clamp_resist': 0.001}
cfg.verbose = False

cfg.distributeSynsUniformly = False
cfg.connRandomSecFromList = True

cfg.recordStep = 1 			
cfg.savePickle = False 	
cfg.saveFileStep = 1000


cfg.alvsomaclampamp = 0.001305
cfg.alvsomaclampampoff = 0.00001
cfg.alvclamptarg = 'MSN'


cfg.msn_msn_basewei = 0.006 
cfg.msn_msn_conprob = 0.4
cfg.msn_msn_synfact = 1
cfg.msn_msn_synmech = 'eckgaba'



cfg.eckgaba_use  = 0.41
cfg.eckgaba_dep = 222
cfg.eckgaba_fac = 1859


cfg.gaba_syn_rev = -85
cfg.tau_gaba = 20

cfg.analysis['plotRaster'] = { 
                              'include': ['MSN_pop'],
                                    'marker': 'o',
                                    'saveFig': True, 
                                    'showFig': False, 
                                    'markerSize': 6}


cfg.recordTraces['V_soma'] = {'sec':'soma','loc':0.5,'var':'v'}

cfg.analysis['plotTraces'] = { 
                                        'include': list(range(5)), 
                                        'saveFig': True, 
                                        'showFig': False,
                                 
                                        } # Plot cell traces 

    
cfg.saveJson = True
cfg.seeds = {'conn': int(cfg.seedval + 7515), 'stim': int(cfg.seedval + 84331), 'loc': int(cfg.seedval + 943)}
