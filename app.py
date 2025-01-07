from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Create prompt templates
tone_template = """
Rewrite the following text in a {tone} tone. Maintain the same meaning and information,
but adjust the language, word choice, and style to match the {tone} tone.
Keep any HTML tags intact if present.

Text to rewrite:
{context}
"""

style_template = """
Analyze the following HTML and suggest Tailwind CSS classes to style it according to a {style} design:
{style_description}

HTML:
{html}

Provide only the Tailwind CSS classes that should be added or modified, in a JSON format with the element's identifier 
or type as the key and the classes as the value. Do not include existing classes unless they need to be modified.
"""

# Create prompt chains
tone_prompt = ChatPromptTemplate.from_template(tone_template)
tone_chain = LLMChain(llm=llm, prompt=tone_prompt)

style_prompt = ChatPromptTemplate.from_template(style_template)
style_chain = LLMChain(llm=llm, prompt=style_prompt)

@app.route('/api/change/tone', methods=['POST'])
def change_tone():
    try:
        data = request.json
        tone = data.get('tone')
        context = data.get('context')
        
        if not tone or not context:
            return jsonify({"error": "Missing tone or context"}), 400
        
        # Use Langchain to get response
        result = tone_chain.run({
            "tone": tone,
            "context": context
        })
        
        return jsonify({"result": result})
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/change/style', methods=['POST'])
def change_style():
    try:
        data = request.json
        style = data.get('style')
        html = data.get('html')
        
        if not style or not html:
            return jsonify({"error": "Missing style or HTML"}), 400
            
        style_prompts = {
            'minimal': "Clean, simple, lots of whitespace, muted colors",
            'modern': "Bold typography, high contrast, vibrant colors",
            'classic': "Traditional, elegant, serif fonts, subtle shadows",
            'bold': "Strong colors, large elements, dramatic contrasts",
            'playful': "Rounded corners, bright colors, fun animations"
        }
        
        style_description = style_prompts.get(style, style)
        
        # Use Langchain to get response
        result = style_chain.run({
            "style": style,
            "style_description": style_description,
            "html": html
        })
        
        return jsonify({"result": result})
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.getenv('OPENAI_API_KEY'):
        raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file")
    app.run(host='0.0.0.0', port=5001, debug=True)