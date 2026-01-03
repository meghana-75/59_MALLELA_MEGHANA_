# **Drug Label Q&A + Dosage Reminder System (RAG)**

A real-time **Retrieval-Augmented Generation (RAG)** system built on **openFDA drug labels** that allows users to:

- Ask natural language questions about drugs  
- Retrieve accurate answers from FDA-approved labels  
- Generate a structured dosage reminder plan (JSON)  
- Run fully locally without external notification services  

---

# **Features**

  1.Real FDA drug label data (openFDA)

  2.RAG pipeline using LangChain + ChromaDB

  3.Semantic search over drug labels

  4.Natural language Q&A (ask_drug)

  5.Structured reminder plan per drug & dosage

  6.FastAPI backend (live testable
  
  7. Confidence-aware answers with FDA section traceability
  
  8. Risk-aware dosage reminders derived from safety warnings(Missing of dosage)

  9. Support for “what-if” medication safety questions

---

# **Tech Stack**

- **Language:** Python 3.9+  
- **LLM Framework:** LangChain  
- **Vector Database:** ChromaDB  
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2)  
- **Backend API:** FastAPI  
- **Data Source:** openFDA Drug Label Dataset 

---


## **Setup Instructions**

**Clone the repository**

git clone https://github.com/meghana-75/59_MALLELA_MEGHANA_.git

cd 59_MALLELA_MEGHANA_

---

# **Create virtual environment**

python -m venv venv

source venv/bin/activate     # Linux / Mac

venv\Scripts\activate        # Windows

---

# **Install dependencies**

pip install -r requirements.txt

# **Prepare the vector database**

python ingest.py

This step:

Loads FDA drug label data

Chunks the text

Generates embeddings

Stores vectors in ChromaDB

---

# **Must be run once before starting the API**

**Run the FastAPI server**

uvicorn api:app --reload

---

# **System Design**

User Query

   ↓
   
Retriever (ChromaDB)

   ↓
   
Relevant Drug Label Chunks

   ↓
   
LLM (LangChain)

   ↓
   
Answer + Reminder JSON

---

# **Requirements**

fastapi

uvicorn

langchain

chromadb

sentence-transformers

huggingface-hub

pydantic

---

## **Future Enhancements**

Drug–drug interaction analysis
Personalized dosage (age, condition)
React frontend
Cloud deployment
Local LLM support

---
