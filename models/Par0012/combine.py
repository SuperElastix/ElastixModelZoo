#! /usr/bin/python

# Script combining forward and inverse TransformParameter files.
# (c) Coert Metz

import sys
import os

numarg = len(sys.argv)
if numarg < 7:
  # Print help message
  print ""
  print " Syntax: combine.py <type> <infile0> <infile1> <outfile0> <outfile1> <ref> [spacing=5000]"
  print ""
  print " Options: "
  print "   type:      determines the order in which the transforms are combined; options are:"
  print "              point: to transform points from the reference time point to all other time points"
  print "              image: to transform all time point images to the reference time point image frame"
  print "   infile0:   forward TransformParameters file."
  print "   infile1:   inverse TransformParameters file."
  print "   outfile0:  respaced forward/inverse TransformParameters file."
  print "   outfile1:  combined (respaced) forward and (respaced) inverse TransformParameters file."
  print "   ref:       reference timepoint index number."
  print "   spacing:   new spacing for respaced forward/inverse TransformParameters file [default=5000]."
  print ""
  exit( 0 )

type = sys.argv[ 1 ]
ref = float( sys.argv[ 6 ] )

if type == 'point':
  infile0 = sys.argv[ 3 ]
  infile1 = sys.argv[ 2 ] 
elif type == 'image':
  infile0 = sys.argv[ 2 ]
  infile1 = sys.argv[ 3 ]
else:
  print " The supplied type is not supported. Choose either 'point' or 'image'"
  print ""
  exit( 0 )

outfile0 = sys.argv[ 4 ]
outfile1 = sys.argv[ 5 ]


spacing = 5000.0
if numarg > 7:
  spacing = float( sys.argv[ 7 ] );

print ""
print "Combine forward and inverse TransformParameter files for '" + type + "' transformation."
print "  Using new spacing of " + str( spacing ) + " time points and reference time point " + str( ref )
print ""

# Check if parameter files exist
if not os.path.exists( infile0 ):
  print "ERROR: parameter file " + infile0 + " does not exist!"
  print ""
  exit( 0 );
if not os.path.exists( infile1 ):
  print "ERROR: parameter file " + infile1 + " does not exist!"
  print ""
  exit( 0 );

# Open parameter file 0 and search for GridSpacing and GridOrigin line
text_filein0 = open( infile0, "r" )
for line in text_filein0:
  if line.find( "(GridOrigin " ) == 0:
    origin_str = line
  elif line.find( "(GridSpacing " ) == 0:
    spacing_str = line
text_filein0.close()

# Extract time point origin from line
origin_split = origin_str.strip().split(' ')
origin_split = origin_split[ len( origin_split ) - 1 ].split(')')
old_origin = float( origin_split[ 0 ] )

# Extract time point spacing from line
spacing_split = spacing_str.strip().split(' ')
spacing_split = spacing_split[ len( spacing_split ) - 1 ].split(')')
old_spacing = float( spacing_split[ 0 ] )

print "Original grid origin in time dimension: " + str( old_origin )
print "Original grid spacing in time dimension: " + str( old_spacing )
print ""

# Determine new grid origin
new_origin = ref - ( spacing / old_spacing ) * ( ref - old_origin )
print "New grid origin in time dimension: " + str( new_origin )

# Recompose origin and spacing lines
new_origin_string = origin_str.strip().split(' ')
new_origin_string.pop()
new_origin_string = " ".join( new_origin_string ) + " " + str( new_origin ) + ")\n"
new_spacing_string = spacing_str.strip().split(' ')
new_spacing_string.pop()
new_spacing_string = " ".join( new_spacing_string ) + " " + str( spacing ) + ")\n"

# Reopen text file, replace origin and spacing and write to output file 1
text_filein0 = open( infile0, "r" )
text_fileout0 = open( outfile0, "w" )
for line in text_filein0:
  if line.find( "(GridOrigin " ) == 0:
    # Write new origin line
    text_fileout0.write( new_origin_string )
  elif line.find( "(GridSpacing " ) == 0:
    # Write new spacing line
    text_fileout0.write( new_spacing_string )
  elif line.find( "(InitialTransformParametersFileName " ) == 0:
    # Remove initial transform
    text_fileout0.write( "(InitialTransformParametersFileName \"NoInitialTransform\")\n" )
  else:
    # Write line read from input file (no change)
    text_fileout0.write( line )

# Replace initial transform parameter filename
text_filein1 = open( infile1, "r" )
text_fileout1 = open( outfile1, "w" )
for line in text_filein1:
  if line.find( "(InitialTransformParametersFileName " ) == 0:
    # Set initial transform filename
    text_fileout1.write( "(InitialTransformParametersFileName \"" + outfile0  + "\")\n" )
  else:
    # Write line read from input file (no change)
    text_fileout1.write( line )

