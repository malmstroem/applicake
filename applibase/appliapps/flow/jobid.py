#!/usr/bin/env python

from applibase.applicake import BasicApp
from applibase.applicake.coreutils import Argument
from applibase.applicake.coreutils import Keys, KeyHelp


class Jobid(BasicApp):
    """
    creates empty workdir, sometimes needed as init node for setting JOB_ID
    """

    def add_args(self):
        return [
            Argument(Keys.WORKDIR, KeyHelp.WORKDIR)
        ]

    def run(self, log, info):
        return info


if __name__ == "__main__":
    Jobid.main()