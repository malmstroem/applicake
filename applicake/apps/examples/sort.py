#!/usr/bin/env python
import os

from applicake.base.app import WrappedApp
from applicake.base.apputils.dirs import create_workdir
from applicake.base.apputils import validation
from applicake.base.coreutils import Argument
from applicake.base.coreutils import KeyHelp, Keys


class SortApp(WrappedApp):
    """
    A more advanced example for a WrappedApp
    copies FILE to COPY using 'cp', and implements own validation routine
    """

    def add_args(self):
        return [
            Argument(Keys.EXECUTABLE, KeyHelp.EXECUTABLE, default='sort'),
            Argument("FILE", "File to be copied"),
            Argument("NUMERIC", "nuemric sort if true"),

            Argument(Keys.WORKDIR, "folder where FILE will go into, created if not specified.")
        ]

    def prepare_run(self, log, info):
        info = create_workdir(log, info)
        numflag=""
        if info['NUMERIC'] == "true":
            numflag="-n "
        outfile = os.path.join(info[Keys.WORKDIR], os.path.basename(info['FILE']))
        command = "%s %s %s" % (info['EXECUTABLE'], info["FILE"], outfile)
        info['FILE'] = outfile
        return info, command

    def validate_run(self, log, info, exit_code, stdout):
        validation.check_file(log, info['FILE'])
        validation.check_exitcode(log, exit_code)
        return info

#use this class as executable
if __name__ == "__main__":
    SortApp.main()
