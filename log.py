def analyze_log_file(log_file):
    with open(log_file, 'r') as f:
        for line in f:
            if 'error' in line.lower():
                print(f"Potential issue found: {line.strip()}")

analyze_log_file('sample_log.txt')
