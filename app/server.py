import uvicorn
from pathlib import Path
import sys

def run_server():
    # Add the app directory to Python path
    app_path = Path(__file__).parent
    sys.path.append(str(app_path))
    
    # Configure uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Allows external access
        port=8000,
        reload=True,  # Enable auto-reload during development
        reload_dirs=[str(app_path)],  # Watch the app directory for changes
        log_level="info"
    )

if __name__ == "__main__":
    run_server()