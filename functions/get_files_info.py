import os
def get_files_info(working_directory, directory="."):
    
    wd_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, directory)
    full_path_abs = os.path.abspath(full_path)
    
    if full_path_abs.startswith(wd_abs) is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(full_path) is False:
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_content = os.listdir(full_path)
    except Exception as e:
        return f"Error: {str(e)}"    
    
    content = ""
    for item in dir_content:
        item_path = os.path.join(full_path, item)
        try:
            is_directory = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
        except Exception as e:
            return f"Error: {str(e)}"
        content += (f'- {item}: file_size={size}, is_dir={is_directory}\n')
    return content