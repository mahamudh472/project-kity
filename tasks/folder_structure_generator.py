import os

def list_files(startpath, exclude_folders=None):
    if exclude_folders is None:
        exclude_folders = []

    for root, dirs, files in os.walk(startpath):
        # Exclude specified folders
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        level = root.replace(startpath, '').count(os.sep)
        indent = '' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = '  |'+'-' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

list_files('d:/myscreen/', exclude_folders=['env', '.git', '__pycache__'])
