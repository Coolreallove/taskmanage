import yaml 
with open ("Sample.yaml","r") as f:
    data = yaml.safe_load(f)
print (data)