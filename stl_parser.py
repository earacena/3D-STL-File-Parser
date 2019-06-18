#
# Author:       Emanuel Aracena
# Date Created: June 14, 2019
# Description:  A parser of ACSII .stl files.
#               The data will get put into an array following the pattern
#               described below.
#               First row, is facet normals, and the rest of the rows
#               are vertices.
#               Working as of June 18, 2019
import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import sys

def parse_ascii_stl_file(filename):
    # Pattern:    normals
    #             vertex 1
    #             vertex 2
    #             vertex 3
    with open(filename) as file:
        # Read file into iteratable array
        line = file.readlines()

        # Clean up unneeded labels
        line = [x.strip('\n') for x in line]
        line = [x.strip('   ') for x in line]
        filter = ['outer loop', 'endfacet', 'endloop', 'endfacet', 'endfacet', line[0], line[len(line)-1]]
        result = [a for a in line if a not in filter]
        result = [x.strip('facet normal ') for x in result]
        result = [x.strip('vertex ') for x in result]
        
        # Show results of parsing (currently a string of characters split by
        # individual objects using result[x].split(' '))
        # Use float(x) to cast after splitting in order to get proper float val
        return result

def prepare_stl_data(parsed):

    vertices = []
    edges = []

    # Take parsed data and store it appropriately into vertices using (x,y,z) values
    for i in range(0, len(parsed), 4):
        #print("normal: %s" % parsed[i].split(' '))
        split = parsed[i+1].split(' ')
        print("vert: %s" % split)
        vertices.append([float(num) for num in split])

        split = parsed[i+2].split(' ')
        print("vert: %s" % split)
        vertices.append([float(num) for num in split])
                    
        split = parsed[i+3].split(' ')
        print("vert: %s" % split)
        vertices.append([float(num) for num in split])

    print (vertices)

    # Since .stl does not specify, form edges as follows:
    #   v0 -> v1
    #   v1 -> v2
    #   v2 -> v0
    for x in range(0, len(vertices), 3):
        edges.append((x, x+1))
        edges.append((x+1, x+2))
        edges.append((x+2, x))

    print (edges)

    return vertices, edges
    
def main():
    # Initial window config
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set OpenGL perspective and camera placement, since most units in the test file
    # are in the triple to 4 digits, set appropriate distance away.
    gluPerspective(45, (display[0]/display[1]), 0.1, 5000.0)
    glTranslatef(0.0, 0.0, -4000)

    # Parse file and prepare data
    parsed = parse_ascii_stl_file(str(sys.argv[1]))
    vertices = []
    edges = []
    vertices, edges = prepare_stl_data(parsed)

    # pygame event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Render shape
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        pygame.display.flip()

# Call main
main()
