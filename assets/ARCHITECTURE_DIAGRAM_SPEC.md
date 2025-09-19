# Architecture Diagram Specification

## Current Implementation Architecture

Based on the actual code implementation, here's what the new architecture diagram should show:

### 🎯 **Manager Agent (Hierarchical Coordinator)**
- **LLM**: Groq/Gemini (configurable)
- **Role**: Coordinates and delegates tasks to specialized agents
- **Process**: Hierarchical with memory enabled

### 🤖 **Three Specialized Agents**

#### 1. **Document RAG Agent** 📚
- **Tools**: 
  - ChromaDBTool (custom implementation)
- **Purpose**: Retrieves tax documents and internal data
- **Database**: ChromaDB with persistent storage in `db/` folder
- **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2

#### 2. **Web Agent** 🌐
- **Tools**:
  - SerperDevTool (web search)
  - ScrapeWebsiteTool (website content scraping)
- **Purpose**: Real-time web searches and website content scraping
- **Capability**: Scrapes and analyzes website content for competitor research

#### 3. **Code Execution Agent** 💻
- **Tools**: None (pure LLM reasoning)
- **Purpose**: Generates Python code for data visualization
- **Output**: Matplotlib visualization scripts

### 📋 **Four Sequential Tasks**

#### 1. **Fetch Tax Docs Task**
- **Agent**: Document RAG Agent
- **Action**: Query ChromaDB for relevant tax documents
- **Input**: User query about business data
- **Output**: Relevant tax documents

#### 2. **Answer Question Task**
- **Agent**: Web Agent  
- **Action**: Find competitors and financial data using web search
- **Tools Used**: SerperDevTool + WebsiteSearchTool
- **Output**: Markdown formatted answers

#### 3. **Business Trends Task**
- **Agent**: Document RAG Agent
- **Action**: Analyze tax data across years (2020-2023)
- **Data Source**: ChromaDB tax documents
- **Output**: `outputs/business_trends.md`

#### 4. **Graph Visualization Task**
- **Agent**: Code Execution Agent
- **Action**: Generate matplotlib visualization code
- **Input**: Data from business trends analysis
- **Output**: `outputs/visualize.ipynb`

### 🔧 **Technical Components**

#### **Data Storage**
- **ChromaDB**: Persistent vector database in `db/` folder
- **Internal Docs**: Sample business documents in `internal_docs/`
- **Outputs**: Generated reports in `outputs/` folder

#### **External APIs**
- **Groq/Gemini**: LLM inference (configurable)
- **Serper**: Web search API
- **HuggingFace**: Embedding models

#### **Configuration**
- **Environment**: `.env` file with API keys
- **Agents**: `config/agents.yaml`
- **Tasks**: `config/tasks.yaml`

### 🔄 **Data Flow**

1. **User Query** → Manager Agent
2. **Manager** → Document RAG Agent (fetch tax docs)
3. **Manager** → Web Agent (competitor research)  
4. **Manager** → Document RAG Agent (business trends analysis)
5. **Manager** → Code Execution Agent (visualization generation)
6. **Final Output** → Business report + visualization code


