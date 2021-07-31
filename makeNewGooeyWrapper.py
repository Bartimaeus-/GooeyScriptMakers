from gooey import Gooey
from gooey import GooeyParser

import os

def getImportLine(scriptName): 
    return '    import {library} as {libAlias}\n'.format(library=scriptName, libAlias = scriptName+'Alias')
    
def getSubparserInit(Alias):
    return '        {AliasStr}Key,{AliasStr}Run = {AliasStr}.initSubparser(subs)\n'.format(AliasStr = Alias)
    
def getToolDictEntry(Alias):
    return '{AliasStr}Key: {AliasStr}Run'.format(AliasStr = Alias)
    

# Script execution goes here
def runCommand(args):
    outputFileName = args.OutputFileName + '.py'
    outputFileName = args.FolderLocation + '\\' + outputFileName
    
    deSCRIPTion = args.ScriptDescription
    parserKey = args.OutputFileName
    parserKey = parserKey.join(parserKey.split()) #remove whitespace from script name
    
    templateFileName = args.Template
    scriptsToAdd = args.ScriptsToAdd
    
    importLines = ""
    subparserInitLines = ""
    dictEntries = "{"

    with open(outputFileName, "x") as newScript:
    
        newScriptTemplate = open(templateFileName,'r').read()
        for scriptFile in scriptsToAdd:
            scriptName = os.path.splitext(os.path.basename(scriptFile))[0]
            scriptAlias = scriptName + 'Alias'
            importLines = importLines + getImportLine(scriptName)
            subparserInitLines = subparserInitLines + getSubparserInit(scriptAlias)
            dictEntries = dictEntries + getToolDictEntry(scriptAlias) + ','
            
        
        dictEntries += '}'    
            
    
        newScript.write(newScriptTemplate.format(imports = importLines,description = deSCRIPTion, subparserInits = subparserInitLines, toolDictionary = dictEntries))
        newScript.close()
        print('New Script Created: ', outputFileName)
        exit()

# Put initialization for the 
def initGooey(parser):
    
    parser.add_argument('FolderLocation',help='Folder location of the new script',widget='DirChooser')
    parser.add_argument('OutputFileName', action='store', help="Name of the new script (no extension)",default='')
    
    parser.add_argument('ScriptsToAdd',help='The name of the scripts to bundle into the new Gooey tool',widget='MultiFileChooser',nargs='+')
    
    parser.add_argument('--ScriptDescription',action='store', help='Description of the new script',default='')
    parser.add_argument('--ScriptHelp',action='store', help='The help text for the new script',default='')
    
    parser.add_argument('--Template',help='The template script file to use',widget='FileChooser', default = 'newWrapperTemplate.py')

# This function should not need to be changed (it is used for adding the tool to another GUI as a subparser)
def initSubparser(gooeyParser, parserKey = 'makeNewGooeyWrapper'):
    myParser = gooeyParser.add_parser(parserKey,help='Generate a Gooey wrapper GUI tool for multiple scripts')
    initGooey(myParser)
    return parserKey, runCommand

# For most cases this will not need to be modified. Put your script execution in runCommand
if __name__ == "__main__":
     

    @Gooey(clear_before_run = True, show_success_modal = False, default_size=(596, 650))
    def main():

        parser = GooeyParser(description='Generate a Gooey wrapper GUI tool for multiple scripts\nScripts must be compliant with the makeNewScriptTemplate format')
        
        initGooey(parser)
        
        args = parser.parse_args()
        runCommand(args)
    
    main()