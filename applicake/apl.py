#!/usr/bin/env python3
"""
Executes main() function of class defined in argv[0]
Potentially unsafe but convenient.

Example usage:
alp.py examples.echobasic --COMMENT hello
"""
import importlib
import inspect
import sys


def main():
    """main, find applicake app and execute main."""
    appliapp = None
    cls = None
    try:
        appliapp = sys.argv[1]
        module = importlib.import_module(appliapp)
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and appliapp in obj.__module__:
                cls = obj
    except ModuleNotFoundError as error:
        raise ModuleNotFoundError('Could not find/load app [%s]: %s' % (appliapp, str(error)))
    try:
        cls.main()
    except KeyError as error:
        raise KeyError('Missing key [%s]: %s' % (appliapp, str(error)))
    except Exception as error:
        raise Exception('General exception, could not run app [%s]: %s' % (appliapp, str(error)))


if __name__ == "__main__":
    main()
