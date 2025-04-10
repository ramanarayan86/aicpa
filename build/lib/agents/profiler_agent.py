# =============================================================================
# File: aicpa/agents/profiler_agent.py
# =============================================================================

import torch
from torch.profiler import profile, ProfilerActivity

class ProfilerAgent:
    """Profiles the runtime performance of a model using PyTorch's Profiler."""

    def __init__(self, record_shapes=True, profile_memory=False):
        self.record_shapes = record_shapes
        self.profile_memory = profile_memory

    def profile_model(self, model: torch.nn.Module, inputs: dict):
        """
        Profiles a single forward pass on the given model + inputs.

        Returns:
            A string table from profiler.key_averages().
        """
        model.eval()
        device = next(model.parameters()).device
        sort_by = "cuda_time_total" if device.type == "cuda" else "cpu_time_total"

        with profile(
            activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
            record_shapes=self.record_shapes,
            profile_memory=self.profile_memory
        ) as prof:
            with torch.no_grad():
                model(**inputs)

        # Provide a table sorted by the device type
        return prof.key_averages(group_by_input_shape=True).table(
            sort_by=sort_by, row_limit=30
        )
