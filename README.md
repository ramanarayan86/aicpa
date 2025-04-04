AICPA: AI Code Performance Analyzer

A modular, AI-agent-powered system to analyze, benchmark, and optimize PyTorch/C++ ML code across NVIDIA GPUs using Torch Profiler, TorchInductor, and CUDA tools.

## 🧱 Directory Structure

```
aicpa/
├── agents/
│   ├── language_detector.py
│   ├── static_graph_parser.py
│   ├── profiler_agent.py
│   ├── efficiency_estimator.py
│   ├── bottleneck_detector.py
│   ├── optimization_agent.py
│   └── explain_agent.py
├── core/
│   ├── config.py
│   ├── hardware_info.py
│   ├── runner.py
│   └── utils.py
├── models/
│   ├── test_model.py
│   └── custom_loader.py
├── ui/
│   ├── app.py  # Streamlit or Gradio
│   └── dashboard.py
├── data/
│   ├── logs/
│   └── reports/
├── scripts/
│   ├── run_pipeline.py
│   └── benchmark_cli.py
├── requirements.txt
└── README.md
```
---

## 🚀 Key Features

-  Deep runtime and static profiling
-  Hardware-aware FLOPs and memory analysis
-  Op-by-op efficiency vs peak comparison
-  AI Agents for optimization recommendations
-  Support for PyTorch, TorchInductor, TorchScript, and C++

## 📦 To-Do

- [ ] Implement full pipeline
- [ ] Add Triton optimization support
- [ ] Deploy Streamlit frontend
- [ ] Add real ML model benchmarking

---


