#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:11:47 2023

@author: adam
"""

from sbi import utils as utils
import numpy as np
import torch
import pandas as pd
import math

parameter_names = ['msn_msn_basewei', 'alvsomaclampampoff', 'seedval']

#prior_min = [0.002, math.log(1)]
#prior_max = [0.02, math.log(100)]
prior_min = [0.002, 0.000]
prior_max = [0.02, 0.00002]

prior = utils.torchutils.BoxUniform(
        low=torch.as_tensor(prior_min), high=torch.as_tensor(prior_max))

x = prior.sample((50,))

for x1 in x:
    print(x1[1].item())
#y = np.exp(x[:,1])    

xnp = x.numpy()
rr = np.random.randint(1,99999,xnp.shape[0])
xnp2 = np.hstack((xnp,np.atleast_2d(rr).T))
    
df2 = pd.DataFrame(xnp2, columns=parameter_names)    
df2.to_csv('params.csv', index = False)
df3 = pd.read_csv('params.csv')
df3n = df3.to_numpy()
