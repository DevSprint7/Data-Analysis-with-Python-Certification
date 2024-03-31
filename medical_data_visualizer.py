import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# Create the overweight column in the df variable
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw the Categorical Plot
def draw_cat_plot():
    # Create a DataFrame for the cat plot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size()).reset_index()
    df_cat.columns = ['cardio', 'variable', 'value', 'total']

    # Draw the catplot
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    fig = g.fig

    # Return the figure
    return fig


# Draw the Heat Map
def draw_heat_map():
    # Clean the data in the df_heat variable
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975)) &
                 (df['ap_lo'] <= df['ap_hi'])]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = (corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool)).abs() < 0.1)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the correlation matrix
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, cmap='coolwarm', square=True, ax=ax)

    # Return the figure
    return fig
