#!/usr/bin/env python

"""
Parse every FATSA record from a line and print
"""

import sys

class FASTAReader(object):
    
    def __init__(self,input_file):
        self.file=input_file
        self.last_ident=None
    def __iter__(self):
        return self
        
    def next(self):
        #If this is the first call
        if self.last_ident is None:
            
            line=self.file.readline()
            assert line.startswith(">")
        #Extract   identifier
            ident=line.split()[0].lstrip(">")
        #ident=line.split()[0][1:]
        #If we have been called before /seen a sequence before
        else:
            ident=self.last_ident
        sequences=[]

        while True:
            line=self.file.readline().rstrip("\n\r")
            if line.startswith(">"):
                self.last_ident=line.split()[0][1:]
                break
            elif line=="":
                raise StopIteration
            else:
                sequences.append(line)
        
        
        return ident, "".join(sequences)
 
reader=FASTAReader(sys.stdin)
        
for ident, sequence in reader:
    print ident, sequence