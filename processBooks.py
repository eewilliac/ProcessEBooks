import os
import configparser

def config_parser_test():
    config = configparser.ConfigParser()
    config.read('app.config')
    source_value = config.get('FileSection', 'source')     
    source_value = "source_value:{}".format(source_value)
    print(source_value)


def is_windows():
    if os.name == 'nt':
        return True
    else:
        return False

def test_os():
    if is_windows():
        return "running windows"
    else:
        return "running linux or macos"

if __name__ == "__main__":
    print(test_os())