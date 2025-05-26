# Google Trends Keyword Crawler

## Description

This application fetches and displays trending Google search keywords for different timeframes using the `pytrends` library and a Flask web interface. Users can view trends for the past 24 hours, 48 hours (daily data), and 7 days (daily data).

## Features

*   Displays trending keywords for the past 24 hours.
*   Displays trending keywords for the past 48 hours (using daily trend data as a proxy).
*   Displays trending keywords for the past 7 days (using daily trend data as a proxy).
*   Simple and clean web interface.
*   Easy to set up and run.

## Project Structure

```
google-trends-crawler/
├── app/
│   ├── static/
│   │   └── style.css         # CSS styles for the web interface
│   ├── templates/
│   │   ├── base.html         # Base HTML template with navigation
│   │   └── trends.html       # HTML template for displaying trends
│   ├── __init__.py           # Initializes the Flask app and app package
│   ├── routes.py             # Defines application routes and view logic
│   └── utils.py              # Utility functions (e.g., fetching trends from pytrends)
├── requirements.txt          # Lists Python package dependencies
├── run.py                    # Main script to run the Flask application
└── README.md                 # This file
```

## Setup and Installation

1.  **Clone the Repository (if applicable):**
    If you have downloaded this project as a zip file, extract it. If it's a Git repository, you would clone it:
    ```bash
    # git clone <repository-url>
    # cd google-trends-crawler
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's good practice to create a virtual environment to manage project dependencies separately.
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```

3.  **Install Dependencies:**
    Install the required Python packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Run the Flask Application:**
    Execute the `run.py` script from the root directory of the project.
    ```bash
    python run.py
    ```

2.  **Access the Application:**
    Open your web browser and navigate to:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

    You should see the web page displaying trending keywords for the past 24 hours by default. You can use the navigation links to view trends for other timeframes.

## Dependencies

The application relies on the following Python libraries:

*   **Flask:** A micro web framework for Python, used to build the web interface.
*   **Pytrends:** An unofficial Google Trends API, used to fetch trending search data.

These are automatically installed when you run `pip install -r requirements.txt`.