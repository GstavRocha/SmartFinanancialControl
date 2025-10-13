from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from datetime import date
from enum import Enum
from typing import Literal, Optional, Dict

getcontext().prec = 28 # IEEE 754 Decimal128
getcontext().rounding = ROUND_HALF_EVEN