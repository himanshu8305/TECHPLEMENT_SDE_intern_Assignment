# Log Query Interface
This project provides a simple web-based log query interface for searching and filtering logs stored in log files. It consists of a Flask backend for handling search requests and serving the frontend UI, and a basic HTML/CSS/JavaScript frontend for user interaction.

# How to Run the Project
1. Clone the repository to your local machine:
git clone <repository_url>
cd log-query-interface

2. Install dependencies:
pip install Flask

3. Start the Flask server:
python log_query_interface.py

4. Open a web browser and navigate to http://localhost:5000 to access the log query interface.


# System Design
The system consists of two main components:
1. Log Ingestor (not provided in this repository):
=> Responsible for receiving logs from various sources/APIs and storing them in log files.
=> Logs are stored in JSON format with standardized fields like level, log_string, timestamp, and metadata.
=> Log files are organized based on source and log level (e.g., log1.log, log2.log, etc.).

2. Query Interface:
=> Provides a web-based UI for users to search and filter logs.
=> Backend built using Flask to handle search requests and serve the frontend UI.
=> Frontend implemented using HTML/CSS/JavaScript for user interaction.

# Features Implemented
Search Logs: Users can enter a search query to find logs containing specific keywords.
Filter Logs: Users can apply filters based on log level, log message, and source.
Clear Results: Users can clear the search results to perform a new search.

# Identified Issues
Dummy Data: The search functionality currently uses dummy data. Real log data from log files should be integrated for actual use.
Scalability: The system may face scalability issues when handling a large volume of logs. Optimizations may be needed for efficient log retrieval.
Security: The system lacks authentication and authorization mechanisms. Implementing role-based access control and securing endpoints would be necessary for production use.
