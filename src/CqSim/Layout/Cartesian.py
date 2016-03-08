from Layout_Base import Layout_Base

class Cartesian(Layout_Base):

  @staticmethod
  def convert_from_idx(**kwargs):
    if ('index' not in kwargs) or ('dims' not in kwargs):
      print "Cartesian: missing arguments!"
      return
    idx = kwargs['index']
    dims = kwargs['dims']

    maximum = 1
    for i in dims:
      maximum *= i
    if idx >= maximum:
      print "Cartesian: cannot fit index into matrix!"
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
    if ('coords' not in kwargs) or ('dims' not in kwargs):
      print "Cartesian: missing arguments!"
      return
    coords = kwargs['coords']
    dims = kwargs['dims']

    idx = 0
    for i in range(0, len(dims)):
      idx *= dims[i]
      idx += coords[i]
    return idx
