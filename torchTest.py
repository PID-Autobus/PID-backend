import torch

# Imprimir la versión de PyTorch
print(f"PyTorch Version: {torch.__version__}")

# Verificar si CUDA está disponible y activo
cuda_available = torch.cuda.is_available()
cuda_active = torch.version.cuda is not None

print(f"CUDA Available: {cuda_available}")
print(f"CUDA Active: {cuda_active}")