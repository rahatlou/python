#!/usr/bin/python
import os, sys

mypath = "."

files = os.listdir(mypath)
files.sort()
fname = 'test.html'

if len(sys.argv)> 1:
 fname  = sys.argv[1] + '/' + fname
 print 'creating ', fname, ' in ', str(sys.argv[1])
else:
 print 'creating ', fname, ' in current directory'
 
out = open("test.html","w+")

out.write( '<html>\n' )
out.write( '  <body>\n' )
out.write( '    <ul>\n' )

for f in files:
  if f.endswith(".cpp") or f.endswith(".cc") or f.endswith(".h"):
    out.write( '       <li><a href=' + f + '>' + f + '</a></li>\n' )


out.write( '    </ul>\n' )
out.write( '  </body>\n' )
out.write( '</html>\n' )
