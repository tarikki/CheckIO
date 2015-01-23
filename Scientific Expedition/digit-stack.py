def digit_stack(commands):
    numbers = []                                    # Array for numbers
    summing_up = 0                                  # A returnable sum
    for command in commands:                        # Iterate over commands
        instructions = command.split(" ")           # Split on Space
        if len(instructions) == 2:                  # Must be a PUSH + digit
            numbers.append(instructions[1])         # Store the number
        else:
            if len(numbers) > 0:                    # If numbers array has members
                if instructions[0] == "POP":        # On POP
                    summing_up += int(numbers[-1])  # Add the number to the sum
                    del numbers[-1]                 # Remove it from the array
                if instructions[0] == "PEEK":       # On Peek
                    summing_up += int(numbers[-1])  # Just add it to the sum

    return summing_up

