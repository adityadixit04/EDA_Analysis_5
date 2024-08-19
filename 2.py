import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Label, Button, filedialog, messagebox

class TrafficAccidentAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Accident Data Analyzer")
        self.df = None
        
        # GUI elements
        self.label = Label(root, text="Traffic Accident Data Analyzer", font=("Arial", 16))
        self.label.pack(pady=20)

        self.load_button = Button(root, text="Load Dataset", command=self.load_data)
        self.load_button.pack(pady=10)

        self.analyze_button = Button(root, text="Analyze Data", command=self.analyze_data, state='disabled')
        self.analyze_button.pack(pady=10)

        self.quit_button = Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Dataset loaded successfully!")
                self.analyze_button.config(state='normal')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset:\n{e}")

    def analyze_data(self):
        if self.df is not None:
            self.df = self.df.dropna()

            # Convert and extract necessary features
            self.df['date'] = pd.to_datetime(self.df['date'])
            self.df['hour'] = self.df['time'].apply(lambda x: int(x.split(':')[0]))
            self.df['month'] = self.df['date'].dt.month
            self.df['day_of_week'] = self.df['date'].dt.dayofweek

            # Visualize distribution of accidents by hour
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df['hour'], bins=24, kde=False)
            plt.title('Distribution of Accidents by Hour')
            plt.xlabel('Hour of the Day')
            plt.ylabel('Number of Accidents')
            plt.show()

            # Visualize accidents by weather condition
            plt.figure(figsize=(10, 6))
            sns.countplot(data=self.df, x='weather_condition')
            plt.title('Accidents by Weather Condition')
            plt.xlabel('Weather Condition')
            plt.ylabel('Number of Accidents')
            plt.xticks(rotation=45)
            plt.show()

            # Visualize accidents by road condition
            plt.figure(figsize=(10, 6))
            sns.countplot(data=self.df, x='road_condition')
            plt.title('Accidents by Road Condition')
            plt.xlabel('Road Condition')
            plt.ylabel('Number of Accidents')
            plt.xticks(rotation=45)
            plt.show()

            # Accident hotspots visualization
            plt.figure(figsize=(10, 10))
            sns.scatterplot(x='longitude', y='latitude', data=self.df, hue='severity', palette='Reds', alpha=0.5)
            plt.title('Accident Hotspots')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.show()

            # Correlation matrix
            correlation = self.df.corr()
            plt.figure(figsize=(12, 8))
            sns.heatmap(correlation, annot=True, cmap='coolwarm')
            plt.title('Correlation Matrix of Factors Contributing to Accidents')
            plt.show()
        else:
            messagebox.showerror("Error", "No dataset loaded!")

if __name__ == "__main__":
    root = Tk()
    app = TrafficAccidentAnalyzer(root)
    root.mainloop()
