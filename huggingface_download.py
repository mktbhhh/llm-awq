import os

# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import hf_hub_download, snapshot_download

# snapshot_download(repo_id="facebook/opt-125m", local_dir="opt-125m")
# snapshot_download(repo_id="wikitext", repo_type="dataset", local_dir="wikitext")
snapshot_download(repo_id="mit-han-lab/pile-val-backup", repo_type="dataset", local_dir="pile-val-backup", local_dir_use_symlinks=False)

print("done")
