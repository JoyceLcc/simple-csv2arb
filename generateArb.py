import csv
import json
import re
import sys
import codecs

filepath = sys.argv[1]


def get_csv_lines(filename):
    lines:list[list[str]] = []
    with codecs.open(filename, encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            temp_line = []
            for cell in line:
                temp_line.append(cell)
            lines.append(temp_line)
    return lines

csvlines = get_csv_lines(filepath)

line_count = 0
col_count = 0
lang_list : list[str]= []

col_count = len(csvlines[0])
if line_count == 0:
    for index in range(3, len(csvlines[0])):
        lang_list.append(csvlines[0][index])
    
for lang in lang_list:
    line_count = 0
    lang_index = lang_list.index(lang) + 3
    dict = {}
    for line in csvlines:
        line_count = line_count + 1
        # Skip first line
        if line_count >= 2:
            dict[line[0] + line[1]] = line[lang_index]

            # Check any placeholders
            placeholder_key_list = re.findall(r'{\w+}', line[lang_index])
            if len(placeholder_key_list) > 0:
                placeholder_list = {}
                for key in placeholder_key_list:
                    key_name = re.sub('[^A-Za-z0-9]+', '', key)
                    type_name = "String"
                    if "int_" in key:
                        type_name = "int"
                    elif "double_" in key:
                        type_name = "double"
                    elif "number_" in key:
                        type_name = "number"

                    placeholder_list[key_name] = {"type": type_name}
                
                # Add description if desc column is not null
                if len(line[2]) > 0:
                    dict["@"+line[0] + line[1]] = { "placeholders": placeholder_list, "description": line[2] }
                else:
                    dict["@"+line[0] + line[1]] = { "placeholders": placeholder_list }

    # print(json.dumps(dict, indent=4))
    with codecs.open("app_"+lang+".arb", "w", encoding='utf-8') as outfile:
        json.dump(dict, outfile, indent=4, ensure_ascii=False)
print("------------------- Done ------------------")
print("Number of row: " + str(line_count))
print("Languages: " + str(lang_list))
print("------------------ Finish -----------------")

