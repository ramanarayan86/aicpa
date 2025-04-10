################################################################################
# File: aicpa/scripts/run_pipeline.py
################################################################################

import torch

from core.config import Config
from core.runner import Runner
from models.test_model import TestModel
from core.utils import create_dummy_input


def run_pipeline(model_name="bert-base-uncased", batch_size=1, seq_len=16):
    config = Config()
    config.device = "cuda" if torch.cuda.is_available() else "cpu"

    # Setup runner
    runner = Runner(config=config)

    # Load model
    model = TestModel.load_model(model_name=model_name, device=config.device)

    # Create dummy inputs
    dummy_inputs = create_dummy_input(model, batch_size=batch_size, seq_len=seq_len, device=config.device)

    # Run the pipeline
    runner.run(model, dummy_inputs)

if __name__ == "__main__":
    run_pipeline()
