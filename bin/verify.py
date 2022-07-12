#! /usr/bin/env python
"""Verify validity of name as git ref."""
import re
import sys

name = sys.argv[1]
acceptable = re.compile(r'^(?!/|.*([/.]\.|//|@\{|\\\\))[^\040\177 ~^:?*\[]+(?<!\.lock)(?<!/)(?<!\.)$')
print(name, '->', 'ACCEPT' if re.match(acceptable, name) else 'REJECT')
