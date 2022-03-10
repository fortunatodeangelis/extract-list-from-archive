# extract-list-from-archive
File list extractor contained in a compressed archive in hierarchical tree format

## Dependency installation
``$ pip install pymsgbox.``

## Run script
``$ python elfa.py C:/Your Directory/Your Archive.Extension.``

## Create .Exe from .py
#### if you want to use the program as an exe file and add it to the right context menu of Windows and use it at the click of the mouse and then have the result copied to the clipboard then follow the steps below

### Dependency installation
Install Auto Py To Exe
``$ pip install auto-py-to-exe.``

### Convert py to exe
Once the installation is complete, start from the terminal
``$ auto-py-to-exe.``
In script location add the .py file, select one file and windows based after a user interface will open where you can configure the final output, follow as in the figure:<br>
<span style="width:100%"><img width="473" alt="image" src="https://user-images.githubusercontent.com/45572072/157649297-6c310dc8-2e8b-4f70-8f5d-d8b6eb1e2345.png"></span>
<br><br>


### Add the rules to the registry
To use the windows right-click program you need to add information to the registry. First put the program folder under the C: / drive, for example C: /Elfa/Elfa.exe

create a reg.txt file in the same folder and write the following instructions in it:

```Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\*\shell\Copy List from Archive\command]
@="\"C:\\Elfa\\Elfa.exe\" \"%1\""
```

Now from powershell launch the following command to record the commands on the registry
`` $ reg.exe import C:\Elfa\reg.txt``

From this moment, whenever you want to extract the content in hierarchical text format on any archive compressed with the right button, the result will be automatically copied to the clipboard


