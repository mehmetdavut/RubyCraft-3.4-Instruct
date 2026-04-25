# RubyCraft-3.4-Instruct

This repository contains the Exploratory Data Analysis (EDA) notebooks, visualization scripts, and evaluation pipelines used to analyze the impact of our Diagnostic Sanitization Procedure (DSP) on Small Language Models (SLMs) coding in modern Ruby 3.4.

## Links
* **[Dataset & Evaluation Logs]** (https://huggingface.co/datasets/mehmetdavut/RubyCraft-3.4-Eval-Logs)
* **[Training Dataset]** (https://huggingface.co/datasets/mehmetdavut/RubyCraft-3.4-Instruct)
* **[Model Collection (100 LoRA Adapters)]** (https://huggingface.co/mehmetdavut)

## 📊 Exploratory Data Analysis (EDA)
All data analysis and visualizations presented in the paper can be fully reproduced using the Jupyter Notebooks provided in the `eda/` directory. The notebooks automatically fetch the raw evaluation results directly from our Hugging Face dataset.

### Available Notebooks:
1. `01_DSP_Impact_Analysis.ipynb`: Analyzes how the DSP methodology recovers the Intrinsic Capability of SLMs by fixing Formatting Hallucinations.
2. `02_Quantization_and_Scaling.ipynb`: Compares the effects of different quantization levels (4-bit, 8-bit, 16-bit) and dataset sizes (1K vs 5K).
3. `03_Architecture_Comparisons.ipynb`: Benchmarks different base architectures (Qwen, Llama, Gemma, Phi) and teacher models.

## How to Run Locally (Using `uv`)

This project uses [uv](https://docs.astral.sh/uv/), Python package and project manager, to ensure 100% reproducible environments.

**1. Clone the repository:**
```bash
git clone https://github.com/mehmetdavut/RubyCraft-3.4-Instruct.git
cd RubyCraft-3.4-Instruct
```

**2. Sync the exact dependencies from uv.lock:**
```bash
uv sync
```

**3. Launch Jupyter Notebook within the isolated environment:**
```bash
uv run jupyter notebook
```

## License
This project is licensed under the Apache 2.0 License.