# utils.py

import os
import time
import logging
from typing import Union

logger = logging.getLogger(__name__)

def get_current_timestamp() -> float:
    return time.time()

def get_file_size_in_bytes(file_path: str) -> int:
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return 0

    return os.path.getsize(file_path)

def is_valid_email(email: str) -> bool:
    try:
        from email.utils import parseaddr
        return parseaddr(email)[1].count('@') == 1
    except Exception:
        return False

def is_valid_phone_number(phone_number: str) -> bool:
    return phone_number.replace('-', '').replace('(', '').replace(')', '').isnumeric()

def get_duration_in_seconds(start_time: Union[float, int], end_time: Union[float, int]) -> float:
    return max(end_time - start_time, 0)