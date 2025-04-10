################################################################################
# File: aicpa/scripts/benchmark_cli.py
################################################################################

import argparse
from scripts.run_pipeline import run_pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AICPA Benchmark CLI")
    parser.add_argument("--model", type=str, default="bert-base-uncased", help="Hugging Face model name")
    parser.add_argument("--batch-size", type=int, default=1, help="Batch size")
    parser.add_argument("--seq-len", type=int, default=16, help="Sequence length")

    args = parser.parse_args()

    run_pipeline(
        model_name=args.model,
        batch_size=args.batch_size,
        seq_len=args.seq_len
    )















# # scripts/benchmark_cli.py

# import argparse
# from aicpa.core.runner import run_pipeline


# def main():
#     parser = argparse.ArgumentParser(description="Run AICPA benchmarking pipeline.")
#     parser.add_argument('--model', type=str, default='mlp', help='Model name: mlp')
#     parser.add_argument('--batch-size', type=int, default=64, help='Batch size for input')
#     parser.add_argument('--input-dim', type=int, default=128, help='Input dimension for model')
#     args = parser.parse_args()

#     run_pipeline(model_name=args.model, batch_size=args.batch_size, input_dim=args.input_dim)


# if __name__ == '__main__':
#     main()

