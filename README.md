A lightweight Python automation project that parses system/application logs, extracts timestamps, converts them into datetime objects, and performs safe date-time manipulations such as adding years with leap-year handling.

🚀 Why This Project?

Logs are everywhere — debugging, monitoring, automation, and testing all depend on them.
This project demonstrates how to:

Programmatically filter logs by keyword

Extract timestamps with millisecond precision

Convert raw strings into Python datetime objects

Perform safe date-time arithmetic (even across leap years)

Build a clean, step-by-step processing pipeline

Perfect for automation engineers, QA, backend developers, and learners.

🧩 How It Works (Pipeline)
Log File
   ↓
Keyword Filtering
   ↓
Timestamp Extraction
   ↓
Datetime Conversion
   ↓
Date-Time Transformation


Each step is handled by a dedicated function to keep the logic modular and easy to debug.

🛠️ Features

🔍 Keyword-based log filtering

🕒 Millisecond-level timestamp extraction

📅 Robust datetime parsing

🔁 Add years safely (handles Feb 29 edge cases)

🧪 Clear console output for each processing stage

▶️ Usage

Place your log file in the project directory

Update the query string in main()

Run the script:

python main.py


The script prints:

Matched log lines

Extracted timestamps

Converted datetime objects

Updated datetimes after transformation

📂 Ideal Use Cases

Log analysis & debugging

Automation scripting

QA validation workflows

Learning Python datetime handling

🌱 Future Enhancements

Support for multiple log formats

Timezone handling

Export results to CSV/JSON

CLI arguments for flexibility
