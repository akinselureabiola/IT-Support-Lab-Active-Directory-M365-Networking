# Python Automation for IT Support Tasks

## Overview

I built this project to simulate a simple IT support task using Python.

In IT support, many user issues tend to repeat over time. Problems like VPN connection failures, password resets, login issues, and mailbox access requests often come up again and again. I wanted to create a small script that could help analyze those recurring issues instead of reviewing them manually one by one.

This project reads IT support issue data from a CSV file, counts how often each issue appears, saves the results into a separate CSV file, and also generates a simple bar chart to make the findings easier to understand.

---

## Why I Built This

While working in IT support and also practicing in my labs, I noticed that the same kinds of incidents appear repeatedly. That made me think about how small automation can help make support work more efficient.

The goal of this project was to build something simple and practical that could:

- show the most common support issues
- help identify recurring patterns
- simulate a basic reporting process
- connect Python with a real IT support use case

I wanted this project to stay simple enough to understand clearly, but still feel close to something that could be useful in a real support environment.

---

## What the Project Does

The script performs four main tasks:

1. Reads issue data from a CSV file (`support_issues.csv`)
2. Extracts and counts how many times each issue appears
3. Displays the results in ranked order in the terminal
4. Saves the ranked results into a CSV file (`results.csv`)
5. Generates a bar chart (`issue_chart.png`) to visualize the most common support issues

---

## Dataset Used

The input file for this project is `support_issues.csv`.

It contains simulated IT support issue records with two fields:

- `timestamp`
- `issue`

I used a structured CSV format instead of a plain text file so the project would feel more realistic and closer to how support data might be stored or exported in a real environment.

Example:

```csv
timestamp,issue
2026-03-31 08:15,Login issue
2026-03-31 08:22,Password reset
2026-03-31 08:35,Outlook not opening
````

---

## Sample Output

When the script runs, it displays the ranked issue counts in the terminal and saves the same results into `results.csv`.

Example output:

```text
1. VPN not connecting: 29
2. MFA setup issue: 26
3. Login issue: 25
4. Password reset: 22
5. Outlook not opening: 17
6. Wi-Fi issue: 17
7. Shared mailbox access: 14
```

---

## Visualization

To make the results easier to understand, I added a simple bar chart that shows the most common IT support issues.

This helped turn the project from just a counting script into something closer to a small reporting tool. It also makes it easier to quickly see which problems occur most often.

The chart is automatically generated and saved as:

* `issue_chart.png`

---

## Files in This Project

```text
Python-Automation-for-IT-Support-Tasks/
│
├── issue_analyzer.py
├── support_issues.csv
├── results.csv
├── issue_chart.png
└── README.md
```

---

## Technologies Used

* Python
* `csv`
* `collections.Counter`
* `matplotlib`

---

## What I Learned

While building this project, I improved my understanding of:

* reading structured data from CSV files
* using `Counter` to analyze repeated issues
* organizing Python code into small functions
* saving processed results into a new file
* visualizing issue trends using a chart
* thinking about how automation can support everyday IT tasks

More importantly, this project helped me apply Python in a way that connects directly to IT support instead of just practicing syntax.

---

## How to Run the Project

1. Make sure Python is installed
2. Make sure the required files are in the same folder
3. Install matplotlib if needed:

```bash
pip install matplotlib
```

4. Run the script:

```bash
python3 issue_analyzer.py
```

---

## Expected Results

After running the script, you should get:

* ranked issue counts shown in the terminal
* a `results.csv` file with the summarized output
* an `issue_chart.png` file showing the issue frequency visually

---

## Future Improvements

If I continue improving this project, I would like to:

* analyze issue trends by date
* filter results by time period
* create multiple charts for better reporting
* connect the script to real exported ticket data
* extend it to support more issue categories

---

## Final Note

This project is part of my hands-on learning in IT support, automation, and troubleshooting.

My goal with it was not to build something overly complex, but to create a practical script that reflects the kind of repeated issue analysis that can happen in real support environments. It was also a good way for me to combine Python with a support-focused problem in a simple and useful way.
