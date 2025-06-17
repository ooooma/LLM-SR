import gc
from argparse import ArgumentParser
import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# arguments
parser = ArgumentParser()
parser.add_argument('--model_name', type=str, default='qwen2.5:32b')
parser.add_argument('--host', type=str, default=None)
parser.add_argument('--port', type=int, default=None)
parser.add_argument('--temperature', type=float, default=0.8)
parser.add_argument('--do_sample', type=bool, default=True)
parser.add_argument('--max_new_tokens', type=int, default=512)
parser.add_argument('--top_k', type=int, default=30)
parser.add_argument('--top_p', type=float, default=0.9)
parser.add_argument('--num_return_sequences', type=int, default=1)
parser.add_argument('--max_repeat_prompt', type=int, default=10)
args = parser.parse_args()

# flask API
app = Flask(__name__)
CORS(app)

# Ollama API地址
OLLAMA_BASE_URL = "http://localhost:11434"

@app.route(f'/completions', methods=['POST'])
def completions():
    content = request.json
    prompt = content['prompt']
    repeat_prompt = content.get('repeat_prompt', 1)

    # parameters
    if 'params' in content:
        params: dict = content.get('params')
        max_new_tokens = params.get('max_new_tokens', args.max_new_tokens)
        temperature = params.get('temperature', args.temperature)
        do_sample = params.get('do_sample', args.do_sample)
        top_k = params.get('top_k', args.top_k)
        top_p = params.get('top_p', args.top_p)
        num_return_sequences = params.get('num_return_sequences', args.num_return_sequences)
        max_repeat_prompt = params.get('max_repeat_prompt', args.max_repeat_prompt)

    # 构建Ollama请求体
    ollama_request = {
        "model": args.model_name,
        "prompt": prompt,
        "options": {
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p
        },
        "stream": False,
        "max_tokens": max_new_tokens
    }

    responses = []
    # 处理重复请求
    for _ in range(min(repeat_prompt, max_repeat_prompt)):
        try:
            # 调用Ollama API
            response = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=ollama_request,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            result = response.json()
            responses.append(result.get("response", ""))
        except Exception as e:
            # 错误处理
            error_msg = f"Error generating response: {str(e)}"
            responses.append(error_msg)
            print(error_msg)

    # Send back the response.
    return jsonify({'content': responses})

if __name__ == '__main__':
    app.run(host=args.host, port=args.port)