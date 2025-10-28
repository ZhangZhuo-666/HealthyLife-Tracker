# System Architecture

The HealthyLife Tracker system is designed with a **three-layer architecture** to ensure scalability and simplicity.

### 1. **Frontend**
- Developed using **HTML**, **CSS**, and **JavaScript**.
- Provides interactive pages for user registration, login, activity logging, and progress visualization.
- Sends requests to the backend through RESTful APIs.

### 2. **Backend**
- Implemented as a lightweight **API server** using Python (Flask) or Node.js (Express).
- Handles user authentication, request validation, and data processing.
- Communicates between frontend and database.

### 3. **Database**
- Stores user information, health records, and daily activity logs.
- Designed using **SQLite** or **MongoDB** for easy local development.

---

###  Data Flow Diagram

Below is the simplified workflow diagram showing how components interact:

```mermaid
flowchart TD
    A[User Interface<br>(Frontend)] --> B[API Gateway<br>(Backend Server)]
    B --> C[Authentication Service]
    B --> D[Data Processing Module]
    D --> E[Database<br>(User Data, Logs, Statistics)]
    E --> B
    B --> A
