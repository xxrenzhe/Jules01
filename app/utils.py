from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
import pandas as pd

def get_trending_keywords(timeframe_hours: int) -> list[str]:
    """
    Fetches trending Google search keywords for a given timeframe.

    Args:
        timeframe_hours: The timeframe in hours (e.g., 24 for today, 
                         48 for the last 2 days, 168 for the last 7 days).
                         Note: For 48h and 168h, this function uses daily trends
                         as a proxy due to pytrends API limitations for specific hourly trends.

    Returns:
        A list of trending keyword strings, or an empty list if an error occurs
        or no trends are found.
    """
    try:
        # Initialize Pytrends
        # hl: host language, tz: timezone offset (in minutes), e.g., 360 for US CST
        pytrends = TrendReq(hl='en-US', tz=360)

        keywords_df = pd.DataFrame()

        if timeframe_hours == 24:
            # Fetch today's trending searches for the US
            # Note: today_searches() returns a DataFrame where keywords are typically in column 0
            keywords_df = pytrends.today_searches(pn='US')
        elif timeframe_hours == 48 or timeframe_hours == 168:
            # Fetch daily trending searches for the US
            # This is used as an approximation for 48h and 7-day trends.
            # Note: trending_searches() returns a DataFrame where keywords are typically in column 0
            keywords_df = pytrends.trending_searches(pn='united_states')
        else:
            # Fallback for unsupported timeframes, or could raise an error
            print(f"Unsupported timeframe_hours: {timeframe_hours}. Using daily trends as default.")
            keywords_df = pytrends.trending_searches(pn='united_states')
            
        # Extract keywords from the DataFrame
        # The keywords are usually in the first column (index 0) of the DataFrame.
        # The column name might be 'title' or 0 depending on the pytrends version/method.
        # We will check for 'title' first, then fall back to index 0.
        if not keywords_df.empty:
            if 0 in keywords_df.columns: # today_searches and trending_searches return df with column name 0
                 # Convert all values in the column to string to avoid issues with non-string data
                return keywords_df[0].astype(str).tolist()
            else:
                print("Could not find the expected keyword column in the DataFrame.")
                return []
        else:
            # Return an empty list if the DataFrame is empty (no trends found)
            return []

    except ResponseError as e:
        # Handle API specific errors (e.g., rate limits, connection issues)
        print(f"Pytrends API ResponseError: {e}")
        return []
    except Exception as e:
        # Handle other potential exceptions
        print(f"An unexpected error occurred in get_trending_keywords: {e}")
        return []

if __name__ == '__main__':
    # Example usage for testing
    print("Fetching today's trends (24h):")
    today_keywords = get_trending_keywords(24)
    print(today_keywords)

    print("\nFetching daily trends (approx. 48h):")
    two_day_keywords = get_trending_keywords(48)
    print(two_day_keywords)

    print("\nFetching daily trends (approx. 7d/168h):")
    seven_day_keywords = get_trending_keywords(168)
    print(seven_day_keywords)

    print("\nFetching for an unsupported timeframe (e.g. 12h), will default to daily:")
    unsupported_keywords = get_trending_keywords(12)
    print(unsupported_keywords)
