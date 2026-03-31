from collections import Counter


# Reads IT support issues from a text file and returns them as a cleaned list
def read_issues(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


# Counts how many times each issue appears using Counter
def count_issues(issues):
    return Counter(issues)


# Displays the counted issues in order of most frequent to least frequent
def display_results(issue_counts):
    print("\nMost Common IT Support Issues:\n")
    
    for i, (issue, count) in enumerate(issue_counts.most_common(), start=1):
        print(f"{i}. {issue}: {count}")


# Saves the counted issues into a text file for reporting or later use
def save_results(issue_counts, filename="results.txt"):
    with open(filename, "w") as file:
        for issue, count in issue_counts.most_common():
            file.write(f"{issue}: {count}\n")
    print(f"\nResults saved to {filename}")


# Controls the overall flow: reads data, processes it, displays results, and saves output
def main():
    issues = read_issues("support_issues.txt")
    issue_counts = count_issues(issues)
    display_results(issue_counts)
    save_results(issue_counts)


# Ensures the script runs only when executed directly (not when imported)
if __name__ == "__main__":
    main()