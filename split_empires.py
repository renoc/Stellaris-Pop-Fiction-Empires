from empire_reader import read_existing_file


def parse_section(linelist):
    assert '{' in linelist[0]
    y = 1
    while y < len(linelist):
        line = linelist[y]
        if '}' in line:
            return y
        elif '{' in line:
            z = parse_section(linelist[y:])
            y = y + z
        y = y + 1
    # data is not properly formatted
    # print(y)
    # print(line)
    assert False


class Empire(object):
    name = u''
    dictdata = {}
    bio = u''
    unaltered_text = u''

    def __init__(self):
        pass

    def __repr__(self):
        return self.unaltered_text


def parse_sub_level(content):
    parsed = {}
    linelist = content.splitlines()
    x = 0
    while x < len(linelist):
        line = linelist[x]
        lastchar = len(line)-1
        if line[lastchar] == '=':
            y = parse_section(linelist[x+1:])
            parsed[line[:lastchar].strip()] = str('\r\n').join(
                linelist[x+2:x+y+1])
            x = x + 1 + y
        elif '=' in line:
            pos = line.index('=')
            multiline = line[pos+1:].strip()
            while multiline[0] == '"' and not multiline[-1] == '"':
                x = x + 1
                multiline = multiline + '\n' + linelist[x].strip()
            parsed[line[:pos].strip()] = multiline
        else:
            # data not properly formatted
            assert not '{' in line
            assert not '}' in line
            assert not '"' in line
        x = x + 1
    return parsed


def parse_top_level(content):
    parsed = {}
    linelist = content.splitlines()
    x = 0
    while x < len(linelist):
        line = linelist[x]
        lastchar = len(line)-1
        if line[lastchar] == '=':
            y = parse_section(linelist[x+1:])
            subdata = Empire()
            subdata.name = line[:lastchar].strip()
            subdata.unaltered_text = str('\r\n').join(linelist[x:x+y+2])
            parsed[subdata.name] = subdata
            x = x + 1 + y
        else:
            # data not properly formatted
            assert not '{' in line
            assert not '}' in line
            assert not '"' in line
            assert not '=' in line
        x = x + 1
    return parsed


def setup_data():
    # print("opening reader")
    parsed_data = parse_top_level(read_existing_file())
    for empire_name in list(parsed_data.keys()):
        empire = parsed_data[empire_name]
        empire.dictdata = parse_sub_level(empire.unaltered_text)
        empire.dictdata = parse_sub_level(empire.dictdata[empire_name])
        # print(empire.dictdata)
        empire.dictdata["species"] = parse_sub_level(empire.dictdata["species"])
        empire.bio = empire.dictdata["species"].get("species_bio", "")
    # print(parsed_data)
    # print(parsed_data.keys())
    # print(parsed_data[list(parsed_data.keys())[0]])
    # print(len(parsed_data))
    return parsed_data


def write_files(formatted_data):
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
            with open('single_empires/%s.txt' % (bio), 'w', newline='') as open_file:
                open_file.write(empire.unaltered_text)
        else:
            user_empires += empire.unaltered_text
    with open('single_empires/user_empires.txt', 'w', newline='') as open_file:
        # print(user_empires)
        open_file.write(user_empires)


def split_empires():
    formatted_data = setup_data()
    write_files(formatted_data)


split_empires()
