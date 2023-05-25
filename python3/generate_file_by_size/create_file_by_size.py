import os
from pathlib import Path
from enum import Enum
from datetime import datetime

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop').replace("\\", "/")
files_path = desktop + "/files"
Path(files_path).mkdir(parents=True, exist_ok=True)


class File(Enum):
    KB = "Kb",
    MB = "Mb",
    GB = "Gb"


FILES_SIZES = {
    File.KB: 2 ** 10,
    File.MB: 2 ** 20,
    File.GB: 2 ** 30
}


def calculate_by_size(prefix: File, size: int):
    return FILES_SIZES[prefix] * size - 1


def create_file(name, size):
    file_full_path = "{0}/{1}".format(files_path, name)
    with open(file_full_path, "wb") as out:
        out.write(bytes("1", 'utf-8'))
        out.seek(size)
        out.write(bytes("1", 'utf-8'))

    print("created file: {}".format(file_full_path))


def generate_files_by_income_size(sizes_GB, sizes_MB=0):
    output_file_dict = dict()

    current_datetime_as_str = datetime.now().strftime('%Y.%m.%d_%H%M%S')
    for file_type, size in {File.GB: sizes_GB, File.MB: sizes_MB}.items():
        if size == 0:
            continue
        count_10 = int(size / 10)
        count_1 = int(size - (count_10 * 10))

        for single_size, count in {1: count_1, 10: count_10}.items():
            for i in range(1, count + 1):
                filename = "{}_{}{}_{:02d}.txt".format(current_datetime_as_str, single_size, file_type.name, i)
                output_file_dict[filename] = calculate_by_size(file_type, single_size)

    for filename, size in output_file_dict.items():
        create_file(filename, size)


SIZE_GB = 1710
SIZE_MB = 500

generate_files_by_income_size(SIZE_GB, SIZE_MB)
