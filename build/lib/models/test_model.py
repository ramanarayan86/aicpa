################################################################################
# File: aicpa/models/test_model.py
################################################################################

from transformers import AutoModel
import torch

class TestModel:
    @staticmethod
    def load_model(model_name="bert-base-uncased", device="cuda"):
        print(f"[TestModel] Loading model: {model_name}")
        m = AutoModel.from_pretrained(model_name)
        m.to(device)
        m.eval()
        return m














# models/test_model.py

# import torch.nn as nn


# class SimpleMLP(nn.Module):
#     def __init__(self, input_dim=128):
#         super(SimpleMLP, self).__init__()
#         self.fc1 = nn.Linear(input_dim, 64)
#         self.relu1 = nn.ReLU()
#         self.fc2 = nn.Linear(64, 32)
#         self.relu2 = nn.ReLU()
#         self.fc3 = nn.Linear(32, 10)

#     def forward(self, x):
#         x = self.relu1(self.fc1(x))
#         x = self.relu2(self.fc2(x))
#         return self.fc3(x)


# def get_model(name):
#     if name == 'mlp':
#         return SimpleMLP()
#     else:
#         raise ValueError(f"Unknown model name: {name}")

