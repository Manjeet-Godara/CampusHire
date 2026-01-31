def get_string(file_path):

    content=file_path.read().decode("utf-8")

    result=""
    type(content)
    for ch in content:

        if ch in [" ", "\n", "\t","\r"]:
            pass
        else:
            result+=str(ch)
    
    return result