# Carbon Footprint Reduction assistant
## See your carbon footprint and suggestions on how to reduce it using generative AI based on score

This project provides a Python-based application that uses OpenAI's API to suggest actionable ways to reduce your carbon footprint based on a given input. It demonstrates how to leverage the OpenAI GPT models for sustainability-focused solutions.

---

## **Features**

- Accepts user input for monthly carbon footprint (in kg CO₂).
- Generates practical suggestions to reduce carbon emissions.
- Utilizes OpenAI’s GPT model gpt-4o.
- Deployed to production using Streamlit

---

## **Installation**

### **Prerequisites**

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- openai
- streamlit

### **Steps**

1. Clone the repository:

   ```bash
   git clone https://github.com/oifeoluwa-e/Carbon-Footprint-Calc.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:

   - **Option 1**: Use an environment variable:
     ```bash
     export OPENAI_API_KEY="your_openai_api_key"
     ```
   - **Option 2**: Create a `.env` file in the project root:
     ```plaintext
     OPENAI_API_KEY="your_openai_api_key"
     ```

---

## **Usage**

### **Run the Application**

Run the script:

```bash
streamlit run main.py
```
If that does not work you can use:
```bash
python -m streamlit run main.py
```

### **Input Example**

When prompted, provide your monthly carbon footprint (e.g., `100 kg CO₂`). The app will return actionable suggestions to help reduce emissions.

---

## **File Structure**

```
project-root/
├── main.py              # Main script for the application
├── requirements.txt     # Python dependencies
├── .env                 # Optional: Contains the API key (not tracked in Git)
├── README.md            # Project documentation
```

---

## **OpenAI API Details**

The app uses OpenAI’s ChatCompletion endpoint for modern GPT models. Ensure you’re using OpenAI Python SDK version `>=1.0.0`.

Example API call:

```python
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user",
         "content": "My carbon footprint is 100 kg CO₂ per month. How can I reduce it?"}
    ],
    max_tokens=100, #optional
)
```

---

## **Troubleshooting**

### **Common Errors**

#### **1. ****`ModuleNotFoundError: No module named 'openai'`**

- Ensure you installed the `openai` library:
  ```bash
  pip install openai
  ```

#### **2. ****`Error with OpenAI API: 'str' object is not callable`**

- Ensure you're using the correct syntax for OpenAI’s API:
  - For OpenAI `>=1.0.0`, use `openai.chat.completions.create`.
  - Verify your API key and check for name conflicts (e.g., don’t name variables `openai`).

### **Checking Logs**

If deployed (e.g., on Streamlit Cloud), check the deployment logs for detailed error messages.

---

## **Contributing**

Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed explanation of changes.

---

## **Acknowledgments**

- OpenAI for their GPT models and API.
- The sustainability community for inspiring eco-friendly innovation.

