import sys
import os
import json
import yaml
import xml.etree.ElementTree as et
def parsowanie():
    if len(sys.argv) != 3:
        print("program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.orig_argv[1]
    output_file = sys.argv[2]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    return input_file, output_file, input_ext, output_ext
def wczytywanie_json(file_path):
    with open(file_path, 'r') as file:
        wczytane = json.load(file)
    return wczytane
def zapisywanie_json(file_path, wczytane):
    with open(file_path, 'w') as file:
        json.dump(wczytane, file, indent=4)
def wczytywanie_yml(file_path):
    with open(file_path, 'r') as file:
        wczytane = yaml.safe_load(file)
    return wczytane
def zapisywanie_yml(file_path, wczytane):
    with open(file_path, 'w') as file:
        yaml.dump(wczytane, file, default_flow_style=False)
def wczytywanie_xml(file_path):
    tree = et.parse(file_path)
    root = tree.getroot()
    return tree, root
def zapisywanie_xml(file_path, tree):
    tree.write(file_path, encodings='utf-8', xml_declaration=True)


if __name__ == "__main__":
    input_file, output_file, input_ext, output_ext = parsowanie()

    wczytane = None

    if input_ext == '.json':
        wczytane = wczytywanie_json(input_file)
    elif input_ext == '.yml' or input_ext == '.yaml':
        wczytane = wczytywanie_yml(input_file)
    elif input_ext == '.xml':
        tree, root = wczytywanie_yml(input_file)
        wczytane = et.tostring(root, encoding='unicode')


    if output_ext == '.json':
        zapisywanie_json(output_file, wczytane)
    elif output_ext == '.yml' or output_file =='.yaml':
        zapisywanie_yml(output_file, wczytane)
    elif output_ext == '.xml':
        if isinstance(wczytane, str):
            root = et.fromstring(wczytane)
            tree = et.ElementTree(root)
        zapisywanie_xml(output_file, tree)
