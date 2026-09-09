"""
Week 7 Assignment: Machine Learning with Scikit-Learn
Author: Sean Coggeshall

Implements two ML pipelines: (1) balanced multi-class sentiment analysis
on product reviews using bag-of-words vectorization and logistic regression,
and (2) stock trend prediction combining technical indicators (RSI, momentum,
volatility) with S&P 500 index features via logistic regression.
"""
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader.data as pdr
from datetime import date, timedelta
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

# -------------------------
# Exercise 19: Expanding the Example Set
# -------------------------
def run_exercise19(csv_path='Reviews.csv', target_per_class=500):
    print("\n" + "="*10 + " Exercise 19: Balanced Sentiment Analysis " + "="*10 + "\n")
    # 1. Load & normalize
    df = pd.read_csv(csv_path)
    df = df.rename(columns={'Score':'rating', 'Summary':'title'})
    df = df[['title','rating']].dropna()
    df = df[df['rating'].isin([1,2,3,4,5])]

    # 2. Balance to `target_per_class` samples per rating
    balanced = pd.concat([
        grp.sample(n=target_per_class, replace=(len(grp)<target_per_class), random_state=42)
        for _, grp in df.groupby('rating')
    ], ignore_index=True)

    # 3. Split (80/20 stratified)
    X = balanced['title'].values
    y = balanced['rating'].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # 4. Vectorize
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec  = vectorizer.transform(X_test)

    # 5. Train
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_vec, y_train)

    # 6. Evaluate
    y_pred = clf.predict(X_test_vec)
    accuracy = np.mean(y_pred == y_test)

    print(f"Balanced set size: {len(balanced)} (≈{target_per_class} per class)")
    print(f"Train/Test split: {len(y_train)}/{len(y_test)}")
    print(f"Accuracy: {accuracy:.2f}\n")

    print("Classification Report:")
    print(metrics.classification_report(
        y_test, y_pred, labels=[1,2,3,4,5], zero_division=0
    ))

    print("Confusion Matrix:")
    print(metrics.confusion_matrix(
        y_test, y_pred, labels=[1,2,3,4,5]
    ))
    print("\n" + "="*50 + "\n")


# -------------------------
# Exercise 20: Stock Trend Prediction
# -------------------------
def calculate_rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean().replace(0, 1e-9)
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def run_exercise20(ticker: str = "AAPL"):
    print("\n" + "="*10 + f" Exercise 20: Stock Trend Prediction ({ticker}) " + "="*10 + "\n")
    # 1) Fetch data
    end   = date.today()
    start = end - timedelta(days=365)
    stock = yf.Ticker(ticker).history(period="1y")
    stock.index = stock.index.tz_localize(None)
    idx   = pdr.get_data_stooq("^SPX", start, end)
    idx.index   = idx.index.tz_localize(None)

    df = stock.join(idx, rsuffix="_idx")
    df = df[['Close','High','Low','Volume','Close_idx','Volume_idx']].copy()

    # 2) Features
    df['priceRise']     = np.log(df['Close']       / df['Close'].shift(1))
    df['volumeRise']    = np.log(df['Volume']      / df['Volume'].shift(1))
    df['priceRise_idx'] = np.log(df['Close_idx']   / df['Close_idx'].shift(1))
    df['volumeRise_idx']= np.log(df['Volume_idx']  / df['Volume_idx'].shift(1))
    df['volatility']    = (df['High'] - df['Low']) / df['Close']
    df['momentum5']     = df['Close'].pct_change(periods=5)
    df['rsi14']         = calculate_rsi(df['Close'], window=14)

    df = df.dropna()

    # 3) Target
    future = df['priceRise'].shift(-1)
    conds   = [future > 0.01, future < -0.01]
    choices = [1, -1]
    df['Target'] = np.select(conds, choices, default=0)
    df = df.dropna()

    # 4) Arrays
    feature_cols = ['priceRise','volumeRise','priceRise_idx',
                    'volumeRise_idx','volatility','momentum5','rsi14']
    X = df[feature_cols].values
    y = df['Target'].values

    # 5) Split & train
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    clf = LogisticRegression(class_weight='balanced', max_iter=1000)
    clf.fit(Xtr, ytr)

    # 6) Eval
    acc  = clf.score(Xte, yte)
    ypred = clf.predict(Xte)

    print(f"Accuracy: {acc:.2%}\n")
    print("Confusion Matrix:")
    print(confusion_matrix(yte, ypred), "\n")
    print("Classification Report:")
    print(classification_report(yte, ypred, target_names=['Flat','Up','Down']))
    print("\nSample Predictions (Actual → Predicted):")
    for actual, pred in list(zip(yte, ypred))[:10]:
        print(f"   {actual} → {pred}")
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    # Run both exercises back‐to‐back
    run_exercise19()
    run_exercise20("AAPL")
