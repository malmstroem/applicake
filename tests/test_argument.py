"""Argument tests."""
import os
import unittest
import sys
import logging

from applicake.base.apputils import dicts
from applicake.base.coreutils.arguments import Argument, parse_sysargs
from applicake.base.coreutils.log import Logger
from applicake.base.coreutils.keys import Keys, KeyHelp
from applicake.base.coreutils.info import get_handler


MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MY_PATH + '/../')

class Test(unittest.TestCase):
    """Argument tests."""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def test_parse_args(cls):
        """Test to parse arguments."""
        sys.argv = ['--INPUT', 'fcuk.ini', '--OUTPUT', 'kufc.ini']
        defaults, cliargs = parse_sysargs([])
        print(defaults)
        print(cliargs)

    def test1_arg_priority(self):
        """Test the argument priorities. Disabled."""
        sys.argv = ['--INPUT', 'fcuk.ini', '--OUTPUT', 'kufc.ini']
        # basic arguments for every node

        basic_args = [Argument(Keys.INPUT, KeyHelp.INPUT, default=''),
                      Argument(Keys.OUTPUT, KeyHelp.OUTPUT, default=''),
                      Argument(Keys.MODULE, KeyHelp.MODULE, default=''),
                      Argument(Keys.LOG_LEVEL, KeyHelp.LOG_LEVEL, default="DEBUG")]


        # Fixme: Prettify WORKDIR creation system
        # WORKDIR: if WORKDIR is defined add related args
        app_args = []

        for i, arg in enumerate(app_args):
            if arg.name == Keys.WORKDIR:
                app_args.insert(i + 1,
                                Argument(Keys.BASEDIR, KeyHelp.BASEDIR, default='.'))
                app_args.insert(i + 2,
                                Argument(Keys.JOB_ID, KeyHelp.JOB_ID, default=''))
                app_args.insert(i + 3,
                                Argument(Keys.SUBJOBLIST, KeyHelp.SUBJOBLIST, default=''))
                app_args.insert(i + 4,
                                Argument(Keys.NAME, KeyHelp.NAME, default=self.__class__.__name__))
                break

        blub = basic_args + app_args
        defaults, cliargs = parse_sysargs(blub)

        # construct info from defaults < info < commandlineargs
        inifile = cliargs.get(Keys.INPUT, None)
        info_fh = get_handler(inifile)
        fileinfo = info_fh.read(inifile)
        info = dicts.merge(cliargs, dicts.merge(fileinfo, defaults))

        # setup logging
        log = Logger.create(info[Keys.LOG_LEVEL])

        # request by malars: show dataset prominent in logger
        if Keys.DATASET_CODE in info:
            if not isinstance(info[Keys.DATASET_CODE], list):
                if Keys.MZXML in info and not isinstance(info[Keys.MZXML], list):
                    logging.info("Dataset is %s (%s)",
                             info[Keys.DATASET_CODE], os.path.basename(info[Keys.MZXML]))
                else:
                    logging.info("Dataset is %s", info[Keys.DATASET_CODE])
            else:
                logging.debug("Datasets are %s", info[Keys.DATASET_CODE])
        #argObj = Argument( "BLUMMER", "DUMMER BLUMMER HELP", default=1)
        #parse_sysargs(argObj)

    @classmethod
    def tearDownClass(cls):
        pass
