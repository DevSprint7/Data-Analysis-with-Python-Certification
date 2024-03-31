import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df_clean = df[(df['value'] >= df['value'].quantile(0.025)) &
              (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Create a line plot
    plt.figure(figsize=(10, 5))
    plt.plot(df_clean.index, df_clean['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    return plt.gca()


def draw_bar_plot():
    # Create a new column for the year and month
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.strftime('%B')

    # Create a pivot table
    df_pivot = df_clean.pivot_table(index='year', columns='month', values='value', aggfunc='mean')

    # Create a bar plot
    ax = df_pivot.plot(kind='bar', figsize=(12, 6))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    return ax


def draw_box_plot():
    # Prepare data for box plots
    df_clean.reset_index(inplace=True)
    df_clean['year'] = [d.year for d in df_clean['date']]
    df_clean['month'] = [d.strftime('%b') for d in df_clean['date']]

    # Create the box plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x='year', y='value', data=df_clean, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_clean, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return fig


# Example usage:
draw_line_plot()
draw_bar_plot()
draw_box_plot()
plt.show()
