import datetime, os, shutil
from export_empires import export_empires

FILENAME = 'user_empire_designs_v3.4.txt'


def backup_files():
    shutil.copy("../" + FILENAME, "backups/%s %s%s" %(
        FILENAME[:-4], '{:%Y-%m-%d %H-%M}'.format(datetime.datetime.now()), FILENAME[-4:]))
    # create backups directory if error thrown


def get_pop_empires():
    filecontents = ''
    for file in os.listdir("single_empires"):
        if file.startswith("user"):
            continue
        with open("single_empires/%s" % file, 'r') as open_file:
            filecontents += open_file.read()
    return filecontents


def get_user_empires():
    filecontents = ''
    file_exists = os.path.exists("single_empires/user_empires.txt")
    if not file_exists:
        export_empires(user_data_only=True)
    with open("single_empires/user_empires.txt", 'r') as open_file:
        filecontents += open_file.read()
    return filecontents


def import_empires():
    backup_files()
    pop_empires = get_pop_empires()
    with open(FILENAME, 'w', newline='') as open_file:
        # print(user_empires)
        open_file.write(pop_empires)
    user_empires = get_user_empires()
    with open("../" + FILENAME, 'w', newline='') as open_file:
        # print(user_empires)
        open_file.write(user_empires + pop_empires)

import_empires()
