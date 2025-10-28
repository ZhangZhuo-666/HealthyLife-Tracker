# System Architecture

The system consists of four main components:

1. **Frontend:**  
   Provides the user interface built with HTML, CSS, and JavaScript.  
   It allows users to record their daily activities, view statistics, and receive reminders.

2. **Backend:**  
   A lightweight API server that handles user requests, manages data flow, and performs basic logic processing.

3. **Database:**  
   Stores user data such as activity logs, daily goals, and health summaries.

4. **Data Analysis & Reports:**  
   Analyzes user data and generates visual summaries to help users track progress and maintain motivation.

---

### System Flow Diagram

```mermaid
flowchart LR
    A[User Interface (Frontend)] --> B[Application Logic (Backend)]
    B --> C[Database (User Data, Activity Logs)]
    C --> D[Data Analysis & Reports]
    A --> E[User Authentication]
    E --> B
