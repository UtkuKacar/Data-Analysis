![76da282fad5a3e279c6b163688f5345b](https://github.com/user-attachments/assets/b3c91748-88ff-4320-b63d-d98caa983bf7)

# Data-Analysis

🎯 This project analyzes force data from the 004F SPRING assembly process to support data-driven decision making, improve quality control, and detect potential production issues early.

📝 Project Overview
The project performs the following main tasks:

Data Extraction:


Reads a CSV file containing raw text data.

Uses regular expressions to parse each row into structured fields (date, time, code, result, product, force1, force2).

Data Cleaning:


Converts force values from string format (with commas as decimal separators) to numeric.

Filters out invalid values (e.g., negative forces).

Standardizes text in the result column and renames force columns to FORCE_POS_1 and FORCE_POS_2.

The cleaned data is saved as cleaned_data.csv.

Exploratory Data Analysis (EDA):


Calculates basic statistics for the force columns.

Generates histograms to visualize the distribution of force values.

Saves the EDA charts as a high-quality JPG file.

Anomaly Detection:


Computes z-scores for the FORCE_POS_1 values.

Identifies records with extreme deviations.

Saves the anomaly records in a separate CSV file.

Performance Analysis:


Filters the data to include only records with "OK" results.

Computes average and variability (standard deviation) for the force values.

Evaluates process performance using a process capability index (CP) for FORCE_POS_1.

Detailed Reporting:


Groups the data by date to report daily production counts.

Breaks down daily OK/NOK distribution.

Extracts detailed records for NOK instances (including date, time, code, and force values) and saves them to a CSV file.

Generates a bar chart for the OK/NOK distribution and saves it as a JPG file.

Analysis Output Capture:


Captures all console output from the analysis and saves it to a text file.

🛠️ Repository Files
csv_extraction.py: Parses raw CSV data into a structured DataFrame.

data_cleaning.py: Cleans and standardizes the data.

eda_analysis.py: Performs exploratory analysis and creates histograms.

anomaly_detection.py: Identifies anomalies in the force data.

performance_analysis.py: Evaluates performance using the OK records.

reporting.py: Generates a bar chart showing OK/NOK distribution.

main.py: Integrates all modules and runs the complete analysis workflow, saving outputs to text and image files.

📦 Dependencies
Python 3.x

Pandas

NumPy

Matplotlib

Install the dependencies with:

pip install pandas numpy matplotlib

▶️ How to Run
Place the cleaned_data.csv file in the project directory.

Run the main analysis pipeline by executing:

python main.py
This will perform the entire analysis, generate charts, and save the outputs to files such as eda_summary.jpg, anomalies_pos1.csv, nok_records.csv, and analysis_results.txt.

📜License
This project is open source and available under the MIT License.
