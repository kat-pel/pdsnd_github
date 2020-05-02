import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to       handle invalid inputs
    while True:
        valid_cities = ["Chicago", "New York City", "Washington"]
        city = input('Please enter Chicago, New York City or Washington: ').title() 
        if city in valid_cities:
            break
        print('Please try again')
    
    # get user input for month (all, january, february, ... , june)
    while True:
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
        month = input('Please enter a month January, February, March, April, May, June or all: ').title() 
        if month in valid_months:
            break
        print('Please try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
        day = input('Please enter a day of the week Monday, Tuesday.. or all: ').title() 
        if day in valid_days:
            break
        print('Please try again')

    print('-'*50)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Weekday'] = df['Start Time'].dt.day_name()

    if month == "All":
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month_filter = df["Month"].isin(months)
    else:
        month_filter = df['Month'] == month

    if day == "All":
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_filter = df['Weekday'].isin(days)
        
    else:
        day_filter = df['Weekday'] == day

    df = df[day_filter & month_filter]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month is:', common_month)

        # display the most common day of week
    common_day = df['Weekday'].mode()[0]
    print('The most common day is:', common_day)

        # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The most common start hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display number of unique stations
    count_stations = df['Start Station'].nunique()
    print('Number of stations: ', count_stations)

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is:', common_end_station)

    # display most frequent combination of start station and end station trip
    combination = df['Start Station'] + ' ' + '-' + ' ' + df['End Station']
    print('The most common combination of stations is:', combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration_hours = (df['Trip Duration'] / 3600).sum().round(0).astype('int')
    print('The total trip duration in hours is:', total_duration_hours)

    # display mean travel time
    trip_duration_mean = (df['Trip Duration'] / 60).mean().round(0).astype('int')
    print('The mean trip duration in minutes is:', trip_duration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if city == 'Washington':
    # Display counts of user types
        user_types_count = df['User Type'].value_counts()
        print('The count of passenger types:', "\n", user_types_count, "\n") 

    else:
    # Display counts of user types
        user_types_count = df['User Type'].value_counts()
        print('The count of passenger types:', "\n", user_types_count, "\n")
    
    # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('The count of genders:', "\n", gender_count, "\n")
    
    # Display earliest, most recent, and most common year of birth
        min_birth_year = df['Birth Year'].min().round(0).astype('int')
        print('The earliest year of birth is:', min_birth_year)
    
        max_birth_year = df['Birth Year'].max().round(0).astype('int')
        print('The most recent year of birth is:', max_birth_year)
    
        common_birth_year = df['Birth Year'].mode()[0].round(0).astype('int')
        print('The most common year of birth is:', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data = input('\nWould you like to see the raw data?\nEnter yes or no:\n').lower()
        if raw_data == 'yes':
                i = 0
                while True:
                    print(df.iloc[i:i+5])
                    i = i + 5
                    five_more = input('Would you like to see five more rows of raw data? Enter yes or no: ').lower()
                    if five_more == 'no':
                        break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
