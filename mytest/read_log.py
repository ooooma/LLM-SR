import json
with open('../logs/oscillator2_local_torch2/samples/samples_0.json' , 'r') as f:
    data = json.load(f)
print(data['function'])