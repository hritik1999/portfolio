from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

# Initialize Flask app
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
        print(data)
        if not tone or not context:
            return jsonify({"error": "Missing tone or context"}), 400
        
        # Use Langchain to get response
        tone_template = """
            Rewrite the following text in a {tone} tone. Maintain the same meaning and information,
            but adjust the language, word choice, and style to match the {tone} tone.
            Keep any HTML tags intact if present.

            Text to rewrite:
            {context}
            """
        tone_prompt = ChatPromptTemplate.from_template(tone_template)
        tone_chain = LLMChain(llm=llm, prompt=tone_prompt)
        result = tone_chain.run({
            "tone": tone,
            "context": context
        })
        print(result)
        return jsonify({"result": result})
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/change/style', methods=['POST'])
def change_style():
    try:
        data = request.json
        style = data.get('style', '').lower()
        html = data.get('html', '')
        
        if not style or not html:
            return jsonify({'error': 'Style and HTML are required'}), 400

        # Enhanced system message for more dramatic styling
        system_message = """You are an innovative web designer known for creating bold, distinctive themes that dramatically transform websites.
        Your designs should be striking and immediately recognizable, pushing the boundaries while maintaining usability.
        Each theme should feel like a complete transformation, not just a color change.
        Use the full power of Tailwind CSS classes to create dramatic visual effects.
        Consider every aspect of design: typography, spacing, shadows, animations, and layout.
        Each style should have its own unique personality and feel completely different from other styles."""

        # Enhanced prompt for more dramatic changes
        prompt = f"""Transform this HTML content into an extremely distinctive {style} theme that will completely change the look and feel of the website.
        
        Key Requirements:
        1. Color Scheme:
           - Use bold, theme-specific color combinations
           - Include multiple shades and accents
           - Consider gradient effects where appropriate
           - Use contrast strategically for visual impact
        
        2. Typography:
           - Choose dramatic font size differences between elements
           - Use distinctive font weights and letter spacing
           - Consider uppercase/lowercase styling
           - Implement creative line heights and text decorations
        
        3. Layout and Spacing:
           - Create unique rhythm with dramatic spacing differences
           - Use asymmetric layouts where appropriate
           - Implement distinctive padding and margin patterns
           - Consider negative space as a design element
        
        4. Components:
           - Give each component a strong, unique identity
           - Use bold shadows and borders
           - Implement distinctive corner treatments
           - Add subtle background patterns or textures
        
        5. Interactive Elements:
           - Create dramatic hover state transformations
           - Use scale, rotation, or position changes
           - Implement multi-step transitions
           - Consider cursor effects and focus states
        
        6. Theme-Specific Elements:
           For {style} specifically, consider:
           - What colors are iconic to this style?
           - What typography defines this style era/mood?
           - What shapes and patterns are associated with it?
           - What interactive behaviors would users expect?
        
        Return the styling in this JSON format:
        {{
            "theme": {{
                "background": "color value (consider gradients)",
                "text": "primary text color",
                "primary": "main brand color",
                "secondary": "supporting color",
                "accent": "highlight color",
                "patterns": ["optional background patterns/textures"]
            }},
            "typography": {{
                "headings": ["font-family", "weight", "letter-spacing", "text-transform"],
                "body": ["font-family", "weight", "line-height"],
                "sizes": {{
                    "h1": "dramatic size",
                    "h2": "distinctive size",
                    "body": "comfortable reading size"
                }}
            }},
            "components": {{
                "card": ["extensive card styling including shadows/borders"],
                "button": ["distinctive button styling with multiple states"],
                "nav": ["unique navigation styling"],
                "section": ["section-specific styling"]
            }},
            "spacing": {{
                "section": "dramatic padding/margin values",
                "container": "container-specific spacing",
                "elements": "inter-element spacing"
            }},
            "effects": {{
                "hover": ["dramatic hover transformations"],
                "transition": ["multi-step transitions"],
                "animation": ["optional subtle animations"]
            }}
        }}

        HTML Content to Style: {html}
        
        Remember: Be bold and creative - this should look dramatically different from a default theme while maintaining usability.
        """

        chat = ChatOpenAI(model="gpt-4o")
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=prompt)
        ]
        
        response = chat.invoke(messages)
        
        try:
            # Parse the response to ensure it's valid JSON
            style_data = json.loads(response.content)
            return jsonify({'result': style_data})
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract JSON from the response
            import re
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
    if not os.getenv('OPENAI_API_KEY'):
        raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file")
    app.run(host='0.0.0.0', port=5001, debug=True)