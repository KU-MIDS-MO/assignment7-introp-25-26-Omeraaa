def build_pipeline(operation_names):
    valid_ops = ["square", "cube", "double", "triple"]
    for op in operation_names:
        if op not in valid_ops:
            raise KeyError("Invalid Operation")
    def pipeline(input_value):
        for op in operation_names:
            if op == "square":
                input_value = input_value * input_value
            elif op == "cube":
                input_value = input_value * input_value * input_value
            elif op == "double":
                input_value = 2 * input_value
            elif op == "triple":
                input_value = 3 * input_value
            else:
                raise KeyError("Invalid Operation")
        
        return input_value
    return pipeline