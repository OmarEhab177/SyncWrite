# SyncWrite

SyncWrite is a simple web application built with Django and WebSockets that allows users to type text in a textarea on one web page and see the changes in real-time on another web page. 

## Requirements

- Django>=3.2.4,<3.3
- channels-redis==4.1.0
- uvicorn==0.22.0
- websockets==11.0.3

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/OmarEhab177/SyncWrite.git
cd syncwrite
```

Create a Python virtual environment and activate it.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages.

```bash
pip install -r requirements.txt
```

## Usage

Run the ASGI server using uvicorn.

```bash
uvicorn syncwrite.asgi:application
```

Now open your web browser and visit `http://127.0.0.1:8000/page1/` and `http://127.0.0.1:8000/page2/`. The text you type into the textarea on page1 should appear in real-time on page2, and vice versa.
