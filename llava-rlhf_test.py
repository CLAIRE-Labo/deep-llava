import torch
from peft import PeftModel

from llava.model.language_model.llava_llama import LlavaLlamaForCausalLM

dtype = torch.bfloat16

model_path = "LLaVA-RLHF-13b-v1.5-336/sft_model" # this model is not available in 'https://huggingface.co/models'
lora_path = "LLaVA-RLHF-13b-v1.5-336/rlhf_lora_adapter_model"

model = LlavaLlamaForCausalLM.from_pretrained(
    model_path,
    device_map={"": "cuda:0"},
    torch_dtype=dtype,
)

model = PeftModel.from_pretrained(
    model,
    lora_path,
)
