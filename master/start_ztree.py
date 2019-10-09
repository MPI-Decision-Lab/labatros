import questionary
import os
import psutil
import lm_functions
import subprocess
import sys

ztree_path = r"C:\labserver\progs\ztree"
settings_path = r"L:\settings\ztree"
fontsize_filename = "fontsize.txt"
version_filename = "version.txt"

default_fontsize = 12
min_fontsize = 6
max_fontsize = 72

fontsize_input = questionary.text(f"Please enter font size in pt [or press ENTER for the default {default_fontsize} pt]: ").ask()


try:
    fontsize = int(fontsize_input)
except:
	print("not a proper size. will use the default")
	fontsize = default_fontsize


if not (min_fontsize < fontsize < max_fontsize):
    print(f"You can only use a font size between {min_fontsize} and {max_fontsize}.")
    fontsize = default_fontsize

print(fontsize)

directory_list = os.listdir(ztree_path)[::-1] # This reverses the list order


from prompt_toolkit.styles import Style

custom_style_fancy = Style([
#    ('qmark', 'fg:#673ab7 bold'),       # token in front of the question
   ('question', 'bold'),               # question text
#    ('answer', 'fg:#f44336 bold'),      # submitted answer text behind the question
    ('pointer', 'fg:#FFFF00 bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#FFFF00 bold'), # pointed-at choice in select and checkbox prompts if use_pointer=False
    ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
#    ('separator', 'fg:#cc5454'),        # separator in lists
#    ('instruction', ''),                # user instructions for select, rawselect, checkbox
#    ('text', ''),                       # plain text
#    ('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
])

version = questionary.select(
    "Please select z-Tree version.",
    choices=directory_list, style=custom_style_fancy).ask()  # returns value of selection

	
with open(os.path.join(settings_path,fontsize_filename),"w+") as fontsize_file:
    fontsize_file.write(str(fontsize))
with open(os.path.join(settings_path,version_filename),"w+") as version_file:
    version_file.write(str(version))
	
ztree_runcommand = 'C:\\labserver\\progs\\ztree\\' + str(version) + '\\ztree.exe'

if lm_functions.process_exists('ztree'):
    print("zTree is already running")
else:
   # os.system(ztree_runcommand)
   pid = subprocess.Popen([ztree_runcommand])
   
   # if you want to print output
   #pid.wait()
   #print pid.stdout
        