Welcome to the retain coding challenge. This assignment consists of two independent tasks designed to evaluate your skills in both refactoring existing code and building a new feature from scratch. You are expected to complete both tasks within the time.

Task 1: Code Refactoring Challenge

Overview
You've inherited a legacy user management API that works but has significant issues. Your task is to refactor and improve this codebase while maintaining its functionality.
Getting Started
Prerequisites
Python 3.8+ installed
Tech Stack
This is an open-ended challenge. You can use any tech stack you choose. The original application is built with Python, but feel free to migrate to a different language or framework if you think it's a better architectural decision. 

Some common options include:
Frontend: React, HTML, CSS, JavaScript
Backend:  Node, REST APIs, Python, FastAPI, SQLAlchemy, Pandas
Data & Infra: PostgreSQL, AWS, Docker
Setup (Should take < 5 minutes)
Access the codebase via this Drive link: https://drive.google.com/file/d/1VkL8uMy60faAgKdiI4nxe5UTUaQCSXbe/view?usp=sharing
# Clone/download this repository
# Navigate to the assignment directory
cd messy-migration


# Install dependencies
pip install -r requirements.txt


# Initialize the database
python init_db.py


# Start the application
python app.py


# The API will be available at http://localhost:5000

Testing the Application
The application provides these endpoints:
GET / - Health check
GET /users - Get all users
GET /user/<id> - Get specific user
POST /users - Create new user
PUT /user/<id> - Update user
DELETE /user/<id> - Delete user
GET /search?name=<name> - Search users by name
POST /login - User login
Refactor this codebase to improve its quality, security, and maintainability. The application currently works but has numerous issues that need addressing.
What We're Looking For
Code Organization (25%)
Proper separation of concerns
Clear project structure
Meaningful function/variable names
Security Improvements (25%)
Identify and fix security vulnerabilities
Implement proper data validation
Secure sensitive information
Best Practices (25%)
Error handling
Proper HTTP status codes
Code reusability
Documentation (25%)
Clear explanation of changes made
Justification for architectural decisions
Any trade-offs you made
What to Focus On
Identify the most critical issues first
Make the code production-ready
Ensure the API remains functional
Write at least a few tests for critical functionality
What NOT to Do
Don't add new features or endpoints
Don't spend time on UI/frontend
Don't over-engineer the solution
Don't aim for 100% test coverage
Don't create extensive documentation beyond explaining your changes
Submission
Deliverables
Your refactored code
A CHANGES.md file documenting:
Major issues you identified
Changes you made and why
Any assumptions or trade-offs
What you would do with more time
How to Submit
Create a new git repository with your solution
Include all necessary files to run the application
Ensure python app.py still works after setup
Share the repository link
Evaluation Criteria
We will evaluate your submission based on:
The quality of your solutions.
The identification of critical issues.
The readability and organization of your code.
Your pragmatic decision-making.
The clarity of your communication.
AI Usage Policy
You are permitted to use AI assistants (e.g., ChatGPT, GitHub Copilot) as you would any other tool. If you use AI significantly, please make a note in your CHANGES.md file, including:
Which tools you used.
What you used them for.
Any AI-generated code you modified or rejected.

Questions?
If you have questions about the requirements, please email anand@retainsure.com within the first 30 minutes of starting the challenge.
Remember: We are not looking for perfection. We want to see how you approach real-world coding problems, prioritize improvements, and communicate your decisions effectively. Good luck!













Task 2: URL Shortener Service

Overview
Build a simple URL shortening service similar to bit.ly or tinyurl. This assignment tests your ability to design and implement a small but complete feature from scratch.
Getting Started
Prerequisites
Python 3.8+ installed
Setup (Should take < 5 minutes)
# Clone/download this repository
# Navigate to the assignment directory
cd url-shortener


# Install dependencies
pip install -r requirements.txt


# Start the application
python -m flask --app app.main run


# The API will be available at http://localhost:5000
# Run tests with: pytest



What's Provided
Basic Flask application structure
Health check endpoints
One example test
Empty files for your implementation
Your Task
Build a URL shortener service with the following features:
Core Requirements
Shorten URL Endpoint
POST /api/shorten
Accept a long URL in the request body
Return a short code (e.g., "abc123")
Store the mapping for later retrieval
Redirect Endpoint
GET /<short_code>
Redirect to the original URL
Return 404 if short code doesn't exist
Track each redirect (increment click count)
Analytics Endpoint
GET /api/stats/<short_code>
Return click count for the short code
Return creation timestamp
Return the original URL
Technical Requirements
URLs must be validated before shortening
Short codes should be 6 characters (alphanumeric)
Handle concurrent requests properly
Include basic error handling
Write at least 5 tests covering core functionality
Example API Usage
# Shorten a URL
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/very/long/url"}'


# Response: {"short_code": "abc123", "short_url": "http://localhost:5000/abc123"}


# Use the short URL (this redirects)
curl -L http://localhost:5000/abc123


# Get analytics
curl http://localhost:5000/api/stats/abc123


# Response: {"url": "https://www.example.com/very/long/url", "clicks": 5, "created_at": "2024-01-01T10:00:00"}

 


Implementation Guidelines
What We're Looking For
Code Quality (30%)
Clean, readable code
Proper error handling
Good API design
Functionality (30%)
All requirements work correctly
Handles edge cases appropriately
Concurrent request handling
Testing (20%)
Tests for main functionality
Tests for error cases
Clear test descriptions
Architecture (20%)
Logical code organization
Separation of concerns
Scalable design decisions
What to Focus On
Get core functionality working first
Use appropriate data structures
Handle common error cases
Keep it simple but complete
What NOT to Do
Don't implement user authentication
Don't add a web UI
Don't implement custom short codes
Don't add rate limiting
Don't use external databases (in-memory is fine)
Submission
Deliverables
Your complete implementation
All tests passing
Brief notes about your approach (optional)
How to Submit
Ensure all tests pass: pytest
Create a zip of your solution
Include any notes about your implementation choices
Share the repository link
Evaluation Criteria
We will evaluate your submission based on:
The quality of your solutions.
The identification of critical issues.
The readability and organization of your code.
Your pragmatic decision-making.
The clarity of your communication.
AI Usage Policy
You are permitted to use AI assistants (e.g., ChatGPT, GitHub Copilot) as you would any other tool. If you use AI significantly, please make a note in your CHANGES.md file, including:
Which tools you used.
What you used them for.
Any AI-generated code you modified or rejected.

Questions?
If you have questions about the requirements, please email anand@retainsure.com within the first 30 minutes of starting the challenge.
Remember: We are not looking for perfection. We want to see how you approach real-world coding problems, prioritize improvements, and communicate your decisions effectively. Good luck!


