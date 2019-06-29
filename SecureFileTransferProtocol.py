import numpy as np
import pandas as pd
import pysftp

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Connecting with remote fileserver~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection('HOST', username='%username%', password='%password%', cnopts = cnopts) as sftp:
  with sftp.cd('%source folder path%)':
    sftp.get(r"%source filename%", r"%Target folder path and filename%"), preserve_mtime = True)

#For exampls, If the file is csv
file_dataframe = pd.read_csv('%file_name%', encoding = '%encoding of the file%', delimiter = '%delimiter%', keep_default_na = False)

#~~~~~~~Time to play with your data !~~~~~~~~~
