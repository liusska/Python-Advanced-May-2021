import os


def extract_files(dir):
    return [el for el in dir if os.path.isfile(el)]


def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_files_extensions(files)

for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    with open("report.txt", 'a') as file:
        file.writelines(f"{extension}\n")
        file.writelines(f"- - - {name}\n" for name in file_names)
