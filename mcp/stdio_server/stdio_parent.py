import subprocess

result = subprocess.run(
    ['python', 'stdio_child.py'],
    input="Zoltan", # writes to the child stdin
    capture_output=True,
    text=True
)
print("The child process returned:", result.stdout) # reads from the child stdout
