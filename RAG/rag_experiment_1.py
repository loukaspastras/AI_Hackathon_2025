# -*- coding: utf-8 -*-
#!pip install langchain openai faiss-cpu

#!pip install sentence-transformers faiss-cpu

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Only if you're using this specific splitter

# 1. Function to load the text file
def load_text_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# 2. Function to split text into chunks
def split_text_into_chunks(text, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

# 3. Function to create embeddings using Sentence Transformers
def create_vector_store(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose another model
    embeddings = model.encode(chunks, convert_to_tensor=True)
    vector_store = faiss.IndexFlatL2(embeddings.shape[1])   # FAISS index
    vector_store.add(np.array(embeddings))  # Add embeddings to FAISS
    return vector_store

# 4. Function to retrieve the most relevant chunk based on the user's query
def retrieve_relevant_chunks(query, vector_store, chunks, k=2):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Same model for query
    query_embedding = model.encode([query], convert_to_tensor=True)

    # Search the vector store to find the most similar chunks
    distances, indices = vector_store.search(np.array(query_embedding), k=k)

    # Get the top k most relevant chunks based on the indices
    relevant_chunks = [chunks[i] for i in indices[0]]  # Extract the corresponding chunks
    return relevant_chunks

# 5. Example workflow
def run_rag_workflow(file_path, user_query):
    # Step 1: Load and split the text file
    text = load_text_file(file_path)
    chunks = split_text_into_chunks(text)

    # Step 2: Create a vector store
    vector_store = create_vector_store(chunks)

    # Step 3: Retrieve the two most relevant chunks for the user's query
    relevant_chunks = retrieve_relevant_chunks(user_query, vector_store, chunks, k=2)  # Set k=2 for two most relevant chunks

    # Return the two most relevant chunks
    return relevant_chunks

# 6. Separate function to print all chunks
def print_all_chunks(chunks):
    print("All Chunks:")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk}\n")

""" Example Usage

# Run the example with your file and query
file_path = "test.txt"  # Provide the path to your text file
user_query = "beautiful world"  # Example query
relevant_chunk = run_rag_workflow(file_path, user_query)

# Output the result
print("Most relevant chunk:", relevant_chunk)

"""
