import openai

openai.api_key = "YOUR_AZURE_OPENAI_API_KEY"
openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com/"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # or another model available in your Azure OpenAI resource
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
