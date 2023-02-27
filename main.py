import os
def comparefilesagainststandards(directory_path):
    standard_files=('Readme.md','.env','.env.ncms','.env.common','main.py')
    compared_files=[]
    additional_files=[]
    for root,dirnames,filenames in os.walk(directory_path):
        for filename in filenames:
            if filename in standard_files:
                compared_files.append(filename)
            else:
                additional_files.append(filename)

    missing_files=[]
    [missing_files.append(file) for file in standard_files if file not in compared_files ]
    
    # print("Given files compared against standards are:\n "," , ".join(compared_files))
    print("Missing file types are:\n"," , ".join(missing_files))
    print("Additional files are:\n"," , ".join(additional_files))
    
# path=r"Desktop\helpage"
comparefilesagainststandards(".")

#Another method
# import glob
# standard_files=('Readme.md','.env','.env.ncms','.env.common','main.py')
# missing_files=[]
# compared_files=[]
# additional_files=[]
# path=r".*"
# fileslist=glob.glob(path)
# # print(fileslist)
# for file in fileslist:
#     if file in standard_files:
#         compared_files.append(file)
#     else:
#         additional_files.append(file)

# for file in standard_files:
#     if file not in compared_files:
#         missing_files.append(file)
# print("Given files compared against standards are:\n "," , ".join(compared_files))
# print("Missing file types are:\n"," , ".join(missing_files))
# print("Additional files are:\n"," , ".join(additional_files))
