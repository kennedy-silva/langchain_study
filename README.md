# 🦜🔗 LangChain Study

Repositório de estudos práticos com **LangChain**, **LangGraph** e conceitos de IA generativa aplicados em Python. Os exemplos exploram desde cadeias simples até RAG (Retrieval-Augmented Generation) e agentes com memória conversacional.

---

## 📁 Estrutura do Projeto

```
langchain_study/
├── documentos/              # PDFs usados no exemplo de RAG
│   ├── GTB_standard_Nov23.pdf
│   ├── GTB_gold_Nov23.pdf
│   └── GTB_platinum_Nov23.pdf
├── env/                     # Ambiente virtual Python
├── main.py                  # Cadeia sequencial com parsers e modelos Pydantic
├── main_chat.py             # Chat com memória de sessão (histórico de conversa)
├── main_rag.py              # RAG com FAISS e documentos PDF
├── main_langgraph.py        # Fluxo de agente com LangGraph
├── requirements.txt         # Dependências do projeto
└── .gitignore
```

---

## 🚀 Exemplos

### `main.py` — Cadeia Sequencial com JSON Output
Demonstra como encadear múltiplos prompts usando LCEL (LangChain Expression Language). O fluxo:
1. Recebe um **interesse do usuário** (ex: "praias")
2. Sugere uma **cidade** com justificativa (saída estruturada em JSON via Pydantic)
3. Sugere **restaurantes** populares na cidade indicada
4. Finaliza sugerindo **atividades culturais** no destino

Conceitos abordados: `PromptTemplate`, `JsonOutputParser`, `RunnableLambda`, modelos Pydantic, encadeamento com `|`.

---

### `main_chat.py` — Chat com Memória de Sessão
Um chatbot de guia de viagem brasileiro com memória entre turnos. O assistente se apresenta como *"Sr. Passeios"* e mantém o contexto da conversa ao longo de múltiplas perguntas.

Conceitos abordados: `ChatPromptTemplate`, `InMemoryChatMessageHistory`, `RunnableWithMessageHistory`, gerenciamento de sessão.

---

### `main_rag.py` — RAG com FAISS e PDFs
Implementa um pipeline de **Retrieval-Augmented Generation** que carrega documentos PDF (regulamentos de cartões de viagem GTB), os divide em chunks, gera embeddings e responde perguntas com base no conteúdo dos documentos.

Conceitos abordados: `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OpenAIEmbeddings`, `FAISS`, retriever, `ChatPromptTemplate`.

---

### `main_langgraph.py` — Agente com LangGraph
Explora o uso do **LangGraph** para construir fluxos de agentes com estados e grafos dirigidos.

Conceitos abordados: `langgraph`, grafos de execução, nós e arestas condicionais.

---

## 🛠️ Tecnologias

- [LangChain](https://python.langchain.com/) — framework principal
- [LangGraph](https://langchain-ai.github.io/langgraph/) — orquestração de agentes
- [OpenAI GPT](https://platform.openai.com/) — modelos de linguagem (`gpt-4o-mini`, `gpt-3.5-turbo`)
- [FAISS](https://github.com/facebookresearch/faiss) — busca vetorial local
- [Pydantic](https://docs.pydantic.dev/) — validação e estruturação de dados
- [python-dotenv](https://pypi.org/project/python-dotenv/) — gerenciamento de variáveis de ambiente

---

## ⚙️ Instalação

### Pré-requisitos
- Python 3.10+
- Chave de API da OpenAI

### Passos

```bash
# Clone o repositório
git clone https://github.com/kennedy-silva/langchain_study.git
cd langchain_study

# Crie e ative o ambiente virtual
python -m venv env
source env/bin/activate        # Linux/macOS
env\Scripts\activate           # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```env
OPENAI_API_KEY=sk-...
```

---

## ▶️ Como Executar

```bash
# Cadeia sequencial com saída JSON
python main.py

# Chat com memória de sessão
python main_chat.py

# RAG com documentos PDF
python main_rag.py

# Agente com LangGraph
python main_langgraph.py
```

---

## 📚 Referências

- [Documentação LangChain](https://python.langchain.com/docs/)
- [Documentação LangGraph](https://langchain-ai.github.io/langgraph/)
- [LCEL — LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/)
- [OpenAI API](https://platform.openai.com/docs/)
