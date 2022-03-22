'''
UF aes 2022
Script for writing multiple sfz files from metadata.
Expected input will be a csv with the general header:
filename	pitch	instrument	start end
'''



import pandas as pd
class sfz_writer:
  def __init__(self,instrument,data_dir):
    self.instrument = instrument
    self.data_dir = data_dir
  def write_header(self):
    with open(f'{self.instrument}.sfz', 'w') as f:
      f.write(
          f"""
          <control>\n default_path={self.data_dir}/\n
<global>
// parameters that affect the whole instrument go here.

// *****************************************************************************
// Your mapping starts here
// *****************************************************************************
          
          """
      )