import os
import chromadb
import google.generativeai as genai
from chromadb import Documents, EmbeddingFunction, Embeddings


RAG_PROMPT_CONSTANT = """\
You are a helpful and informative bot that answers questions using text from the reference passage included below. \
Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
strike a friendly and converstional tone. \
If the passage is irrelevant to the answer, you may ignore it.

QUESTION: '{query}'
PASSAGE: '{relevant_passage}'

ANSWER:
"""

class GeminiEmbeddingFunction(EmbeddingFunction):
    """
    Custom embedding function using the Gemini AI API for document retrieval.

    This class extends the EmbeddingFunction class and implements the __call__ method
    to generate embeddings for a given set of documents using the Gemini AI API.

    Parameters:
    - input (Documents): A collection of documents to be embedded.

    Returns:
    - Embeddings: Embeddings generated for the input documents.
    """
    def __call__(self, input: Documents) -> Embeddings:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
        
        genai.configure(api_key=gemini_api_key)
        model = "models/embedding-001"
        title = "Custom query"

        return genai.embed_content(model=model, content=input, task_type="retrieval_document", title=title)["embedding"]

def generate_answer(db,query):
    def __generate_answer(prompt):
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        answer = model.generate_content(prompt)
        return answer.text
    
    #retrieve top 5 relevant text chunks
    relevant_text = get_relevant_passage(query,db,n_results=5)
    prompt = make_rag_prompt(query, relevant_passage="".join(relevant_text))
    answer = __generate_answer(prompt)

    return answer

def load_chroma_collection(path, name):
    chroma_client = chromadb.PersistentClient(path=path)
    return chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())


def get_relevant_passage(query, db, n_results):
  return db.query(query_texts=[query], n_results=n_results)['documents'][0]

def make_rag_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  return RAG_PROMPT_CONSTANT.format(query=query, relevant_passage=escaped)


if __name__=="__main__":
    db = load_chroma_collection(name="brts_chatbot_collection")
    answer = generate_answer(db, query="tell me about the brts system")
    print(answer)