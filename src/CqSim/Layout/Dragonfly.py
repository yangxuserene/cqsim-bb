from Layout_Base import Layout_Base

class Dragonfly(Layout_Base):

  @staticmethod
  def convert_from_idx(**kwargs):
    if ('index' not in kwargs) or ('glinks' not in kwargs) or ('rlinks' not in kwargs) or ('nodes' not in kwargs):
      print "Dragonfly: missing arguments!"
      return
    idx = kwargs['index']
    dims = []
    dims.append(kwargs['glinks']+1)
    dims.append(kwargs['rlinks']+1)
    dims.append(kwargs['nodes'])

    maximum = 1
    for i in dims:
      maximum *= i
    if idx >= maximum:
      print "Dragonfly: node index exceeds network capability!"
      return

    coords = []
    dims.reverse()
    for i in range(0, len(dims)):
      coords.append(idx%dims[i])
      idx //= dims[i]
    coords.reverse()
    return coords

  @staticmethod
  def convert_to_idx(**kwargs):
    if ('coords' not in kwargs) or ('glinks' not in kwargs) or ('rlinks' not in kwargs) or ('nodes' not in kwargs):
      print "Dragonfly: missing arguments!"
      return
    coords = kwargs['coords']
    dims = []
    dims.append(kwargs['glinks']+1)
    dims.append(kwargs['rlinks']+1)
    dims.append(kwargs['nodes'])

    idx = 0
    for i in range(0, len(dims)):
      idx *= dims[i]
      idx += coords[i]
    return idx
