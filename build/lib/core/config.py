################################################################################
# File: aicpa/core/config.py
################################################################################

class Config:
    """Global or default config parameters."""

    def __init__(self):
        self.device = "cuda"  # or "cpu"
        self.default_model = "bert-base-uncased"
        self.log_level = "INFO"