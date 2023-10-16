
# Simple_Prompt
This is a basic example to help you deploy an LLM application using the Agenta LLMOps Platform.

## How to Use

### Step 1: Set Up Environment Variables
Create a `.env` file in your project directory and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-api-key-here
```

### Step 2: Install Agenta
If you haven't installed Agenta yet, run the following command:
```
pip install agenta
```

### Step 3: Initialize Your Project
Initialize your Agenta project by running:
```
agenta init
```
Then, answer the prompts that appear.

### Step 4: Serve Your Application
To serve your application, run:
```
agenta variant serve --file_name=app.py
```

