# Business Impact Simulator

A backend application that simulates and analyzes the business impact of projects across different industry domains using AI agents.

## Overview

The Business Impact Simulator is a backend service that evaluates any project's potential impact within a specific industry domain. It uses a combination of AI agents to provide detailed insights into both technical and business implications.

## Features

- AI-powered project analysis
- Automatic domain classification
- Technical impact simulation
- Business impact analysis
- Data processing and validation
- Support for multiple industry domains

## Requirements

- Python 3.9 or higher
- OpenAI API key (for CrewAI)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/business_impact_simulator.git

# Navigate to the project directory
cd business_impact_simulator

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## API Usage

Start the backend server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### Key Endpoints

- `POST /api/analyze` - Analyze a project's impact
  ```python
  import requests

  # Example request
  response = requests.post(
      "http://localhost:8000/api/analyze",
      json={
          "project": {
              "name": "Project Name",
              "description": "Project Description",
              "content": {
                  "code": "...",
                  "documentation": "..."
              }
          },
          "specified_domain": "Healthcare"  # Optional
      }
  )
  ```

- `GET /api/health` - Health check endpoint

## Development

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set up your environment variables
5. Run tests: `pytest`
6. Start the development server: `uvicorn src.main:app --reload`

## Supported Domains

- Healthcare
- Financial Services
- Manufacturing
- Retail
- Education
- Logistics
- Energy
- Telecommunications
- Real Estate
- Hospitality

## License

MIT License
