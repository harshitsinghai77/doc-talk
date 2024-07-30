# doc-talk

Building a document-based question answering system similar to ChatGPT for company's internal use. This system utilizes FastAPI for a REST API, Langchain for document storage and retrieval, FAISS for vector similarity search, and Meta's llama3 model for question answering. Users can upload documents, ask questions about them, and receive concise answers with document references. Aiming for a production-ready solution with containerization, detailed documentation, and a Streamlit frontend (planned).

## Usage

1. Upload documents using the `/upload` endpoint or the Streamlit frontend.
2. Process directories of documents using the `/process-directory` endpoint.
3. Ask questions about the uploaded documents using the `/ask` endpoint or the Streamlit frontend.
4. Retrieve task status and manage the document store using the corresponding API endpoints.

## API Endpoints

- `/ask` (POST): Ask a question about the uploaded documents.
- `/upload` (POST): Upload a single document file.
- `/process-directory` (POST): Process a directory of documents.
- `/task/{task_id}` (GET): Retrieve the status of a task.
- `/search` (POST): Search for documents based on a query.
- `/save` (POST): Save the document store to a file.
- `/load` (POST): Load the document store from a file.
- `/clear` (POST): Clear the document store.
- `/document-count` (GET): Get the count of documents in the store.
- `/clear-old-tasks` (POST): Clear old tasks from the task list.

For detailed information on the request and response formats, refer to the API documentation.
