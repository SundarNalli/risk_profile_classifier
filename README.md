# Risk Profile Classifier

An intelligent investment risk profiling system that uses AI to classify users into Conservative, Moderate, or Aggressive risk profiles based on their responses to carefully crafted questions.

## 🌟 Features

- **Interactive Quiz Interface**: User-friendly Streamlit web application
- **AI-Powered Classification**: Uses Ollama with Llama 3.2 model for intelligent risk assessment
- **Real-time Processing**: FastAPI backend with immediate response
- **LangGraph Workflow**: Structured conversation flow using LangGraph
- **Responsive Design**: Modern, intuitive user interface

## 🏗️ Architecture

The project follows a microservices architecture with the following components:

```
risk_profile_classifier/
├── agents/                 # AI agents for quiz and classification
│   ├── quiz_agent.py      # Manages quiz flow and question handling
│   └── classify_agent.py  # AI-powered risk classification
├── app/
│   └── graph.py           # LangGraph workflow definition
├── dashboard/
│   └── app.py             # Streamlit web interface
├── server/
│   └── main.py            # FastAPI backend server
├── data/
│   └── questions.json     # Quiz questions and options
└── utils/                 # Utility functions
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model downloaded in Ollama

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd risk_profile_classifier
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Ollama**
   ```bash
   # Install Ollama (if not already installed)
   # Visit https://ollama.ai/ for installation instructions
   
   # Download Llama 3.2 model
   ollama pull llama3.2
   ```

### Running the Application

1. **Start the FastAPI backend server**
   ```bash
   uvicorn server.main:app_fastapi --host 0.0.0.0 --port 8000 --reload
   ```

2. **Start the Streamlit dashboard** (in a new terminal)
   ```bash
   streamlit run dashboard/app.py
   ```

3. **Access the application**
   - Open your browser and go to `http://localhost:8501` (or the URL shown in the terminal)
   - Click "Start Quiz" to begin the risk profiling process

## 📋 Usage Guide

### Taking the Risk Profile Quiz

1. **Start the Quiz**: Click the "Start Quiz" button on the dashboard
2. **Answer Questions**: Respond to each question by selecting one of the provided options
3. **Complete the Assessment**: Continue until all questions are answered
4. **View Results**: Receive your personalized risk profile classification with explanation

### Sample Questions

The quiz includes questions such as:
- How would you react if your investment dropped 20% in a month?
- What's your investment goal time horizon?

### Risk Profile Categories

- **Conservative**: Low risk tolerance, capital preservation focus
- **Moderate**: Balanced approach to risk and return
- **Aggressive**: High risk tolerance, growth-focused strategy

## 🔧 API Endpoints

The FastAPI server provides the following endpoints:

- `GET /question` - Retrieve the next quiz question
- `POST /answer` - Submit an answer and get the next question or final classification
- `GET /reset` - Reset the quiz state

### Example API Usage

```bash
# Get first question
curl http://localhost:8000/question

# Submit answer
curl -X POST http://localhost:8000/answer \
  -H "Content-Type: application/json" \
  -d '{"answer": "Wait and watch"}'

# Reset quiz
curl http://localhost:8000/reset
```

## 🛠️ Development

### Project Structure

- **`agents/`**: Contains the core AI agents
  - `quiz_agent.py`: Manages quiz state and question flow
  - `classify_agent.py`: Handles AI-powered risk classification

- **`app/`**: LangGraph workflow definitions
  - `graph.py`: Defines the conversation flow using StateGraph

- **`dashboard/`**: Streamlit web interface
  - `app.py`: Main dashboard application

- **`server/`**: FastAPI backend
  - `main.py`: API endpoints and server logic

- **`data/`**: Configuration and data files
  - `questions.json`: Quiz questions and answer options

### Adding New Questions

To add new questions, edit `data/questions.json`:

```json
{
  "id": 3,
  "question": "Your new question here?",
  "type": "category",
  "options": ["Option 1", "Option 2", "Option 3"]
}
```

### Customizing the AI Model

The classification uses Ollama with Llama 3.2. To use a different model:

1. Update the model name in `agents/classify_agent.py`:
   ```python
   llm = ChatOllama(model="your-model-name")
   ```

2. Ensure the model is available in Ollama:
   ```bash
   ollama pull your-model-name
   ```

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'agents'**
   - Ensure you're running from the project root directory
   - Check that all import paths are correct

2. **Connection refused to localhost:8000**
   - Make sure the FastAPI server is running
   - Check if port 8000 is available

3. **Ollama model not found**
   - Ensure Ollama is running: `ollama serve`
   - Download the required model: `ollama pull llama3.2`

4. **JSONDecodeError in dashboard**
   - Verify the FastAPI server is responding correctly
   - Check server logs for any errors

### Debug Mode

To run in debug mode with more verbose output:

```bash
# FastAPI with debug
uvicorn server.main:app_fastapi --host 0.0.0.0 --port 8000 --reload --log-level debug

# Streamlit with debug
streamlit run dashboard/app.py --logger.level debug
```

## 📊 Performance

- **Response Time**: < 2 seconds for AI classification
- **Concurrent Users**: Supports multiple simultaneous users
- **Scalability**: Can be easily scaled with additional instances

## 🔒 Security

- No sensitive data is stored permanently
- All data is processed in memory
- No external API calls except to local Ollama instance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for AI workflow orchestration
- [LangGraph](https://langchain.com/langgraph) for conversation flow management
- [Ollama](https://ollama.ai/) for local LLM inference
- [Streamlit](https://streamlit.io/) for the web interface
- [FastAPI](https://fastapi.tiangolo.com/) for the backend API

## 📞 Support

For questions, issues, or contributions, please:
1. Check the troubleshooting section above
2. Search existing issues
3. Create a new issue with detailed information

---

**Happy Risk Profiling! 🎯**
