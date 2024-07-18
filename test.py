import os

def print_directory_tree(root_dir, indent=''):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f'{indent}{item}/')
            print_directory_tree(item_path, indent + '    ')
        else:
            print(f'{indent}{item}')


if __name__ == "__main__":
    root_directory = os.getcwd()  # 替换为你的PyCharm工程路径
    print(f'{root_directory}/')
    print_directory_tree(root_directory)
