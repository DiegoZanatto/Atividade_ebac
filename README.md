# Project Atividade_EBAC
Simple Data Visualization with Pandas and Seaborn
This project demonstrates a simple process of generating a CSV file, reading it using Pandas, and creating a line plot using Seaborn. The generated line plot is then saved as a PNG image.

# Project Overview
The project involves the following steps:

Data Preparation: The project starts by defining a dataset representing daily gasoline sales. This dataset is then written into a CSV file using the csv module.

Data Loading: The CSV file is loaded into a Pandas DataFrame for further analysis and visualization.

Data Visualization: The Pandas DataFrame is used to create a line plot using Seaborn. The x-axis represents the "day," and the y-axis represents "sales." The resulting plot showcases the trend in gasoline sales over the specified days.

Image Saving: The generated line plot is saved as a high-resolution PNG image using Matplotlib's savefig function.

# How to Use
1) Clone the repository to your local machine using the following command:
  git clone https://github.com/your-username/Atividade_EBAC.git
2) Navigate to the project directory:
   cd Atividade_EBAC
3) Run the script:
   python gasolina.py

After running the script, you will find two new files in the project directory:

gasolina.csv: The CSV file containing the generated data.
gasolina.png: The line plot visualizing the data, saved as a PNG image.

# Requirements
Python 3.x
Pandas
Seaborn
Matplotlib

# Author
Diego Zanatto

# License
This project is licensed under the MIT License - see the LICENSE file for details.
