def get_string(file_path):
    the_file=open(file_path,"r")

    content=the_file.read()

    result=""

    for ch in content:

        if ch in [" ", "\n", "\t"]:
            pass
        else:
            result+=ch