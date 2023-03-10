import os
import json

def compare_folder_contents(directory_path,standard_file):
    fileObject=open(standard_file,"r")
    jsoncontent=fileObject.read()
    standardfilelist=json.loads(jsoncontent)
    fileObject.close()
    compared_files=[]
    additional_files=[]
    for root,dirnames,filenames in os.walk(directory_path):
        for filename in filenames:
            if filename in standardfilelist:
                compared_files.append(filename)
            else:
                additional_files.append(filename)

    missing_files=[]
    [missing_files.append(file) for file in standardfilelist if file not in compared_files ]
    
    return missing_files,additional_files
if __name__=="__main__":
#     if len(sys.argv)!=3:
#         sys.exit("Require 3 command line arguments")
#     cmdline_param1,cmdline_param2=sys.argv[1],sys.argv[2]
#     del sys.argv[1:]
    compare_folder_contents(sys.argv[1],sys.argv[2])
