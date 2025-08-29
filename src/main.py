import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class DataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def analyze_sales_trends(self):
        # Tính toán doanh thu hàng tháng
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        monthly_sales = self.data.resample('M', on='Date').sum()
        return monthly_sales

    def plot_sales(self, monthly_sales):
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=monthly_sales, x=monthly_sales.index, y='Revenue')
        plt.title('Doanh Thu Hàng Tháng')
        plt.xlabel('Tháng')
        plt.ylabel('Doanh Thu')
        plt.show()

    def generate_report(self, monthly_sales):
        c = canvas.Canvas('Sales_Report.pdf', pagesize=letter)
        c.drawString(100, 750, 'Báo Cáo Doanh Thu')
        c.drawString(100, 735, 'Doanh thu hàng tháng:')
        for i, row in enumerate(monthly_sales.iterrows()):
            c.drawString(100, 700 - i * 15, f'{row[0].strftime("%Y-%m")} - {row[1]["Revenue"]}')
        c.save()

if __name__ == '__main__':
    analyzer = DataAnalyzer('data/sales.csv')
    monthly_sales = analyzer.analyze_sales_trends()
    analyzer.plot_sales(monthly_sales)
    analyzer.generate_report(monthly_sales)
