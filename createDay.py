import requests

def fetch_task(day):
    # Replace 'YOUR_SESSION_COOKIE' with your actual session cookie value
    session_cookie = 'YOUR_SESSION_COOKIE'
    
    # Fetch the task description
    task_url = f"https://adventofcode.com/2023/day/{day}"
    task_response = requests.get(task_url, cookies={'session': session_cookie})
    task_html = task_response.text
    
    # Fetch the puzzle input
    input_url = f"https://adventofcode.com/2023/day/{day}/input"
    input_response = requests.get(input_url, cookies={'session': session_cookie})
    puzzle_input = input_response.text
    
    return task_html, puzzle_input

# Replace '12' with the desired day
day = '12'
task_html, puzzle_input = fetch_task(day)

# Print the task description and puzzle input
print("Task Description:")
print(task_html)
print("\nPuzzle Input:")
print(puzzle_input)