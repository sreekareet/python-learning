def analyze_log(filepath):
    #dictionaries to store the counts of operations and results
    op_count = {}
    result_count = {}

    try:
        with open(filepath, "r") as file:
            for line in file: #for each line in the file
                line = line.strip() #remove leading/trailing whitespace
                parts = line.split() #split the line into parts based on whitespace
                operation = parts[2] #get the operation from the line (3rd part)
                result = parts[-1] #last part of the line is accessed using -1 index
                op_count[operation] = op_count.get(operation, 0) + 1 #increment the count for the operation
                result_count[result] = result_count.get(result, 0) + 1 #increment the count for the result
    except FileNotFoundError:
        print(f"log file not found: {filepath}")
        return

    print("=== FastKVS Log Summary ===")

    print(f"Total Operations: {sum(op_count.values())}")
    print("Operation Counts:")
    for op, count in op_count.items():
        print(f"{op}: {count}")

    print("Result Counts:")
    for res, count in result_count.items():
        print(f"{res}: {count}")

analyze_log("server.log")