import glob
import os

from lib import convert_json_into_csv

input_dir = 'data'


def main():
    json_files = glob.glob(os.path.join(input_dir, "**\*.json"), recursive=True)
    print(json_files)
    [convert_json_into_csv(json_file) for json_file in json_files]
        

if __name__ == "__main__":
    main()
