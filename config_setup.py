def apply_configuration(config_file):
    config = {}
    
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()

    print("Applying configuration settings:")
    for key, value in config.items():
        print(f"{key}: {value}")

apply_configuration('config.txt')
