# SQL CHATBOT

Ever wished you could just *talk* to your database? Now you can!

This little app lets you ask questions about your data in plain English. No more trying to remember complicated SQL commands. Just ask, "How many students are there?" and it'll find the answer for you.

It's all powered by a **LangChain SQL Agent** and the speedy **Groq API**. It's smart enough to figure out your question, write the SQL "nerd stuff" for you, and give you back a simple, human-readable answer.

## What's Cool About It?

* **Talk like a person:** Ask questions naturally. "Who has the highest grade?" is way easier than `SELECT name, MAX(grade) FROM students;`.
* **See the AI's "brain":** You can watch in real-time as the agent thinks, writes its SQL query, and gets the answer. It's pretty cool!
* **Use our DB or yours:** It comes with a `student.db` file so you can try it immediately. Or, you can easily hook it up to your own **MySQL** database.
* **Warp-speed answers:** Thanks to Groq, you won't be waiting around.
* **It remembers!** You can ask follow-up questions because it keeps track of your conversation.

---

## How to Get it Running

Ready to try it? It's just a few quick steps.

1.  **Get the Code**
    Grab the code from GitHub (or wherever you have it).
    ```bash
    git clone [https://your-repository-url.git](https://your-repository-url.git)
    cd your-repository-directory
    ```

2.  **Install the Parts**
    This will install all the libraries the app needs.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Add the Test Database**
    The app looks for a file named `student.db` to play with. Make sure you have it in the same folder as the app.

4.  **Add Your API Key**
    Create a file named `.env` in the same folder. Inside it, put your Groq API key:
    ```
    GROQ_API_KEY="gsk_YOUR_REAL_GROQ_KEY"
    ```

5.  **Launch it!**
    This is the fun part.
    ```bash
    streamlit run app.py
    ```
    *(If your file isn't named `app.py`, use that name instead!)*

---

## How to Use It

Okay, the app should be open in your browser. Here's what to do:

1.  Pop open the **sidebar** on the left.
2.  Paste your **Groq API Key** into the box.
3.  **Pick your database:**
    * Want to start easy? Just pick "**Use SQLlite 3 database- student.db**".
    * Want to use your own? Select "**connect to your sql database**" and just fill in your details.
4.  That's it! **Start chatting.** Ask it anything about your data.
    * "How many students are in the 'Physics' department?"
    * "What's the average grade for everyone?"
    * "Find anyone named 'John'."