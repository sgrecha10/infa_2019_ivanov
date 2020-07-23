"""
Модуль для рекурсивной (транзитивной?) перезагрузки всех модулей

"""

from importlib import reload
import types


def status(module):
    print('reloading:', module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED:', module.__name__)

def rekreload(module, visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited.add(module)
        for _attr in module.__dict__.values():
            if type(_attr) == types.ModuleType:
                rekreload(_attr, visited)

def rekreload_all(arg):
    visited = set()
    if type(arg) == types.ModuleType:
        rekreload(arg, visited)

def tester(reloader, modname):
    import importlib, sys
    if len(sys.argv) > 1:
        modname = sys.argv[1]

    module = importlib.import_module(modname)
    reloader(module)

if __name__ == '__main__':
    tester(rekreload_all, 'reloadall')