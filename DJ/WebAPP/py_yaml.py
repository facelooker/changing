import yaml

with open("conf_fat.yml", "r") as file:
      content = file.read()


data = yaml.load(content,Loader=yaml.FullLoader)
print(data['host']['doname'],data['host']['port'])

