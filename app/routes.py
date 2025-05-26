# This script defines the routes for the Flask application.
# It handles requests for different timeframes of Google Trends data
# and renders the appropriate HTML template.

from flask import render_template
from app import app  # Import the Flask app instance
from app.utils import get_trending_keywords # Import the utility function

@app.route('/')
@app.route('/trends/24h')
def trends_24h():
    """
    Route for displaying trending Google searches for the past 24 hours.
    This is also the default route.
    """
    keywords = get_trending_keywords(timeframe_hours=24)
    timeframe_display = "Past 24 Hours"
    return render_template('trends.html', keywords=keywords, timeframe=timeframe_display)

@app.route('/trends/48h')
def trends_48h():
    """
    Route for displaying trending Google searches for the past 48 hours.
    Uses daily trends as a proxy.
    """
    keywords = get_trending_keywords(timeframe_hours=48)
    timeframe_display = "Past 48 Hours (Daily Trends)"
    return render_template('trends.html', keywords=keywords, timeframe=timeframe_display)

@app.route('/trends/7d')
def trends_7d():
    """
    Route for displaying trending Google searches for the past 7 days (168 hours).
    Uses daily trends as a proxy.
    """
    keywords = get_trending_keywords(timeframe_hours=168)
    timeframe_display = "Past 7 Days (Daily Trends)"
    return render_template('trends.html', keywords=keywords, timeframe=timeframe_display)
