from crewai.tools import BaseTool
import chromadb
from pydantic import BaseModel, Field
from typing import Type, Optional, Any
import json
import os


class ChromaDBToolSchema(BaseModel):
    """Input for ChromaDBTool."""

    query: str = Field(
        ...,
        description="The query to search retrieve relevant information from the ChromaDB database. Pass only the query, not the question.",
    )


class ChromaDBTool(BaseTool):
    """Tool to search the ChromaDB database"""

    name: str = "ChromaDBTool"
    description: str = "A tool to search the ChromaDB database for relevant information on internal documents"
    args_schema: Type[BaseModel] = ChromaDBToolSchema
    query: Optional[str] = None

    def _run(self, query: str) -> str:
        """Search the ChromaDB database

        Args:
            query (str): The query to search retrieve relevant information from the ChromaDB database. Pass only the query as a string, not the question.

        Returns:
            str: The result of the search query formatted as a readable string
        """
        try:
            # Get the project root directory (4 levels up from this file)
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            db_path = os.path.join(project_root, "db")
            
            # Ensure the db directory exists
            os.makedirs(db_path, exist_ok=True)
            
            # Create ChromaDB client with persistent storage in the project's db directory
            client = chromadb.PersistentClient(path=db_path)
            collection = client.get_or_create_collection("tax_docs")

            response = collection.query(
                query_texts=[query],
                n_results=3,
            )
            
            # Format the response into a readable string
            if not response['documents'] or not response['documents'][0]:
                return f"No relevant documents found for query: '{query}'"
            
            formatted_results = []
            documents = response['documents'][0]
            metadatas = response['metadatas'][0] if response['metadatas'] else [{}] * len(documents)
            distances = response['distances'][0] if response['distances'] else [0] * len(documents)
            
            for i, (doc, metadata, distance) in enumerate(zip(documents, metadatas, distances)):
                filename = metadata.get('filename', 'Unknown file')
                # Truncate document content for readability
                doc_preview = doc[:500] + "..." if len(doc) > 500 else doc
                
                formatted_results.append(
                    f"Document {i+1} (from {filename}, relevance: {1-distance:.3f}):\n"
                    f"{doc_preview}\n"
                )
            
            return "\n".join(formatted_results)
            
        except Exception as e:
            return f"Error searching ChromaDB: {str(e)}"
        
    def _format_response(self, response: dict) -> str:
        """Format ChromaDB response into readable string."""
        if not response.get('documents') or not response['documents'][0]:
            return "No documents found."
            
        results = []
        for i, doc in enumerate(response['documents'][0]):
            metadata = response['metadatas'][0][i] if response['metadatas'] else {}
            filename = metadata.get('filename', 'Unknown')
            preview = doc[:300] + "..." if len(doc) > 300 else doc
            results.append(f"[{filename}]: {preview}")
            
        return "\n\n".join(results)