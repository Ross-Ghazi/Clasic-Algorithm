   2020-11-30
 crate random array for inputs
  """

from random import randint
from time import time
def create_array(size=10,max=50):   # create random array as input
    return[randint(0,max)  for _ in range(size)]






