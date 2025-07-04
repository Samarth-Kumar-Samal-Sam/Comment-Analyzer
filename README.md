# 💬 Comment Analyzer Web Application

### 🚀 **Live Demo**

🔗 [Try the Application Here](https://sam-comment-analyzer.streamlit.app/) — **Instantly analyze the sentiment of your comments with ease!**

---

## 📌 Project Overview

Make sense of textual feedback with this intuitive **Comment Analyzer** app! Powered by advanced NLP techniques and sentiment analysis libraries, the application classifies comments as **Positive**, **Negative**, or **Neutral** to help businesses, researchers, and users understand public opinion effectively.

Built using **Streamlit** for a smooth, interactive user interface, it includes visual sentiment breakdowns and word cloud representations to provide deeper insights into the comment data.

---

## 🛠️ Tech Stack & Tools

| Technology               | Purpose                                 |
| ------------------------ | -------------------------------------- |
| 🐍 Python 3.7+           | Core programming language               |
| 🚀 Streamlit             | Fast, interactive web UI                |
| 📊 Matplotlib & Seaborn  | Visualization of sentiment and word clouds |
| 🐼 Pandas & NumPy        | Data manipulation & numerical computing |
| 🧹 NeatText              | Text cleaning and preprocessing         |
| 📚 NLTK                  | Natural language processing             |
| 🤖 Scikit-learn          | Machine learning for sentiment classification |
| ☁️ WordCloud             | Generate word cloud visuals             |
| 🔍 NRCLex                | Emotion and sentiment lexicon analysis  |
| 🐚 IPykernel             | Kernel management for Jupyter compatibility |

---

## ✨ Key Features

* ✍️ **User Input:** Enter any comment or text for instant sentiment analysis  
* 🔍 **Sentiment Classification:** Categorizes comments into Positive, Negative, or Neutral  
* 🌈 **Visual Sentiment Breakdown:** Pie charts and bar graphs showing sentiment distribution  
* ☁️ **Word Cloud Visualization:** Displays prominent words from input comments for intuitive insight  
* 🧹 **Text Preprocessing:** Removes noise and normalizes input text for accurate predictions  
* ⚡ **Fast and Interactive:** Real-time results with a clean, responsive UI

---

## ⚙️ Setup Instructions (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/Samarth-Kumar-Samal-Sam/Comment-Analyzer.git

cd Comment-Analyzer
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

---
## 📁 Repository Structure

```plaintext
.
│
├── Dataset/                             # Contains the datasets used for training and analysis
│   ├── Refined_Dataset.csv              # Cleaned and processed dataset
│   └── depression-sampled.csv           # Sampled dataset used for training or testing
│
├── Models/                              # Stores saved models and test data
│   ├── Model.pkl                        # Trained machine learning model
│   ├── x_test.pkl                       # Features of the test dataset
│   └── y_test.pkl                       # Labels of the test dataset
│
├── Notebooks/                           # Jupyter notebooks for experimentation and analysis
│   ├── Exploratory Data Analysis.ipynb  # Initial data exploration and visualization
│   ├── Testing Model.ipynb              # Notebook for testing model performance
│   └── Training Model.ipynb             # Notebook used to train the machine learning model
│
├── .gitignore                           # Specifies files/folders to be ignored by Git
├── LICENSE                              # Open source license for the project
├── README.md                            # Project overview and setup instructions
├── app.py                               # Main Python app (likely the backend or web interface)
└── requirements.txt                     # List of Python dependencies required for the project
```

---

## 🚀 Usage Instructions
1. Enter or paste a comment/text in the input box.
2. Click Analyze to classify the sentiment.
3. View the predicted sentiment: Positive, Negative, or Neutral.
4. Explore sentiment visualizations and word cloud for deeper insights.
5. Optionally, upload bulk comments for batch analysis (if implemented).

---
## 👨‍💻 Contributing

Contributions are warmly welcome! Follow these steps:

1. Fork the repository

2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your improvements:

   ```bash
   git commit -m "Add feature description"
   ```

4. Push to your branch:

   ```bash
   git push origin feature-name
   ```

5. Submit a Pull Request 🚀

---

## 📜 License

This project is licensed under the **[MIT License](LICENSE)**.

---

## 👤 Author

**Samarth Kumar Samal**
🔗 [GitHub Profile](https://github.com/Samarth-Kumar-Samal-Sam)

---

## 🙏 Acknowledgements

Thanks to the wonderful open-source tools and libraries that made this project possible:

- [Streamlit](https://docs.streamlit.io/) – For building the interactive web app
- [NeatText](https://pypi.org/project/neattext/) – For simple and quick text cleaning
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/) – For text preprocessing and linguistic data
- [Scikit-learn](https://scikit-learn.org/) – For machine learning algorithms and model building
- [Matplotlib](https://matplotlib.org/) – For static visualizations
- [Seaborn](https://seaborn.pydata.org/) – For statistical data visualization
- [WordCloud](https://amueller.github.io/word_cloud/) – For generating word clouds from text data
- [NRCLex](https://pypi.org/project/nrclex/) – For emotion and sentiment analysis using the NRC lexicon
- [Pandas](https://pandas.pydata.org/) – For data manipulation and analysis
- [NumPy](https://numpy.org/) – For numerical computations
