#!/usr/bin/env python3

import re
import os
import sys

InpProgram = sys.argv[1]
program = os.path.abspath(os.path.join("programs", f"{InpProgram}.psep"))
lines = []
variables = {}

# new code to be added
