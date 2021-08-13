import torch

state_dict = torch.load(r"C:\Users\GF\Desktop\yolov4-pytorch-master\new-data-no-mcl-l2\Epoch49-Total_Loss27.3518-Val_Loss35.9451.pth")
torch.save(state_dict, "yolov3.pth", _use_new_zipfile_serialization=False)