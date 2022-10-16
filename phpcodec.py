import codecs,sys, subprocess
from importlib import machinery

def phpdecode(input):
    return (
        'import helper;helper.run(b"""{}""")\n'
            .format("\n".join(str(input.tobytes(),'utf-8')
            .split("\n")[1:]).replace('"','\\"')),
        len(input)
    )

def search_function (s):
    if (s != "php"):
        return None

    return codecs.CodecInfo(None, phpdecode, name='php')

codecs.register(search_function)

if (__name__ == '__main__'):
    loader = machinery.SourceFileLoader('php',sys.argv[1])
    loader.load_module()
