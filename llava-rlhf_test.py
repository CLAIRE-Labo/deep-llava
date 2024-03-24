import torch
from peft import PeftModel

from llava.model.language_model.llava_llama import LlavaLlamaForCausalLM

dtype = torch.bfloat16

# model_path = "LLaVA-RLHF-13b-v1.5-336/sft_model" # this model is not available in 'https://huggingface.co/models'
# lora_path = "LLaVA-RLHF-13b-v1.5-336/rlhf_lora_adapter_model"

# general path:
model_path = "/claire-rcp-scratch/home/mekjavic/LLaVA-RLHF-13b-v1.5-336/sft_model"
lora_path = "/claire-rcp-scratch/home/mekjavic/LLaVA-RLHF-13b-v1.5-336/rlhf_lora_adapter_model"

model = LlavaLlamaForCausalLM.from_pretrained(
    model_path,
    device_map={"": "cuda:0"},
    torch_dtype=dtype,
)

model = PeftModel.from_pretrained( # pip install peft -> its a method to fine-tune large pretrained models in an efficient manner
    model,
    lora_path,
)
