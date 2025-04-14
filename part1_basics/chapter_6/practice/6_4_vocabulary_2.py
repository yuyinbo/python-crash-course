vocabulary = {
    "Variable": "A variable is a named storage location in memory that holds "
                "a value which can change during program execution.",
    "Function": "A function is a reusable block of code that performs "
                "a specific task. It can accept inputs (parameters) "
                "and return an output (return value).",
    "Loop": "A loop is a control structure that repeats a block of code "
            "multiple times, either a fixed number of times (for loop) "
            "or while a condition is true (while loop).",
    "List": "A list is an ordered collection of items in Python, enclosed "
            "in square brackets. Lists can contain elements of "
            "different types and support indexing.",
    "Condition": "A condition is a logical statement that evaluates "
                 "to True or False, used to control the flow of "
                 "the program, typically with if, elif, and else."
}

for term, meaning in vocabulary.items():
    print(term + ": " + meaning)
