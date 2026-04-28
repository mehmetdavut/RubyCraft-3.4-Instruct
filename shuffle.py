from datasets import load_dataset

# Fixed seed for absolute reproducibility
SEED_VALUE = 42
# Target count strictly matching our HQ subset size
TARGET_COUNT = 1845
# The output file name
output_filename = "gemini_5k_ctrl.jsonl"

# 1. Load the raw, uncurated 5K dataset (ALL) from the Hugging Face Hub
dataset = load_dataset(
    "mehmetdavut/RubyCraft-3.4-Instruct",
    data_files="gemini_5k_all.jsonl",
    split="train",
)

# 2. Shuffle the dataset deterministically using the fixed seed
shuffled_dataset = dataset.shuffle(seed=SEED_VALUE)

# 3. Select the first 1845 samples to construct the CTRL group
random_dataset = shuffled_dataset.select(range(TARGET_COUNT))

# 4. Save to disk as JSONL, preserving UTF-8 formatting
random_dataset.to_json(output_filename, force_ascii=False)

print(f"✅ Process complete! {TARGET_COUNT} random samples have been saved to {output_filename}.")
