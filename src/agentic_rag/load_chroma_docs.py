import os
import sys
import chromadb
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

def load_documents_to_chromadb():
    """Load markdown documents from internal_docs directory to ChromaDB."""
    try:
        # Initialize SentenceTransformer model
        logger.info("Initializing SentenceTransformer model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize ChromaDB client with persistent storage
        logger.info("Connecting to ChromaDB...")
        # Get the project root directory (3 levels up from this file)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        db_path = os.path.join(project_root, "db")
        
        # Ensure the db directory exists
        os.makedirs(db_path, exist_ok=True)
        
        # Create ChromaDB client with persistent storage in the project's db directory
        chroma_client = chromadb.PersistentClient(path=db_path)
        collection = chroma_client.get_or_create_collection("tax_docs")
        
        # Get documents directory
        docs_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "internal_docs"
        )
        
        if not os.path.exists(docs_dir):
            logger.error(f"Documents directory not found: {docs_dir}")
            return False
            
        # Get markdown files
        try:
            markdown_files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]
        except OSError as e:
            logger.error(f"Error reading directory {docs_dir}: {e}")
            return False
            
        if not markdown_files:
            logger.warning(f"No markdown files found in {docs_dir}")
            return True
            
        logger.info(f"Found {len(markdown_files)} markdown files to process")
        
        # Process each file
        processed_count = 0
        for filename in markdown_files:
            file_path = os.path.join(docs_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                if not content.strip():
                    logger.warning(f"Skipping empty file: {filename}")
                    continue
                    
                # Generate embedding using SentenceTransformer
                logger.info(f"Processing {filename}...")
                embedding = model.encode(content).tolist()
                
                # Create unique ID
                doc_id = filename.split(".")[0]
                
                # Add document to ChromaDB
                collection.add(
                    documents=[content],
                    metadatas=[{"filename": filename, "file_path": file_path}],
                    ids=[doc_id],
                    embeddings=[embedding]
                )
                processed_count += 1
                logger.info(f"Successfully added {filename} to ChromaDB")
                
            except FileNotFoundError:
                logger.error(f"File not found: {file_path}")
                continue
            except UnicodeDecodeError as e:
                logger.error(f"Error reading file {filename}: {e}")
                continue
            except Exception as e:
                logger.error(f"Error processing file {filename}: {e}")
                continue
                
        logger.info(f"Successfully loaded {processed_count} documents into ChromaDB")
        return True
        
    except Exception as e:
        logger.error(f"Failed to load documents to ChromaDB: {e}")
        return False

if __name__ == "__main__":
    success = load_documents_to_chromadb()
    if not success:
        sys.exit(1)
    logger.info("Document loading completed successfully")