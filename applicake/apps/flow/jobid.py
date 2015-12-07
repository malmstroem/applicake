#!/usr/bin/env python

from applicake.base import BasicApp
from applicake.base.coreutils import Argument
from applicake.base.coreutils import Keys, KeyHelp


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