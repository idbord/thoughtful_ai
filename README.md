# Thought.AI Coding Interview Take Home

## Setting up the Environment
1. Clone the repository
2. Navigate to the project directory:
   ```bash
   cd thoughtful_ai_coding_interview
    ```
3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
    ```
4. Activate the virtual environment:
    
    On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
     On Windows:
     ```bash
     .venv\Scripts\activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Test Classes
To ensure the package sorting logic works as expected, you can run the provided test suite using pytest.

1. Make sure your virtual environment is activated and dependencies are installed (as per "Setting up the Environment" above).

2. Run the tests from the project root directory:

   ```bash
   pytest test_package_sorting.py
   ```