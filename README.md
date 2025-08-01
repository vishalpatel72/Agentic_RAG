# 🤖 Agentic RAG Practical Example

A comprehensive **Agentic RAG (Retrieval-Augmented Generation)** system built with [CrewAI](https://crewai.com) that demonstrates multi-agent collaboration for business intelligence and document analysis.

## ✨ Key Features

- **🗄️ ChromaDB Integration**: Document storage and retrieval with persistent vector database
- **🔍 Web Search Capabilities**: Real-time web search using SerperDevTool
- **🤝 Multi-Agent System**: Specialized agents for different tasks (RAG, Web Search, Code Execution)
- **⚡ Fast LLM Inference**: Supports Groq and Gemini APIs for high-speed processing
- **📊 Business Intelligence**: Automated analysis and visualization generation
- **🏗️ Hierarchical Process**: Manager agent coordinates specialized workers
- **🔧 Flexible Configuration**: Easy switching between LLM providers

📋 **[View Detailed Architecture Specification](./assets/ARCHITECTURE_DIAGRAM_SPEC.md)**

*Complete technical specification of the multi-agent architecture with ChromaDB integration, web scraping capabilities, and hierarchical task coordination for comprehensive business intelligence analysis.*

## 🚀 Quick Start

### Prerequisites
- Python >=3.10, <=3.13
- [UV](https://docs.astral.sh/uv/) for dependency management

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd agentic-rag-practical-example
   ```

2. **Install UV:**
   ```bash
   pip install uv
   ```

3. **Install dependencies:**
   ```bash
   crewai install
   ```

### Configuration

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Add your API keys to `.env`:**
   ```bash
   SERPER_API_KEY=your_serper_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   LLM=groq/llama3-70b-8192
   OPENAI_API_KEY=your_groq_api_key_here  # Used for CrewAI validation
   ```

3. **Load documents into ChromaDB (optional):**
   ```bash
   python src/agentic_rag/load_chroma_docs.py
   ```

### Running the Project

```bash
crewai run
```

This will:
- Analyze business documents using RAG
- Generate comprehensive business trends report
- Create visualization code for data insights
- Output results to `outputs/` directory

## 🏗️ Architecture

### Agents
- **📚 Document RAG Agent**: Retrieves information from ChromaDB vector database
- **🌐 Web Agent**: Performs real-time web searches using SerperDevTool
- **💻 Code Execution Agent**: Generates and executes analysis code

### Tasks
- **📋 Fetch Tax Docs**: Retrieves relevant documents from internal database
- **❓ Answer Question**: Provides detailed answers using RAG
- **📈 Business Trends**: Analyzes trends and generates insights
- **📊 Graph Visualization**: Creates data visualization code

### Tools
- **ChromaDBTool**: Custom tool for vector database operations
- **SerperDevTool**: Web search capabilities
- **ScrapeWebsiteTool**: Website content scraping and analysis

## 📁 Project Structure

```
agentic-rag-practical-example/
├── src/agentic_rag/
│   ├── config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   └── chromadb_tool.py     # Custom ChromaDB tool
│   ├── crew.py                  # Main crew definition
│   ├── main.py                  # Entry point
│   └── load_chroma_docs.py      # Document loader
├── internal_docs/               # Sample documents
├── db/                         # ChromaDB storage
├── outputs/                    # Generated reports
├── .env.example               # Environment template
└── README.md
```

## 🔧 Configuration Options

### Switching LLM Providers

The system supports multiple LLM providers. Update your `.env` file:

**For Groq:**
```bash
LLM=groq/llama3-70b-8192
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_groq_api_key
```

**For Gemini:**
```bash
LLM=gemini/gemini-1.5-pro
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_gemini_api_key
```

### Customizing Queries

Edit `src/agentic_rag/main.py` to change the analysis query:

```python
inputs = {
    "query": "Your custom business question here",
    "company": "Your Company Name",
    "company_description": "Brief company description",
}
```

## 📊 Output Examples

The system generates:

1. **Business Trends Report** (`outputs/business_trends.md`)
   - Financial analysis over multiple years
   - Revenue and expense trends
   - Profitability insights

2. **Visualization Code** (`outputs/visualize.ipynb`)
   - Python matplotlib scripts
   - Interactive data visualizations
   - Chart generation code

## 🛠️ Development

### Adding Custom Tools

1. Create a new tool in `src/agentic_rag/tools/`
2. Import and add to agent configuration in `crew.py`
3. Update agent YAML configurations as needed

### Training the Crew

```bash
crewai train <n_iterations> <filename>
```

### Testing

```bash
crewai test <n_iterations> <model_name>
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com) for the multi-agent framework
- [ChromaDB](https://www.trychroma.com/) for vector database capabilities
- [Groq](https://groq.com/) for fast LLM inference

