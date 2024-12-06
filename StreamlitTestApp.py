#!/usr/bin/env python
# coding: utf-8

# In[6]:


from openai import OpenAI
import os
import openai



# In[14]:


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),)

try:
    prompt = "My carbon footprint is 100 kg CO₂ per month. How can I reduce it?"
    response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
        max_tokens=100
    )
    
    print(response.choices[0].message.content)
except Exception as e:
    print("Error with OpenAI API:", e)


# In[ ]:




