import os

LINE_KEY = "LINE_NUMBER"

class RaveBot( object ):
    
    def generate( self ):

        pth_text = os.path.dirname( os.path.realpath(__file__) )
        pth_text = os.path.join( pth_text, "burning.txt" )
        fh = open( pth_text )
        lines = fh.readlines()
        fh.close()

        idx_line = int( os.environ.get( LINE_KEY, "0" ) )
        next_line = lines[ idx_line ].rstrip()

        next_index = idx_line+1
        if next_index >= len( lines ):
            next_index = 0

        os.environ[ LINE_KEY ] = str(next_index)
        return next_line

# commandline testing stub
if __name__ == '__main__':
    b = RaveBot()
    while True:
        print "'%s'" % b.generate()
        raw_input()