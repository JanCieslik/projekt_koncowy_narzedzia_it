import sys
import os
import json

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


if __name__ == "__main__":
    input_file, output_file, input_ext, output_ext = parsowanie()
    print(f"Plik wejsciowy: {input_file}, Plik wyjsciowy: {output_file}")
