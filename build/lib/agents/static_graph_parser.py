################################################################################
# File: aicpa/agents/static_graph_parser.py
################################################################################

import torch.fx

class StaticGraphParser:
    """Uses torch.fx or other methods to parse a model's static graph."""
    def __init__(self):
        pass

    def parse(self, model: torch.nn.Module):
        try:
            graph_module = torch.fx.symbolic_trace(model)
            return graph_module
        except Exception as e:
            print("[StaticGraphParser] Could not parse model:", e)
            return None

