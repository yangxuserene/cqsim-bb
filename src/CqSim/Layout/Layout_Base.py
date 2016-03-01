# The abstract base class for network layout conversion
# Classes derived from this must implement the following methods:
#   convert_from_idx:
#     Takes a node index and relevant arguments and returns the coordinates
#     of that node in the system.
#   convert_to_idx():
#     Takes the coordinate of a node and relevant arguments and returns the
#     index of that node in the original list

from abc import ABCMeta, abstractmethod

class Layout_Base:
  __metaclass__ = ABCMeta

  @abstractmethod
  def convert_from_idx(self):
    pass

  @abstractmethod
  def convert_to_idx(self):
    pass

