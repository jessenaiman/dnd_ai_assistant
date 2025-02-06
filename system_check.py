import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available.")
    
    # Get the number of available GPUs
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs available: {num_gpus}")
    
    # Check memory for each GPU
    for i in range(num_gpus):
        print(f"GPU {i}:")
        print(f"  Name: {torch.cuda.get_device_name(i)}")
        print(f"  Memory Usage:")
        print(f"    Allocated: {torch.cuda.memory_allocated(i) / 1e9:.2f} GB")
        print(f"    Cached: {torch.cuda.memory_reserved(i) / 1e9:.2f} GB")
        
        # You can also print a summary of memory usage
        print(torch.cuda.memory_summary(i))
else:
    print("CUDA is not available. Check your installation or GPU drivers.")