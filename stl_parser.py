#
# Author:       Emanuel Aracena
# Date Created: June 14, 2019
# Description:  A parser of ACSII .stl files.
#               The data will get put into an array following the pattern
#               described below.
#               First row, is facet normals, and the rest of the rows
#               are vertices.

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


parsed = parse_ascii_stl_file(str(sys.argv[1]))

# for i in range(0, 9, 2)
#      dosomething(i)

