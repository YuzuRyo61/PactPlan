#!/usr/bin/env python
import sys
import os
from migrate.versioning.shell import main

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pactplan.config import PP_CONFIG

if __name__ == "__main__":
    main(
        debug="False",
        url=PP_CONFIG["database"]["uri"],
        repository="migrate"
    )
