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
    assert False


class ParadoxData(object):
    content = u''

    def parse_top_level(self):
        parsed = {}
        linelist = self.content.splitlines()
        x = 0
        while x < len(linelist):
            line = linelist[x]
            lastchar = len(line)-1
            if line[lastchar] == '=':
                y = parse_section(linelist[x+1:])
                subdata = ParadoxData()
                subdata.content = str('\r\n').join(linelist[x+2:x+1+y])
                parsed[line[:lastchar].strip()] = subdata
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


def setup_data():
    filedata = ParadoxData()
    #print("opening reader")
    filedata.content = read_existing_file()
    parsed_data = filedata.parse_top_level()
    for specie in list(parsed_data.keys()):
            parsed_data[specie] = parsed_data[specie].parse_top_level()
            parsed_data[specie]["species"] = parsed_data[specie]["species"].parse_top_level()
    print(parsed_data)
    print(parsed_data.keys())
    print(parsed_data[list(parsed_data.keys())[0]])
    print(len(parsed_data))


setup_data()
