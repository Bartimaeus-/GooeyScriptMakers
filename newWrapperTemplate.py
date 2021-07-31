if __name__ == "__main__":
    from gooey import Gooey
    from gooey import GooeyParser
    import os
    
{imports}
    import convertTextEncoding as utfEncoding
    import trimLines as lineSlicer
    
    import deleteCSVcolumnByNumber as delCSVcolNum
    
    @Gooey(clear_before_run = True, show_success_modal = False, default_size=(596, 650),  header_show_title = True, header_show_subtitle = True)
    def main():
        
        
        parser = GooeyParser(description='{description}')
        
        # create the subparsers
        subs = parser.add_subparsers(help='commands', dest='command')
        
        # First, add the tool subparser. hold on to the results (This is how the tool is added to our GUI)
{subparserInits}
        utfEncodeKey,utfRun = utfEncoding.initSubparser(subs)
        lineSliceKey,lineSliceRun = lineSlicer.initSubparser(subs)
        delCSVcolNumKey, delCSVcolNumRun = delCSVcolNum.initSubparser(subs)
        
        # Next, add the suboarser keys and run funcitons to a dictionary
        # https://stackoverflow.com/a/9168387/3158933
        
        toolDict = {toolDictionary}
        
        
        args = parser.parse_args()
        
        toolDict[args.command](args)      

        exit()
    
    
    main()