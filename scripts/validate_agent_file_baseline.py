import os
import sys

# Define the path to your baseline files and agent contract files
baseline_directory = 'path/to/baselines'
agent_directory = 'path/to/agent_contracts'

# Function to validate agent contract files against baselines

def validate_agent_files():
    try:
        # List all baseline files
        baselines = os.listdir(baseline_directory)
        # List all agent contract files
        agent_files = os.listdir(agent_directory)

        # Validate each agent file against the corresponding baseline
        for agent in agent_files:
            # Check if an equivalent baseline exists
            baseline_file = agent.replace('.contract', '.baseline')
            if baseline_file in baselines:
                with open(os.path.join(baseline_directory, baseline_file), 'r') as baseline:
                    with open(os.path.join(agent_directory, agent), 'r') as agent_file:
                        # Compare content
                        if baseline.read() != agent_file.read():
                            print(f'Validation failed for {agent}')
                            sys.exit(1)  # Validation fails
            else:
                print(f'Baseline for {agent} not found.')
                sys.exit(1)  # Validation fails

        print('All agent files validated successfully.')
        sys.exit(0)  # All files match

    except Exception as e:
        print(f'Script error: {e}')
        sys.exit(2)  # Error during validation

if __name__ == '__main__':
    validate_agent_files()