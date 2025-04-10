################################################################################
# File: aicpa/agents/optimization_agent.py
################################################################################

class OptimizationAgent:
    """Suggests code-level or compiler-level optimizations."""

    def suggest(self, bottlenecks: list):
        suggestions = []
        for b in bottlenecks:
            # Just naive suggestions.
            suggestions.append(f"For {b}, consider using bigger batch size or enabling TorchInductor.")
        return suggestions