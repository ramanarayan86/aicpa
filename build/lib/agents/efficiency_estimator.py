
# =============================================================================
# File: aicpa/agents/efficiency_estimator.py
# =============================================================================

class EfficiencyEstimator:
    """Estimates efficiency (e.g., FLOPs vs. peak FLOPs) for each operation."""

    def __init__(self, peak_flops: float = 1e12):
        # Suppose we got peak_flops from hardware_info or Deepseek.
        self.peak_flops = peak_flops

    def estimate_efficiency(self, op_name: str, flops: float, time_ms: float):
        """
        Compute efficiency as ratio of ideal time vs. actual time, in percentage.

        ideal_time_ms = (flops / peak_flops) * 1000
        efficiency = (ideal_time_ms / time_ms) * 100
        """
        if time_ms <= 0:
            return 0.0
        ideal_time_ms = (flops / self.peak_flops) * 1e3
        eff = (ideal_time_ms / time_ms) * 100.0
        return eff
