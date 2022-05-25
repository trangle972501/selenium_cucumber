import itertools
import os
import time

from webportal.common.environment import *
from webportal.common.helpers import env

timeout = int(env(WEBPORTAL_TIMEOUT, 5))
poll_during_waits = float(env(WEBPORTAL_POLL_DURING_WAITS, 0.5))
