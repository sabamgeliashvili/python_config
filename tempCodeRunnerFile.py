def apply_configuration(config_file):
    # Create an empty dictionary to store configuration settings
    config = {}
    
    # Open the configuration file in read mode
    with open(config_file, 'r') as f:
        # Iterate through each line in the configuration file
        for line in f:
            # Split each line into key and value pairs based on '=' delimiter
            key, value = line.strip().split('=')
            # Add key-value pairs to the configuration dictionary after stripping whitespace
            config[key.strip()] = value.strip()

    # Print out the configuration settings
    print("Applying configuration settings:")
    for key, value in config.items():
        print(f"{key}: {value}")

# Test the function with the sample configuration file
apply_configuration('config.txt')