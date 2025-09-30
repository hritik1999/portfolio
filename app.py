from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field
from typing import List, Dict
import json
import os
import json, re

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/api/change/tone', methods=['POST'])
def change_tone():
    try:
        data = request.json
        tone = data.get('tone')
        context = data.get('context')
        if not tone or not context:
            return jsonify({"error": "Missing tone or context"}), 400
        
        llm = ChatOpenAI(
            model="gpt-5",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
                
        # Use Langchain to get response
        tone_template = """  
            As part of Hritik Gupta's professional portfolio website, Rewrite the following text in a {tone} tone while preserving its original meaning and information.  
            Adjust the language, word choice, and style to align with the {tone} tone.  

            Guidelines:
                1. Maintain first-person perspective where appropriate
                2. Respond with only the rewritten text—no additional comments or explanations.  

            Text to rewrite:  
            {context}  
            """  
        tone_prompt = ChatPromptTemplate.from_template(tone_template)
        tone_chain = tone_prompt | llm
        result = tone_chain.invoke({
            "tone": tone,
            "context": context
        })
        print(result)
        return jsonify({"result": result.content})
            
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/api/change/style', methods=['POST'])
def change_style():
    try:
        data = request.json
        style = data.get('style', '').lower()
        html = data.get('html', '')
        if not style or not html:
            return jsonify({'error': 'Style and HTML are required'}), 400

        # Enhanced system message with emphasis on bold design and high contrast
        system_message = (
            "You are an innovative web designer known for creating bold, distinctive themes that "
            "dramatically transform websites. Your designs must incorporate animated gradients, "
            "and creative typography—all while ensuring all text remains legible with at least a 7:1 contrast ratio "
            "Focus on dramatic background changes—using bold gradients, unique patterns"
            "while ensuring the rest of the design remains cohesive and usable. "
        )

        # Enhanced prompt to drive dramatic styling
        prompt = (
            f"Transform this HTML content into an extremely distinctive {style} theme that completely overhauls "
            "the look and feel of the website.\n\n"
            "Key Requirements:\n"
            "1. Color Scheme:\n"
            "   - Use bold, theme-specific color combinations with at least 7:1 contrast for text.\n"
            "   - Include multiple shades, accents, and gradient effects if appropriate.\n"
            "   - Ensure that text remains readable even over gradients or patterns.\n\n"
            "2. Typography:\n"
            "   - Choose dramatic font sizes, weights, and creative letter spacing.\n"
            "   - Consider inventive uppercase/lowercase styles and line heights.\n\n"
            "3. Layout and Spacing:\n"
            "   - Create unique, asymmetric layouts with dramatic padding/margin patterns.\n\n"
            "4. Components:\n"
            "   - Give each component a strong, unique identity using bold shadows, borders, and creative corner treatments.\n"
            "   - Optionally include subtle background patterns or textures.\n\n"
            "5. Background Transformation:\n"
            "   - Drastically change the background using bold gradients, dynamic images, or intricate patterns.\n"
            "   - Ensure the background is the most dramatic change, setting a completely new tone for the site.\n"
            "   - If using gradients or patterns, incorporate overlays to maintain text legibility (at least 7:1 contrast).\n\n"
            "6. Interactive Elements:\n"
            "   - Create dramatic hover transformations with scale, rotation, or position changes.\n"
            "   - Implement multi-step transitions and engaging focus effects.\n\n"
            "7. Theme-Specific Elements:\n"
            f"   For {style}, think about what colors, typography, interactive behaviors and background define the style.\n\n"
            "Return the styling in this JSON format:\n"
            "{\n"
            "    \"theme\": {\n"
            "         \"background\": \"completely transformed background style (e.g., a gradient or patterned image)\",\n"
            "        \"text\": \"primary text color\",\n"
            "        \"primary\": \"main brand color\",\n"
            "        \"secondary\": \"supporting color\",\n"
            "        \"accent\": \"highlight color\",\n"
            "        \"patterns\": [\" background patterns/textures\"]\n"
            "    },\n"
            "    \"typography\": {\n"
            "        \"headings\": [\"font-family\", \"weight\", \"letter-spacing\", \"text-transform\"],\n"
            "        \"body\": [\"font-family\", \"weight\", \"line-height\"],\n"
            "        \"sizes\": {\n"
            "            \"h1\": \"dramatic size\",\n"
            "            \"h2\": \"distinctive size\",\n"
            "            \"body\": \"comfortable reading size\"\n"
            "        }\n"
            "    },\n"
            "    \"components\": {\n"
            "        \"card\": [\"extensive card styling including shadows/borders\"],\n"
            "        \"button\": [\"distinctive button styling with multiple states\"],\n"
            "        \"nav\": [\"unique navigation styling\"],\n"
            "        \"section\": [\"section-specific styling\"]\n"
            "    },\n"
            "    \"spacing\": {\n"
            "        \"section\": \"dramatic padding/margin values\",\n"
            "        \"container\": \"container-specific spacing\",\n"
            "        \"elements\": \"inter-element spacing\"\n"
            "    },\n"
            "    \"effects\": {\n"
            "        \"hover\": [\"dramatic hover transformations\"],\n"
            "        \"transition\": [\"multi-step transitions\"],\n"
            "        \"animation\": [\"optional subtle animations\"]\n"
            "    }\n"
            "}\n\n"
            f"HTML Content to Style: {html}\n\n"
            "Be bold and creative while ensuring all text remains legible and accessible."
        )

        # Create and send messages to the LLM
        chat = ChatOpenAI(model="gpt-5-mini", temperature=0.3)
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=prompt)
        ]
        response = chat.invoke(messages)

        try:
            style_data = json.loads(response.content)
            return jsonify({'result': style_data})
        except json.JSONDecodeError:
            # Try to extract JSON if the response contains extra text
            json_match = re.search(r'({[\s\S]*})', response.content)
            if json_match:
                try:
                    style_data = json.loads(json_match.group(1))
                    return jsonify({'result': style_data})
                except json.JSONDecodeError:
                    return jsonify({'error': 'Invalid style data format'}), 500
            return jsonify({'error': 'Invalid style data format'}), 500

    except Exception as e:
        print(f"Error in change_style: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001,debug=True)
