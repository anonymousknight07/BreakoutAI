![image](https://github.com/user-attachments/assets/dc0587bc-10ad-4974-badd-ea671aa0c451)

# AI Data Extraction Agent

An intelligent data extraction system that combines web searching capabilities with LLM processing to automatically gather and process information from various sources. The system supports both CSV file uploads and Google Sheets integration for seamless data handling.

# Video tutorial 
[Video walkthrough](https://github.com/user-attachments/assets/c3438020-d9f4-4969-9efd-458ebae10920)

## 🌟 Key Features

### 1. Smart Data Input Dashboard

- **File Upload Support**
    - CSV file upload via intuitive browse button
    - Direct Google Sheets connection with authentication
    - Column preview and selection functionality
    - Dynamic data preview display

### 2. Dynamic Query System

- **Template-Based Queries**
    - Custom prompt creation with variable placeholders
    - Support for {company} style dynamic replacements
    - Multiple field extraction in single queries
    - Query template management and storage

### 3. Automated Web Search

- **Intelligent Search Processing**
    - Automated web searching for each entity
    - Rate-limited API calls to prevent blocking
    - Multiple search result aggregation
    - Structured data storage for LLM processing

### 4. LLM Integration

- **Advanced Data Extraction**
    - Groq API integration for data processing
    - Custom extraction prompts
    - Multi-field information extraction
    - Error handling and retry mechanisms

### 5. Results Management

- **Flexible Output Options**
    - Interactive results dashboard
    - CSV export functionality
    - Direct Google Sheets update option
    - Real-time progress tracking

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **Data Processing**: Pandas
- **APIs**:
    - Google Sheets API
    - SerpAPI/ScraperAPI
    - Groq API
- **Storage**: CSV and Google Sheets

## 📋 Prerequisites

1. Python 3.8 or higher
2. Google Cloud Platform account with:
    - Enabled Google Sheets API
    - Valid credentials
3. API keys for:
    - SerpAPI or ScraperAPI
    - Groq API
4. Stable internet connection

## 🚀 Installation

1. Clone the repository:
```bash 
git clone https://github.com/anonymousknight07/BreakoutAI.git
```



2. Create and activate a virtual environment:
```bash 
python -m venv venv source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3. Install dependencies:
```bash 
pip install -r requirements.txt
```



4. Configure environment variables:

```bash
cp .env.example .env 
```

cp .env.example .env

## ⚙️ Configuration

Set up your `.env` file with the following variables:

plaintext

Copy
```bash
#Google Sheets API Configuration 
GOOGLE_SHEETS_CREDENTIALS=path/to/credentials.json GOOGLE_SHEETS_TOKEN=path/to/token.json 

# Search API Configuration 
SERPAPI_API_KEY=your_serpapi_key SCRAPER_API_KEY=your_scraper_api_key 

# LLM API Configuration 
GROQ_API_KEY=your_groq_api_key #
```


## 📁 Project Structure

```bash
ai-data-extraction-agent/ 
├── api/ # API integrations 
│ ├── __init__.py │ 
  ├── google_sheets.py # Google Sheets integration 
│ ├── llm_api.py # Groq API handling
│ └── search_api.py # Search API integration ├── ui / # Frontend components 
│ ├── __init__.py │ ├── animations.py # UI animations 
│ └── dashboard.py # Main dashboard 
├── main.py # Application entry 
├── requirements.txt # Dependencies 
└── .env # Configuration

```



## 🎯 Usage Guide

### 1. Starting the Application

```bash
python main.py
```

- If you have installed streamlit 
```bash

streamlit run main.py

```

Access the dashboard at `http://localhost:8501`

### 2. Data Input

- **CSV Upload**:
    1. Click "Upload CSV" button
    2. Select your CSV file
    3. Choose the main entity column
- **Google Sheets**:
    1. Click "Connect to Google Sheets"
    2. Authenticate with Google
    3. Enter sheet URL
    4. Select target worksheet

### 3. Query Configuration

1. Enter your query template
    - Example: "Get me the email address of {company}"
    - For multiple fields: "Get the email and address for {company}"
2. Select target columns for extraction
3. Configure any additional parameters

### 4. Extraction Process

1. Click "Start Extraction"
2. Monitor progress in real-time
3. View results in the dashboard
4. Export or update Google Sheets as needed

## 🔧 Advanced Features

### 1. Multi-Field Extraction
```bash 
Example template 

"Extract the following for {company}: 
- Email address 
- Physical address 
- Phone number "

```


### 2. Google Sheets Integration

- Real-time sheet updates
- Multiple worksheet support
- Automated data synchronization

### 3. Error Handling

- Automatic retry mechanism
- Failed extraction logging
- User notifications
- Rate limit management

## 🚨 Troubleshooting

1. **Google Sheets Connection Issues**
    - Verify credentials
    - Check API enablement
    - Confirm sheet permissions
2. **Search API Problems**
    - Monitor rate limits
    - Check API key validity
    - Verify network connectivity
3. **LLM Processing Errors**
    - Validate API key
    - Check prompt format
    - Monitor usage limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Roadmap

- [ ]  Advanced query template builder
- [ ]  Batch processing optimization
- [ ]  Custom extraction rules
- [ ]  Advanced error recovery
- [ ]  Multiple LLM provider support

## 📞 Support

For support:

1. Check documentation
   - [How to create google service account](https://cloud.google.com/iam/docs/service-accounts-create)
   - [Google sheet API](https://developers.google.com/sheets/api/reference/rest)
   - [Groq AI](https://console.groq.com/docs/overview)
   - [Serpapi](https://serpapi.com/search-api)
2. Review existing issues
3. Create detailed bug reports


## 🙏 Acknowledgments

- SerpAPI/ScraperAPI for search capabilities
- Groq for LLM processing
- Google Cloud Platform for Sheets integration

---

Developed by Akshat Pandey

Made with ❤️ for data automation
