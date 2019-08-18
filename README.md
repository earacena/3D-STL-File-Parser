# 3D STL File Format Parser
### Author
Emanuel Aracena

### Date Created
June 14, 2019

## Description
This python script is a parser for .stl files that generates and renders a 3D wireframe for display.
### Dependencies
PyGame, Python3, PyOpenGL
### Usage
Once all the dependencies are installed, run the following (preferably in a virtual environment):

`python3 stl_parser.py file.stl`

The Sphericon.stl file is a example file included from the [STL format wikipedia page](https://en.wikipedia.org/wiki/STL_%28file_format%29). 
To try it out type:

`python3 stl_parser.py Sphericon.stl`

To use the included virtual environment with dependencies installed, make sure to have the `virtualenv` package installed. If not type (using pip3):

`pip install virtualenv`

Then in the folder with the project files, type:

`source 3dv_env/bin/activate`

The terminal line should now have a `(3dv_env)` preceeding it, now simply follow the instructions above to run the script.
