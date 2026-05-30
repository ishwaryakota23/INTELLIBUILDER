from flask import Flask, request, jsonify
from flask_cors import CORS
from compiler import generate_config
from validator import validate_config
from repair import repair_config
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "IntelliBuilder Backend Running Successfully"


@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.json
        prompt = data["prompt"]

        config_text = generate_config(prompt)

        print("\n========== LLM RESPONSE ==========")
        print(config_text)
        print("==================================\n")

        # Remove markdown code fences added by Llama
        config_text = config_text.replace("```json", "")
        config_text = config_text.replace("```", "")
        config_text = config_text.strip()

        print("\n========== CLEANED JSON ==========")
        print(config_text)
        print("==================================\n")

        config = json.loads(config_text)
        config.pop(
            "permissions",
            None
            )
        errors = validate_config(config)
        print("\n========== VALIDATION ==========")
        if errors:
            for error in errors:
                print(error)
        else:
            print("No validation errors")
        print("================================\n")
        config, repairs = repair_config(config)
        print("\n========== REPAIR ENGINE ==========")
        if repairs:
            for repair in repairs:
                print(repair)
        else:
            print("No repairs needed")
        print("===================================\n")
        return jsonify({
            "config": config,
            "validation_errors": errors,
            "repairs": repairs
            })
    except Exception as e:
        print("\n========== ERROR ==========")
        print(str(e))
        print("===========================\n")
        return jsonify({
            "error": str(e)
            }), 500
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
