from Layout_Base import Layout_Base

class Hilbert2D(Layout_Base):

  @staticmethod
  def convert_from_idx(**kwargs):
    if ('index' not in kwargs) or ('n' not in kwargs):
      print "Hilbert2D: missing arguments!"
      return
    d = kwargs['index']
    n = kwargs['n']
    rx=0
    ry=0
    s=1
    t=d
    x = y = 0
    while(s<n):
      rx = 1 & (t/2)
      ry = 1 & (t ^ rx)
      if ry==0:
        if rx == 1:
          x = s-1 - x
          y = s-1 - y    
        x,y = y, x
      x += s * rx
      y += s * ry
      t /= 4      
      s*=2

    return [x,y]

  @staticmethod
  def convert_to_idx(**kwargs):
    if ('coords' not in kwargs) or ('n' not in kwargs):
      print "Hilbert2D: missing arguments!"
      return
    coords = kwargs['coords']
    n = kwargs['n']
    x = coords[0]
    y = coords[1]
    rx=0
    ry=0
    d=0
    s=n/2
    while s>0:
      rx = (x&s)>0
      ry = (y&s)>0
      d += s*s*((3*rx)^ry)
      if ry==0:
        if rx == 1:
          x = n-1 - x
          y = n-1 - y    
        x,y = y, x
      s/=2

    return d
