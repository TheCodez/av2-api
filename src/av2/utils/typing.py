# <Copyright 2022, Argo AI, LLC. Released under the MIT license.>

"""Types used throughout the package."""

from __future__ import annotations

from pathlib import Path
from typing_extensions import Any, Union  # noqa

import numpy as np
from upath import UPath

NDArrayNumber = np.ndarray
NDArrayBool = np.ndarray
NDArrayFloat = np.ndarray
NDArrayFloat32 = np.ndarray
NDArrayByte = np.ndarray
NDArrayInt = np.ndarray
NDArrayObject = np.ndarray


PathType = Union[Path, UPath]
