import re
import csv


input_file = "minecraftlogs.txt"
output_csv = "serverconnections.csv"

# Regex for the lines we are parsing out - thanks ChatGPT
patterns = {
    "Connected": r"^\[(.*?)INFO\].*Player connected: ([^,]+),",
    "Disconnected": r"^\[(.*?)INFO\].*Player disconnected: ([^,]+),"
}

with open(input_file, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(["Time", "Action", "Username"])
    
    for line in infile:
        for action, pattern in patterns.items():
            match = re.match(pattern, line)
            if match:
                datetime = match.group(1)[:-5] #this little number at the end "[:-5]" is to get rid of the milliseconds that prevent numbers from processing the datetime as a date/time. If I were better at regex I would have pulled them out in the pattern expressions.
                username = match.group(2)
                
                writer.writerow([datetime, action, username])

                break

print(f"Parsing complete. Results saved to {output_csv}")
