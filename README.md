# SMIM-Extractor
Script to extract the Skyrim-Mod Static-Mesh Improvement mod. (For easier manual install)
##Disclaimer
This is an unofficial tool!
##Requirements
- Download [SMIM](http://www.nexusmods.com/skyrim/mods/8655/ "SMIM")
- [Python 3.x ](https://www.python.org/)
- 7zip, if you want to run it directly on the .7z-file (currently not recommended because of copy stability issues

##Usage
Run scripts with parameters:
- Input: SMIM (as .7z or extracted folder)
- Output: Output directory
- -z: Optional parameter to set a custom path for 7zip
A functional call could look like this:
```
python "C:\Downloads" "C:\MyFolder" -z "C:\CustomProgramFolder\7zip\7z.exe"
```
