# =============================================================================
# File: aicpa/core/hardware_info.py
# =============================================================================

import pynvml

class HardwareInfo:
    """
    Queries GPU hardware info. In practice, you could also integrate Deepseek
    here for advanced hardware analysis.
    """

    def __init__(self):
        pynvml.nvmlInit()

    def get_gpu_info(self):
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        name = pynvml.nvmlDeviceGetName(handle)
        sm_count = pynvml.nvmlDeviceGetMultiprocessorCount(handle)
        clock = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM)
        # naive peak flops formula
        # This is a placeholder. Actual formula may differ by GPU architecture.
        flops = 2 * sm_count * clock * 1e6 * 128  # e.g., assume 128 cores per SM
        return {
            'gpu_name': name.decode('utf-8'),
            'sm_count': sm_count,
            'clock_mhz': clock,
            'peak_flops': flops
        }
