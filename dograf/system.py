import psutil
from typing import Dict
from time import sleep
import json

psutil.PROCFS_PATH = "/host"

def get_system_data() -> Dict[str, float]:
    
    data = {
        "ram": psutil.virtual_memory().percent,
        "cpu": psutil.cpu_percent(),
    }
    # collect disk and network data over 0.1 s interval
    # unit is bytes/second
    POLL_INTERVAL = 0.1

    disk_io_init = psutil.disk_io_counters()
    sleep(POLL_INTERVAL)
    disk_io_fin = psutil.disk_io_counters()

    net_io_init = psutil.net_io_counters()
    sleep(POLL_INTERVAL)
    net_io_fin = psutil.net_io_counters()

    data["d_io_r"] = (disk_io_init.read_bytes - disk_io_fin.read_bytes)/POLL_INTERVAL
    data["d_io_w"] = (disk_io_init.write_bytes - disk_io_fin.write_bytes)/POLL_INTERVAL

    data["n_io_r"] = (net_io_init.bytes_recv - net_io_fin.bytes_recv)/POLL_INTERVAL
    data["n_io_s"] = (net_io_init.bytes_sent - net_io_fin.bytes_sent)/POLL_INTERVAL

    return json.dumps(data)