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

load_dotenv()
app = Flask(__name__)
CORS(app)

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
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

@app.route('/api/change/theme', methods=['POST'])
def generate_theme():
    try:
        data = request.json
        theme = data.get('theme')
        
        if not theme:
            return jsonify({"error": "missing theme"}), 400

        class Theme(BaseModel):
            background: str = Field(description="Color value for background, consider gradients")
            text: str = Field(description="Primary text color")
            primary: str = Field(description="Main brand color")
            secondary: str = Field(description="Supporting color")
            accent: str = Field(description="Highlight color")
            patterns: List[str] = Field(description="Optional background patterns or textures")

        class Typography(BaseModel):
            headings: Dict[str, List[str]] = Field(description="Font settings for headings")
            body: Dict[str, List[str]] = Field(description="Font settings for body text")
            sizes: Dict[str, str] = Field(description="Font sizes for different elements")

        class Components(BaseModel):
            card: List[str] = Field(description="Extensive card styling")
            button: List[str] = Field(description="Distinctive button styling")
            nav: List[str] = Field(description="Unique navigation styling")
            section: List[str] = Field(description="Section-specific styling")

        class Spacing(BaseModel):
            section: str = Field(description="Dramatic padding/margin values")
            container: str = Field(description="Container-specific spacing")
            elements: str = Field(description="Inter-element spacing")

        class Effects(BaseModel):
            hover: List[str] = Field(description="Hover transformations")
            transition: List[str] = Field(description="Multi-step transitions")
            animation: List[str] = Field(description="Optional subtle animations")

        class ThemeTemplate(BaseModel):
            theme: Theme
            typography: Typography
            components: Components
            spacing: Spacing
            effects: Effects

        class ThemeResponse(BaseModel):
            lightTheme: ThemeTemplate
            darkTheme: ThemeTemplate 

            class Config:
                json_schema_extra = {
                    "type": "object",
                    "properties": {
                        "lightTheme": {
                            "type": "object",
                            "properties": {
                                "theme": {"type": "object"},
                                "typography": {"type": "object"},  # Just define as object, no required here
                                "components": {"type": "object"},
                                "spacing": {"type": "object"},
                                "effects": {"type": "object"},
                            },
                            "required": ["theme", "typography", "components", "spacing", "effects"]  # Only these top-level fields are required
                        },
                        "darkTheme": {
                            "type": "object",
                            "properties": {
                                "theme": {"type": "object"},
                                "typography": {"type": "object"},  # Same fix here, no required in nested properties
                                "components": {"type": "object"},
                                "spacing": {"type": "object"},
                                "effects": {"type": "object"},
                            },
                            "required": ["theme", "typography", "components", "spacing", "effects"]  # Only top-level fields
                        }
                    },
                    "required": ["lightTheme", "darkTheme"]  # Light and dark themes are required
                }
                

        # Create the prompt template
        theme_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an innovative web designer known for creating bold, distinctive themes that dramatically transform websites.
            Your designs should be striking and immediately recognizable, pushing the boundaries while maintaining usability.
            Each theme should feel like a complete transformation, not just a color change.
            Use the full power of Tailwind CSS classes to create dramatic visual effects.
            Consider every aspect of design: typography, spacing, shadows, animations, and layout.
            Each style should have its own unique personality and feel completely different from other styles.
             
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
                For {theme} specifically, consider:
                - What colors are iconic to this style?
                - What typography defines this style era/mood?
                - What shapes and patterns are associated with it?
                - What interactive behaviors would users expect?

             """),
            ("human", "Generate matching light and dark themes for {theme}. Use HSL format for all colors.")
        ])


        structured_llm = llm.with_structured_output(ThemeResponse)
        # Create and run the chain
        theme_chain = theme_prompt | structured_llm

        result = theme_chain.invoke({"theme": theme})
        return jsonify(result.model_dump())

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001,debug=True)