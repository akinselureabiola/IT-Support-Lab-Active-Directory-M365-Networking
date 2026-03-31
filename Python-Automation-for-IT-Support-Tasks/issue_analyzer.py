import csv
from collections import Counter
import matplotlib.pyplot as plt


# Reads IT support issues from a CSV file and returns only the issue names
def read_issues(filename):
    issues = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            issues.append(row["issue"])
    return issues


# Counts how many times each issue appears
def count_issues(issues):
    return Counter(issues)


# Displays the counted issues in ranked order
def display_results(issue_counts):
    print("\nMost Common IT Support Issues:\n")
    for i, (issue, count) in enumerate(issue_counts.most_common(), start=1):
        print(f"{i}. {issue}: {count}")


# Saves the counted issues into a CSV file
def save_results(issue_counts, filename="results.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Issue", "Count"])

        for i, (issue, count) in enumerate(issue_counts.most_common(), start=1):
            writer.writerow([i, issue, count])

    print(f"\nResults saved to {filename}")


# Creates a simple bar chart for the issue counts
def create_chart(issue_counts, filename="issue_chart.png"):
    issues = [issue for issue, count in issue_counts.most_common()]
    counts = [count for issue, count in issue_counts.most_common()]

    plt.figure(figsize=(10, 6))
    plt.bar(issues, counts)
    plt.xlabel("Issue Type")
    plt.ylabel("Count")
    plt.title("Most Common IT Support Issues")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

    print(f"\nChart saved to {filename}")


# Main function
def main():
    issues = read_issues("support_issues.csv")
    issue_counts = count_issues(issues)
    display_results(issue_counts)
    save_results(issue_counts)
    create_chart(issue_counts)


# Runs the script only when executed directly
if __name__ == "__main__":
    main()