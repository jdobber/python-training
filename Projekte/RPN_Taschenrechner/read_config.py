import toml
import json

config = """
[database]
port = 3000

[database2]
port = 6789
"""
#config = toml.load("config.toml")
config = toml.loads(config)

for key, value in config.items():
    #print(key, value)
    for param, param_value in value.items():
        print(key, ":", param, " => ", param_value)

#print("----")        
print( json.dumps(config, indent = 4) )