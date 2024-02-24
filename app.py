import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts.prompt import PromptTemplate
import os
from dotenv import load_dotenv
from pathlib import Path
import json

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
openai_api_key = os.getenv('OPENAI_API_KEY')


llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=1, model="gpt-3.5-turbo")

output = llm.invoke("""Pink Eyeshadow and Fuchsia Lips
Step into the spotlight with a dazzling pink monochromatic moment that's equal parts simplicity and striking allure! Dive into the magical realm of our 'Eye Lit You So!' Vivid Eyeliner - 01 Pink Sphinx, setting the stage for glamour.



But we're not stopping there – ignite the scene with our 'Mettle Satin Lipstick' in the vivacious shade 'Elizabeth' for those premium-looking lips. This dynamic duo ensures your look is both modern and mesmerizing, proving that the allure of pink knows no bounds.



How to Get The Look:

Step 1: Start with a pink eyeliner and trace your eyes with the desired look you want
Step 2: Top it up with the highly pigmented 'Contour De Force Eyes And Face Palette - 02 - Pink Pro.'
Step 3: Create a small wing with a black eyeliner or continue the drama with a pink liner
Step 4: For lips, line your lips with 'Lipping On The Edge Lip Liner - 04 Tan Fan' and fill in with a subtle nude pink lipstick
""" + """\n I need to create a webstory for this information. Give me a heading and 1 line summary of this information. Make the heading lucrative and emphasizing on the information. Provide output in the format of JSON as follows:
{
    "heading" : <web-story-heading>,
    "summary' : <web-story-summary>
}""")

print(json.loads(output.content)["heading"])
print(json.loads(output.content)["summary"])