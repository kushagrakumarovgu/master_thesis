[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab.svg)](#getting-started)
[![Status](https://img.shields.io/badge/state-active-4caf50.svg)](#project-overview)
[![Tests](https://img.shields.io/badge/tests-manual-orange.svg)](#usage)
[![Docs](https://img.shields.io/badge/docs-up%20to%20date-6c63ff.svg)](#getting-started)
[![License](https://img.shields.io/badge/license-private-lightgrey.svg)](#contributing)
[![Support](https://img.shields.io/badge/support-contact%20maintainer-0d47a1.svg)](#faq)

# Bias Detection Tool

`Bias Detection Tool` evaluates sentiment, politeness, and reasoning signals across multiple large language models (LLMs). It is ideal for comparing provider behavior on the same dataset and assembling unified reports for downstream analysis.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
   - [Requirements](#requirements)
   - [Environment Setup](#environment-setup)
   - [Configuration](#configuration)
3. [Usage](#usage)
   - [OpenAI GPT](#openai-gpt)
   - [Google Gemini](#google-gemini)
   - [Anthropic Claude](#anthropic-claude)
4. [Aggregating Intermediate Outputs](#aggregating-intermediate-outputs)
5. [Producing the Final Report](#producing-the-final-report)
6. [FAQ](#faq)
7. [Citation](#citation)
8. [Contributing](#contributing)

## Project Overview

The tool accepts a CSV file containing conversation snippets or prompts, calls out to several LLM providers, and calculates comparative metrics. All intermediate and final artifacts are written to `src/new_results/`, keeping experimentation data organized.

## Getting Started

### Requirements

- Python 3.10.12 (or compatible 3.10 release)
- `pip` for dependency management
- Unix-like shell (macOS, Linux, or WSL)

Verify your interpreter version:

```console
python --version
Python 3.10.12
```

### Environment Setup

Create and activate a virtual environment:

```console
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```console
pip3 install -r requirements.txt
```

### Configuration

Create a `.env` file at the repository root and populate it with your own API credentials. Replace the placeholders below with valid keys; the values shown are illustrative only.

```dotenv
OPENAI_API_KEY=OPENAI_REAL_KEY
GPT_MODEL=gpt-4o

GEMINI_API_KEY=GEMINI_REAL_KEY
GROQ_API_KEY=GROQ_REAL_KEY
ANTHROPIC_API_KEY=ANTHROPIC_REAL_KEY
```

> Keep your `.env` file out of version control and rotate keys regularly.

## Usage

Each provider-specific script reads a CSV file and writes a transformed copy to `src/new_results/`. Use absolute or relative paths for the `--csv-file` argument.

### OpenAI GPT

```console
python src/openai_inference.py --csv-file <path_to_input_csv>
```

Outputs: `src/new_results/<input_file_name>_openai_gpt4o_output.csv`

### Google Gemini

```console
python src/gemini_inference.py --csv-file <path_to_input_csv>
```

Outputs: `src/new_results/<input_file_name>_geminipro_output.csv`

### Anthropic Claude

```console
python src/anthropic_claude.py --csv-file <path_to_input_csv>
```

Outputs: `src/new_results/<input_file_name>__anthropic_claude_sonnet_output.csv`

## Aggregating Intermediate Outputs

When input data is processed in multiple chunks, consolidate the partial results before producing the final report. Update the input/output filenames inside `src/combine.py`, then run:

```console
python src/combine.py
```

## Producing the Final Report

Merge the selected model outputs back into the source dataset to obtain a single CSV containing the original columns plus `sentiment_score`, `politeness_score`, and `reasoning`.

```console
python src/merge_new_results.py --data-file <path_to_original_csv> --result-file <path_to_model_output_csv>
```

The merged file is written to `src/new_results/final_result/`.

## FAQ

1. **"Too many requests" errors** – Your provider is rate-limiting the job. Split the master CSV into smaller batches, run the scripts separately, and combine outputs with `src/combine.py`.
2. **"Number of requests exceeded" or quota exhaustion** – Similar to the above; reduce batch size or wait for quota reset. Consolidate the individual outputs once processing completes.


## Contributing

Contributions, bug reports, and feature suggestions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (for example, `feature/new-idea`).
3. Submit a pull request describing your updates.

© 2025 Kushagra Kumar. Licensed under the MIT License.
