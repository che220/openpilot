#!/usr/bin/env python3
# simple boardd wrapper that updates the panda first
import os

from panda import Panda
from common.basedir import BASEDIR

PANDA_FW_FN = os.path.join(BASEDIR, "silence_dos", "silent_dos_panda.bin.signed")


def main() -> None:
  panda_list = Panda.list()
  if len(panda_list) > 0:
    for tmp_panda in panda_list:
      panda = Panda(tmp_panda)
      if tmp_panda.is_dos():
        tmp_panda.flash(fn=PANDA_FW_FN)


if __name__ == "__main__":
  main()
