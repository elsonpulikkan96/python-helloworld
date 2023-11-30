import subprocess

def list_top_processes():
    try:
        # Run ps command to get process information, sorting by CPU and memory usage
        ps_output = subprocess.check_output(['ps', 'aux', '--sort=-%cpu,%mem'])

        # Decode and split the output into lines
        ps_lines = ps_output.decode('utf-8').split('\n')

        # Print the header
        print(ps_lines[0])

        # Print the top 10 processes
        for line in ps_lines[1:11]:
            print(line)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_top_processes()

