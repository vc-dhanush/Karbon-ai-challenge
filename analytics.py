import pandas as pd
import matplotlib.pyplot as plt

def generate_charts(df, bank_name):
    # Expenses Pie Chart
    expenses = df[df['Debit'] > 0].groupby('Category')['Debit'].sum()
    plt.figure(figsize=(6,6))
    expenses.plot.pie(autopct='%1.1f%%', title='Expenses by Category')
    plt.savefig(f'{bank_name}_expenses_chart.png')
    plt.close()

    # Credit vs Debit Trend
    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.groupby(df['Date'].dt.to_period('M')).sum()
    plt.figure(figsize=(8,5))
    monthly[['Credit','Debit']].plot(title='Monthly Credit vs Debit')
    plt.savefig(f'{bank_name}_monthly_trend.png')
    plt.close()
