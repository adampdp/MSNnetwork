from neuron import h

class mahonCell:
  def __init__ (self,ID=0,ty=0,col=0,poflag=0):
    self.ID=ID
    self.ty=ty
    self.col=col
    self.poflag=poflag
    self.initsoma()  #init soma params
  
  def initsoma (self):
 
    chanList = [
	'Nam',
	'Km',
	'Leakm',
	'Kirm',
	'KAfm',
	'KAsm',
	'Krpm',
	'NaPm',
	'NaSm']
    
   
    self.soma = h.Section()
    self.soma.diam = 5.6419
    self.soma.L = 5.6419
    self.soma.nseg = 3
    self.soma.Ra = 1
    for chan in chanList:
        self.soma.insert(chan)
        

  
