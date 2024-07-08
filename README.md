# Simple RAG Demo with Azure OpenAI and LangChain

This demo sets up a basic question-answering system using Azure OpenAI and LangChain. The system retrieves relevant documents and generates responses based on those documents.

## Prerequisites

1. **Azure Account**: Access to Azure OpenAI service.
2. **Python Environment**: Python installed with necessary libraries.
3. **LangChain Library**: Install LangChain.

## Step-by-Step Guide

### Step 1: Set Up Azure OpenAI

1. **Create Azure OpenAI Resource**:
   - Go to the Azure portal and create an Azure OpenAI resource.
   - Note the endpoint and API key.

2. **Install Azure OpenAI Python SDK**:
   ```
   pip install openai
   ```
Step 2: Install LangChain

pip install langchain

Step 3: Create a Simple Document Store
For this demo, you can use a simple list of documents.
```
documents = [
    {"title": "Document 1", "text": "Azure OpenAI provides powerful language models."},
    {"title": "Document 2", "text": "LangChain simplifies the integration of language models with data sources."},
    {"title": "Document 3", "text": "Retrieval-Augmented Generation (RAG) enhances the capability of language models by using external data."}
]
```
Step 4: Implement the Retrieval Component

For simplicity, we'll implement a basic retrieval function that searches for the most relevant document.

```
def simple_retrieval(query, documents):
    # Basic keyword search
    results = [doc for doc in documents if query.lower() in doc['text'].lower()]
    return results if results else documents
```

Step 5: Set Up Azure OpenAI Integration
Use the OpenAI SDK to generate responses.
```
import openai

openai.api_key = "YOUR_AZURE_OPENAI_API_KEY"
openai.api_base = "YOUR_AZURE_OPENAI_ENDPOINT"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # or another model available in your Azure OpenAI resource
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
```

Step 6: Combine Retrieval and Generation
Integrate the retrieval and generation steps.
```
def rag_query(query):
    # Step 1: Retrieve relevant documents
    retrieved_docs = simple_retrieval(query, documents)
    
    # Step 2: Generate response using the retrieved documents
    context = "\n".join([doc['text'] for doc in retrieved_docs])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    
    return generate_response(prompt)
```
# Example query
```
query = "What is RAG?"
response = rag_query(query)
print(response)
```
Running the Demo:

Ensure all necessary libraries are installed.
Replace placeholders with your actual Azure OpenAI API key and endpoint.
Run the script to see the Retrieval-Augmented Generation in action.
