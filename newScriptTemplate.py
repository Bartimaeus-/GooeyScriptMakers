from gooey import Gooey
from gooey import GooeyParser

import os

# Script execution goes here
def runCommand(args):
    inputFiles = args.inputFiles
    for inputFile in inputFiles:
    
        if args.outputFileName != '':
            outputFileName = args.outputFileName
        else:
            outputFileName = 'output_' + inputFile #prefix
            # suffix (line below)
            # outputFileName = os.path.splitext(inputFile)[0] + '_output' + os.path.splitext(inputFile)[1]

# Put initialization for the 
def initGooey(parser):
    
    parser.add_argument('inputFiles',help='The name of the input file(s), including file extension',widget='MultiFileChooser',nargs='+')
    parser.add_argument('--outputFileName', action='store', help="Name of output file. If not provided the input file name will be used with a 'output_' prefix",default='')

# This function should not need to be changed (it is used for adding the tool to another GUI as a subparser)
def initSubparser(gooeyParser, parserKey = '{subparserKey}'):
    myParser = gooeyParser.add_parser(parserKey,help='{subparserHelp}')
    initGooey(myParser)
    return parserKey, runCommand

# For most cases this will not need to be modified. Put your script execution in runCommand
if __name__ == "__main__":
     

    @Gooey(clear_before_run = True, show_success_modal = False, default_size=(596, 650))
    def main():

        parser = GooeyParser(description='{description}')
        
        initGooey(parser)
        
        args = parser.parse_args()
        runCommand(args)
    
    main()