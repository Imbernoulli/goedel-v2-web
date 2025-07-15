import os

files_to_process = [""]
dirs_to_process = ["."]

with open("output.txt", 'w', encoding='utf-8') as f:
    # 处理单个文件
    for file_path in files_to_process:
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as input_f:
                    f.write(f"\n=== File: {file_path} ===\n")
                    content = input_f.read()
                    f.write(content)
                    f.write("\n")
            except Exception as e:
                pass

    # 处理目录
    for d in dirs_to_process:
        for root, dirs, files in os.walk(d):
            for file in files:
                file_path = os.path.join(root, file)
                if any(x in file_path for x in [
                    ".log", ".git", ".sample", ".pyc", ".md",
                    "migration", "__", "moment", "modal"
                ]):
                    continue
                try:
                    with open(file_path, 'r', encoding='utf-8') as input_f:
                        f.write(f"\n=== File: {file_path} ===\n")
                        content = input_f.read()
                        f.write(content)
                        f.write("\n")
                except Exception as e:
                    pass