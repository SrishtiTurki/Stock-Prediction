# Web Scraping Reddit with PRAW

This project allows you to scrape Reddit data using the PRAW (Python Reddit API Wrapper) library. You can fetch top posts, display titles, authors, scores, and other related details.

## Steps to Set Up and Run the Project

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/SrishtiTurki/Stock-Web-Scraping-Prediction/blob/main/RedditWebScraping.py
```

Navigate to the project directory:

```bash
cd RedditWebScraping
```

### Step 2: Set Up Your `.env` File

For security, we store sensitive API credentials in an `.env` file, which is not shared on GitHub. Follow these steps to create and configure your `.env` file:

#### Create a `.env` File in the Root Directory

1. Create a new file named `.env` in the root directory of your project.
2. Add the following environment variables to the `.env` file:

```bash
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

### Step 3: Get Your Reddit API Credentials

To interact with Reddit's API, you'll need to create an app and get your client ID, client secret, and user agent. Follow these steps:

#### Step 3.1: Create a Reddit Account

If you don't already have a Reddit account, [sign up for one](https://www.reddit.com/register).

#### Step 3.2: Access the Reddit Developer Portal

1. Visit the [Reddit Apps](https://www.reddit.com/prefs/apps) page.
2. Scroll down to the **Developed Applications** section.

#### Step 3.3: Create a Reddit Application

1. Click on **Create App** or **Create Another App**.
2. Fill out the application details as follows:
   - **Name**: Choose a name for your app (e.g., `MyRedditBot`).
   - **App Type**: Select **Script** (since this is a personal project).
   - **Redirect URI**: Enter `http://localhost` (this is a required field but won't be used in this case).
   - **Description**: Optional (you can add a description if you like).
3. Click **Create App**.

#### Step 3.4: Copy Your Credentials

After creating your app, you'll see the **client ID** and **client secret** in the app details. Copy these credentials.

Your app credentials should look like this:

```python
reddit = praw.Reddit(
    client_id="abcd1234",  # Your app's client ID
    client_secret="xyz7890",  # Your app's client secret
    user_agent="MyRedditBot/0.1 by MyUsername"  # Your app's user agent
)
```

#### Step 3.5: Add Credentials to `.env`

Paste your credentials into your `.env` file, like so:

```bash
REDDIT_CLIENT_ID=abcd1234
REDDIT_CLIENT_SECRET=xyz7890
REDDIT_USER_AGENT=MyRedditBot/0.1 by MyUsername
```

### Step 4: Install the Required Dependencies

You can install the necessary libraries by using `pip`. It's recommended to create a virtual environment first (optional but preferred):

1. **Create a virtual environment** (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

If you don't have a `requirements.txt` file, you can manually install the required libraries:

```bash
pip install praw python-dotenv
```

### Step 5: Run the Script

Once you've completed the setup, you can run the script to start fetching Reddit posts:

```bash
python reddit_scraper.py
```

The script will fetch top posts from the `/r/stocks` subreddit and display the title, author, score, and URL for each post.

### Step 6: Continue Fetching Posts

The script will ask if you want to fetch the next set of posts:

```bash
Do you want to fetch the next 10 posts? (yes/no): yes
```

### Notes

- The `.env` file will **never** be uploaded to GitHub, ensuring your API credentials are kept private.
- If you plan to deploy this project or share it with others, make sure to add `.env` to your `.gitignore` file to prevent accidental uploads.

### Troubleshooting

- **Missing `.env` file**: Ensure that you've created and populated the `.env` file with your Reddit API credentials.
- **API rate limits**: If you encounter issues with API rate limits, make sure to respect Reddit's API usage policies, or try to limit the number of requests made in a short time.


# Stock Price Prediction Model
This repository contains a machine learning model built to predict stock price volatility using various technical features of the National Stock Exchange of India Ltd (NSE). The model employs a Random Forest Regressor to predict the stock price changes (volatility) based on historical stock data.
## Dependencies

To run this stock prediction model, you'll need to install the following Python libraries:

- **pandas**: For data manipulation and analysis.
- **matplotlib**: For creating visualizations.
- **seaborn**: For enhanced data visualizations.
- **scikit-learn**: For machine learning tasks like data splitting, model building, and evaluation.
- **scipy**: For statistical operations (skewness).
- **numpy**: For numerical computations.

To install all dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
pandas
matplotlib
seaborn
scikit-learn
scipy
numpy
```

## How to Run

1. **Clone the Repository**:
   
   First, clone the repository to your local machine.

   ```bash
   git clone https://github.com/SrishtiTurki/Stock-Web-Scraping-Prediction/blob/main/Predicting_Stocks.ipynb
   cd SPredicting_Stock
   ```

2. **Install Dependencies**:
   
   Make sure all required dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Data**:
   
   The dataset is loaded directly in the script from GitHub. If you prefer to manually download the data, save it as `National_Stock_Exchange_of_India_Ltd.csv` in the project directory.

4. **Run the Script**:
   
   After setting up everything, run the script using:

   ```bash
   python Predicting_Stock.py
   ```

   This will:
   - Load the data
   - Perform data preprocessing
   - Train the Random Forest model
   - Display evaluation metrics such as R² score.

---
