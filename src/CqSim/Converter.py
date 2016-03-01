"""
Provides API for network layout conversion

Description of API calls:
  coords = convert_from_idx(type, **kwargs):
  idx    = convert_to_idx(type, **kwargs):

  where type   is the layout to be converted to/from
        idx    is the index of the original node
        coords is the coordinates of the node in the specified layout
        and kwargs is the dictionary of arguments to be provided to the converter
"""

from Layout import Hilbert2D
from Layout import Hilbert3D
from Layout import Cartesian

class Converter(object):
  def __init__(self):
    self.converters = { 'Hilbert2D': Hilbert2D.Hilbert2D,
                        'Hilbert3D': Hilbert3D.Hilbert3D,
                        'Cartesian': Cartesian.Cartesian }

  def convert_from_idx(self, layout, **kwargs):
    return self.converters[layout].convert_from_idx(**kwargs)

  def convert_to_idx(self, layout, **kwargs):
    return self.converters[layout].convert_to_idx(**kwargs)

if __name__ == '__main__':
  c = Converter()
  for i in range(32):
    args = {'index': i, 'dims': [2, 3, 4, 2]}
    coords = c.convert_from_idx('Cartesian', **args)
    print coords
  args = {'coords': [0, 1, 1, 0], 'dims': [2, 3, 4, 2]}
  print c.convert_to_idx('Cartesian', **args)
