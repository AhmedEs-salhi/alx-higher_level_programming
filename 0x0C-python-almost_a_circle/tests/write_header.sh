#!/usr/bin/env bash

echo "#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
$3 = __import__('models.$2', fromlist=['$3']).$3" > $1