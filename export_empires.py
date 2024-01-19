from split_empires import setup_data


def write_files(formatted_data, user_data_only=False):
    user_empires = ""
    for empire_name in list(formatted_data.keys()):
        empire = formatted_data[empire_name]
        bio = empire.bio
        if bio:
            bio = bio.splitlines()[0]
            bio = bio.replace('"', '', 2)
        if '-' in bio and len(bio) < 32:
            # print(bio)
            # print(empire.unaltered_text)
            if user_data_only:
                continue
            with open('single_empires/%s.txt' % (bio), 'w', newline='') as open_file:
                open_file.write(empire.unaltered_text + "\r\n")
        else:
            user_empires += empire.unaltered_text + "\r\n"
    with open('single_empires/user_empires.txt', 'w', newline='') as open_file:
        # print(user_empires)
        open_file.write(user_empires)


def export_empires(user_data_only=False):
    formatted_data = setup_data()
    write_files(formatted_data, user_data_only=user_data_only)


export_empires()
