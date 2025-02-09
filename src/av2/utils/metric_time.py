# <Copyright 2022, Argo AI, LLC. Released under the MIT license.>

"""Time units utilities."""

from enum import Enum
from typing_extensions import Union


class TimeUnit(str, Enum):
    """Metric time units."""

    Second = "SECOND"
    Millisecond = "MILLISECOND"
    Microsecond = "MICROSECOND"
    Nanosecond = "NANOSECOND"


def to_metric_time(ts: Union[int, float], src: TimeUnit, dst: TimeUnit) -> float:
    """Convert a timestamp from src units of metric time, to dst units.

    Args:
        ts: timestamp, expressed either as an integer or float, measured in `src` units of metric time
        src: source unit of metric time
        dst: destination/target unit of metric time

    Returns:
        timestamp expressed now in `dst` units of metric time
    """
    units_per_sec = {
        TimeUnit.Second: 1,
        TimeUnit.Millisecond: 1e3,
        TimeUnit.Microsecond: 1e6,
        TimeUnit.Nanosecond: 1e9,
    }
    # ts is in units of `src`, which will cancel with the denominator
    return ts * (units_per_sec[dst] / units_per_sec[src])
