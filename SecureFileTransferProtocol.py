import numpy as np
import pandas as pd
import pysftp
import shutil

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Connecting with remote fileserver~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection('HOST', username='%username%', password='%password%', cnopts = cnopts) as sftp:
  with sftp.cd('%source folder path%)':
    sftp.get(r"%source filename%", r"%Target folder path and filename%"), preserve_mtime = True)

#For exampls, If the file is csv
file_dataframe = pd.read_csv('%file_name%', encoding = '%encoding of the file%', delimiter = '%delimiter%', keep_default_na = False)



#~~~~~~~~~~~~~~~~~If the file is present on Local Network Windows Network Access Shared (NAS)~~~~~~

source_path = r"%path of the NAS drive%"
dest_path = r"%Path of the target folder on your local%"
shutil.copyfile(source_path, dest_path)


#~~~~~~~Time to play with your data !~~~~~~~~~
