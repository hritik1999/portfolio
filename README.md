# AI-Powered Portfolio Site

A modern portfolio website built with Vue.js and Flask, featuring AI-powered content customization using GPT-4 through Langchain.

## Features

- **Dynamic Content Customization**
  - Tone adjustment using GPT-4
  - Style customization with Tailwind CSS
  - Custom tone and style options

- **Modern Tech Stack**
  - Frontend: Vue.js with shadcn-vue components
  - Backend: Flask with Gunicorn
  - Styling: Tailwind CSS
  - AI: Langchain with GPT-4
  - Containerization: Docker

## Prerequisites

- Docker and Docker Compose
- OpenAI API key

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio-site
```

2. Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your-api-key-here
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:80
- Backend API: http://localhost:5001

## Development Setup

### Frontend

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

### Backend

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run development server:
```bash
python app.py
```

## Docker Configuration

### Frontend Container
- Node.js 18 for building
- Nginx for serving
- Environment Variables:
  - `VITE_API_URL`: Backend API URL

### Backend Container
- Python 3.10
- Gunicorn server
- Environment Variables:
  - `OPENAI_API_KEY`: Your OpenAI API key
  - `PORT`: Server port (default: 5001)
  - `WORKERS`: Gunicorn workers (default: 4)

## API Endpoints

### `/api/change/tone`
Changes the tone of provided text content.

- Method: POST
- Body:
```json
{
  "tone": "professional",
  "context": "Text to modify"
}
```

### `/api/change/style`
Generates Tailwind CSS classes for the specified style.

- Method: POST
- Body:
```json
{
  "style": "modern",
  "html": "<div>HTML content</div>"
}
```

## Available Tones
- Professional
- Casual
- Friendly
- Formal
- Creative
- Custom (user-defined)

## Available Styles
- Minimal
- Modern
- Classic
- Bold
- Playful
- Custom (user-defined)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
