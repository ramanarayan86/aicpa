################################################################################
# File: aicpa/core/utils.py
################################################################################

import torch

def create_dummy_input(model, batch_size=1, seq_len=16, vocab_size=30522, device="cuda"):
    """Example: for a text-based model, create random input_ids and attention_mask."""
    input_ids = torch.randint(0, vocab_size, (batch_size, seq_len), device=device)
    attention_mask = torch.ones((batch_size, seq_len), device=device)
    return {"input_ids": input_ids, "attention_mask": attention_mask}