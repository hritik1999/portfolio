from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

app = Flask(__name__)
CORS(app)

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv('OPENAI_API_KEY')
)

@app.route('/api/change/tone', methods=['POST'])
def change_tone():
    try:
        data = request.json
        tone = data.get('tone')
        context = data.get('context')
        if not tone or not context:
            return jsonify({"error": "Missing tone or context"}), 400
        
        # Use Langchain to get response
        tone_template = """  
            Rewrite the following text in a {tone} tone while preserving its original meaning and information.  
            Adjust the language, word choice, and style to align with the {tone} tone.  

            Respond with only the rewritten text—no additional comments or explanations.  

            Text to rewrite:  
            {context}  
            """  
        tone_prompt = ChatPromptTemplate.from_template(tone_template)
        tone_chain = LLMChain(llm=llm, prompt=tone_prompt)
        result = tone_chain.run({
            "tone": tone,
            "context": context
        })
        print('input:',context)
        print('*'*50)
        print(result)
        print('*'*50)
        return jsonify({"result": result})
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, ssl_context=("cert.pem", "key.pem"))