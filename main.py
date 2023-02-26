import os
def comparefilesagainststandards(directory_path):
    # file_ext=('.md','.html','.css','.js','.txt','.png','.jpeg')
    standard_file_type=('md','html','css','js','txt','png','jpeg')
    compared_files=[]
    additional_files=[]
    for root,dirnames,filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith(standard_file_type):
                compared_files.append(filename)
            else:
                additional_files.append(filename)

    file_types=[]
    missing_files=[]
    for file in compared_files:
        filename,filetype=file.split(".")
        file_types.append(filetype)
    [missing_files.append(ext) for ext in standard_file_type if ext not in file_types]

    # print("Given files compared against standards are:\n "," , ".join(compared_files))
    print("Missing file types are:\n"," , ".join(missing_files))
    print("Additional files are:\n"," , ".join(additional_files))
    
# path=r"Desktop\helpage"
comparefilesagainststandards(".")
