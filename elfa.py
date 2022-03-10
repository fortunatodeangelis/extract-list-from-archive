# Import
import zipfile
import subprocess
import sys
import os.path
import pymsgbox

# Edit Here
app_name = 'NAME APP'
allowed_ext = 'EXTENSION ARCHIVE'
allowed_ext_file = 'EXTENSION FILE'


# Check if exist arg in line
if(len(sys.argv[1:])) == 0:
    pymsgbox.alert('Nessun File Selezionato', app_name)
    sys.exit()

# check if arg in line has extension allowed
if sys.argv[1:][0].lower().endswith(allowed_ext) != True:
    pymsgbox.alert('Selezionare un file ' + allowed_ext, app_name)
    sys.exit()

# check if file exist
file_exists = os.path.exists(sys.argv[1:][0])
if(file_exists != True):
    pymsgbox.alert('Il File Non Esiste', app_name)
    sys.exit()

# zip file handler  
zip = zipfile.ZipFile(sys.argv[1:][0])

# Create tree for patten /root/parent/child/item
def create_tree(data, items):
    if len(items) == 1:
        if items[0] in data:
            return
        else:
            data[items[0]] = dict()
    else:
        if items[0] not in data:
            data[items[0]] = dict()
        create_tree(data[items[0]], items[1:])

# Create Plain tree from dictonary
def tree_to_plain(d, indent=0):
    res = ''
    for key, value in d.items():
      res += '  '  * indent + str(key) + "\n"
      if isinstance(value, dict):
        res += tree_to_plain(value, indent+1)
      else:
        res += '  ' * (indent+1) + str(value) + "\n"
    return res

# dict
out = dict()

# Iterate and add element to dictonary for create a tree
for item in zip.namelist():
     if allowed_ext_file in item:
        items = item.split("/")
        create_tree(out, items)
    
# Run subprocess for clip the result    
subprocess.run(['clip.exe'], input=tree_to_plain(out, indent=0).replace(allowed_ext_file, "").strip().encode('utf-8'), check=True)
pymsgbox.alert('Contenuto Copiato', app_name)
sys.exit()
