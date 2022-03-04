import torch

print(f"pytorch version: {torch.__version__}")
print(f"your device is cuda enabled: {torch.cuda.is_available()}")
print(f"if cuda is enabled, your device is: {torch.cuda.get_device_name(0)}")
print("torch.cuda.memory_allocated: %fGB"%(torch.cuda.memory_allocated(0)/1024/1024/1024))
print("torch.cuda.memory_reserved: %fGB"%(torch.cuda.memory_reserved(0)/1024/1024/1024))
print("torch.cuda.max_memory_reserved: %fGB"%(torch.cuda.max_memory_reserved(0)/1024/1024/1024))
# print(f"{torch.cuda.memory_summary()}")
print(f"TOTAL GPU MEMORY: {torch.cuda.get_device_properties(0).total_memory/1024/1024/1024} GB")
