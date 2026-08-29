from transformers import AutoModel
model = AutoModel.from_pretrained("bert-base-uncased")
model = model.to("cuda")  # <- demands an Nvidia GPU
