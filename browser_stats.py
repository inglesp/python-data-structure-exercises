# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py

from browser_stats_data import browser_stats_by_year_and_month

print('browser_stats_by_year_and_month is a {} with {} elements'.format(type(browser_stats_by_year_and_month).__name__, len(browser_stats_by_year_and_month)))


# TODO:
# * Display a report that answers the following questions:
#   * What period does the report cover?
#   * In the period covered, which browsers have had over 50% of market share?
#   * In which month did Firefox first become the most popular browser?
#   * In which month did Chrome first overtake IE in popularity?
#   * In which month was Firefox's popularity highest?
#   * In which month was the combined popularity of Safari and Opera highest?
#   * Which month saw the biggest percentage point rise in Chrome's popularity?
#   * Which month saw the biggest percentage point 
