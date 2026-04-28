# utils.py


def get_architecture(model_name):
    name = str(model_name).lower()
    if "qwen" in name and "coder" in name:
        return "Qwen-Coder"
    elif "qwen" in name:
        return "Qwen"
    elif "llama" in name:
        return "Llama"
    elif "gemma" in name:
        return "Gemma"
    elif "phi" in name:
        return "Phi"
    else:
        return "Other"

def get_tier(model_name):
    name = str(model_name).lower()
    if any(size in name for size in ["7b", "8b", "9b", "big"]):
        return "Big (≥ 7B)"
    elif "qwen" in name and "coder" in name and "7b" not in name:
        return "Small (< 4B)"
    elif any(size in name for size in ["1.5b", "2b", "3b", "mini", "small", "3.2"]):
        return "Small (< 4B)"
    else:
        return "Unknown"

def standardize_model_names(df, model_column="model_architecture"):
    df_clean = df.copy()
    
    df_clean["Architecture"] = df_clean[model_column].apply(get_architecture)
    df_clean["Tier"] = df_clean[model_column].apply(get_tier)
    df_clean = df_clean[
        (df_clean["Architecture"] != "Other") & 
        (df_clean["Tier"] != "Unknown")
    ]
    
    return df_clean

ARCH_ORDER = ["Gemma", "Llama", "Phi", "Qwen", "Qwen-Coder"]