
# Movie Recommendation System

This project involves developing a movie recommendation system using IMDb datasets. The system utilizes data cleansing, vectorization algorithms, and a user-friendly interface to provide accurate movie recommendations.


## Overview

The Movie Recommendation System is designed to suggest movies to users based on their preferences. By leveraging data from IMDb, the system cleanses and processes the data, applies machine learning algorithms for vectorization, and provides an interactive UI for user interaction.

## Features

- **Data Cleansing**: Ensures data quality and consistency by cleaning two IMDb datasets with 5,000 entries using NumPy, Pandas, and Python.
- **Vectorization Algorithm**: Utilizes Scikit-learn to optimize movie recommendation accuracy.
- **User Interface**: Built with Streamlit, allowing users to interact with the recommendation system easily.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   
2. **Set up a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the Movie Recommendation System, execute the following command in your terminal:

```sh
streamlit run app.py
```

This will start the Streamlit server, and you can interact with the recommendation system through your web browser.

---
