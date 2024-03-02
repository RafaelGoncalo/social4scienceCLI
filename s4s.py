import subprocess

# Function to simulate user inputs for the CLI
def simulate_cli_input(inputs):
    process = subprocess.Popen(["python", "your_cli_script.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    for user_input in inputs:
        process.stdin.write(user_input + "\n")
        process.stdin.flush()

    output, _ = process.communicate()
    print(output)

# Simulate user inputs for the CLI
user_inputs = [
    "1",  # Full social analysis
    "YOUR_YOUTUBE_API_KEY",
    "2",  # Collect data of videos
    "1",  # Collect data from a single video
    "https://www.youtube.com/watch?v=VIDEO_ID",
    "0",  # Exit
]

simulate_cli_input(user_inputs)
