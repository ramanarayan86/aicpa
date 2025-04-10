################################################################################
# File: aicpa/core/runner.py
################################################################################

import torch
from agents.language_detector import LanguageDetector
from agents.static_graph_parser import StaticGraphParser
from agents.profiler_agent import ProfilerAgent
from agents.efficiency_estimator import EfficiencyEstimator
from agents.bottleneck_detector import BottleneckDetector
from agents.optimization_agent import OptimizationAgent
from agents.explain_agent import ExplainAgent

from core.hardware_info import HardwareInfo

class Runner:
    """Coordinates the overall process from ingestion, profiling, and analysis."""

    def __init__(self, config, deepseek_client=None):
        self.config = config
        self.language_detector = LanguageDetector()
        self.parser = StaticGraphParser()
        self.profiler = ProfilerAgent(record_shapes=True, profile_memory=False)
        self.hwinfo = HardwareInfo()
        self.bottleneck_detector = BottleneckDetector()
        self.optimization_agent = OptimizationAgent()
        self.explain_agent = ExplainAgent(deepseek_client=deepseek_client)

    def run(self, model, inputs):
        # 1) Parse static graph
        gmodule = self.parser.parse(model)
        if gmodule:
            print("\n[Static Graph]")
            gmodule.graph.print_tabular()
        # 2) Profile
        table_str = self.profiler.profile_model(model, inputs)
        print("\n[Profiler Results]")
        print(table_str)

        # 3) Bottleneck detection
        bottlenecks = self.bottleneck_detector.detect_bottlenecks(table_str)
        print("\n[Bottlenecks Detected]")
        for b in bottlenecks:
            print(" -", b)

        # 4) Optimization suggestions
        suggestions = self.optimization_agent.suggest(bottlenecks)
        print("\n[Optimization Suggestions]")
        for s in suggestions:
            print(" -", s)

        # 5) Explanation
        explanation = self.explain_agent.explain_bottlenecks(bottlenecks)
        print(explanation)










# # core/runner.py

# from aicpa.models.test_model import get_model
# from aicpa.core.hardware_info import get_gpu_peak_flops
# from aicpa.agents.profiler_agent import profile_model
# from aicpa.agents.efficiency_estimator import compute_efficiency
# import torch
# import json


# def run_pipeline(model_name='mlp', batch_size=64, input_dim=128):
#     model = get_model(model_name).cuda()
#     input_tensor = torch.randn(batch_size, input_dim).cuda()

#     print("\n[STEP 1] GPU Info")
#     hardware_info = get_gpu_peak_flops()
#     print(json.dumps(hardware_info, indent=2))

#     print("\n[STEP 2] Running Profiler")
#     table, summary = profile_model(model, input_tensor)
#     print(table)

#     print("\n[STEP 3] Efficiency Report")
#     results = compute_efficiency(summary, hardware_info['peak_flops'])
#     for r in results:
#         print(json.dumps(r, indent=2))
