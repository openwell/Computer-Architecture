#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
# cpu.load()
cpu.load('./ls8/examples/mult.ls8')
print(cpu.ram)
cpu.run()