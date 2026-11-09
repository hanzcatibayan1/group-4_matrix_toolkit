print("=" * 50)
print("\t" * 4 + "MATRIX TOOLKIT")
print("=" * 50)

# operation choices, user input
try:
    choice = int(
        input(
            "1. Matrix Addition (A + B)\n"
            "2. Matrix Multiplication (A x B)\n"
            "3. Insertion (1D Array)\n"
            "4. Deletion (1D Array)\n"
            "5. Searching (1D Array)\n"
            "6. Updating (1D Array)\n"
            "Choose operation (1-6): "
        )
    )

    if choice == 1:
        print("=" * 50)
        print("\t" * 3 + "Matrix Addition (A + B)")
        print("=" * 50)
        print("MATRIX A:")

        # user input for dimension size (dynamic)
        rows_A = int(input("Enter rows for matrix A: "))
        columns_A = int(input("Enter columns for matrix A: "))

        matrix_A = []  # empty list that will hold the value of matrix A
        print("Enter elements for Matrix A row by row (space-separated):")
        for i in range(1, rows_A + 1):
            # split method to separate value input using space
            # converts an iterable of values (such as a list of strings) into a list of integers.
            row_A = list(map(int, input(f"Row {i}: ").split()))
            if len(row_A) != columns_A:
                raise ValueError(f"Expected {columns_A} elements for row {i}.")
            matrix_A.append(row_A)

        print("MATRIX A:")
        print(*matrix_A, sep="\n")  # separator (new line) for good readability of the output

        print("=" * 50)

        print("MATRIX B:")
        # user input for dimension size (dynamic)
        rows_B = int(input("Enter rows for matrix B: "))
        columns_B = int(input("Enter columns for matrix B: "))

        matrix_B = []  # empty list that will hold the value of matrix B
        print("Enter elements for Matrix B row by row (space-separated):")
        for i in range(1, rows_B + 1):
            # split method to separate value input using space
            row_B = list(map(int, input(f"Row {i}: ").split()))
            if len(row_B) != columns_B:
                raise ValueError(f"Expected {columns_B} elements for row {i}.")
            matrix_B.append(row_B)

        print("MATRIX B:")
        print(*matrix_B, sep="\n")  # separator (new line) for good readability of the output

        print("=" * 50)

        # dimension size validation
        if rows_A != rows_B or columns_A != columns_B:
            print(
                f"Cannot add A ({rows_A} x {columns_A}) and B ({rows_B} x {columns_B}):"
                " addition needs equal dimensions."
            )
        else:
            matrix_C = []  # empty list that will hold the final result of A+B
            for i in range(rows_A):
                row_C = []  # empty list that will hold the result of the process inside inner loop
                for j in range(columns_A):
                    # 2d array addition process
                    row_C.append(matrix_A[i][j] + matrix_B[i][j])
                matrix_C.append(row_C)

            print("\t" * 2 + "Matrix Addition Result (A + B):")
            print("=" * 50)
            print(*matrix_C, sep="\n")

    elif choice == 2:
        print("=" * 50)
        print("\t" * 3 + "Matrix Multiplication (A x B)")
        print("=" * 50)
        print("MATRIX A:")
        rows_A = int(input("Enter rows for matrix A: "))
        columns_A = int(input("Enter columns for matrix A: "))

        matrix_A = []
        print("Enter elements for Matrix A row by row (space-separated):")
        for i in range(1, rows_A + 1):
            row_A = list(map(int, input(f"Row {i}: ").split()))
            if len(row_A) != columns_A:
                raise ValueError(f"Expected {columns_A} elements for row {i}.")
            matrix_A.append(row_A)

        print("MATRIX A:")
        print(*matrix_A, sep="\n")

        print("=" * 50)

        print("MATRIX B:")
        rows_B = int(input("Enter rows for matrix B: "))
        columns_B = int(input("Enter columns for matrix B: "))

        if columns_A != rows_B:
            print(
                "Error: Matrices cannot be multiplied! Columns of A must equal Rows of B."
            )
        else:
            matrix_B = []
            print("Enter elements for Matrix B row by row (space-separated):")
            for i in range(1, rows_B + 1):
                row_B = list(map(int, input(f"Row {i}: ").split()))
                if len(row_B) != columns_B:
                    raise ValueError(f"Expected {columns_B} elements for row {i}.")
                matrix_B.append(row_B)

            print("MATRIX B:")
            print(*matrix_B, sep="\n")

            print("=" * 50)

            matrix_C = []
            for i in range(rows_A):
                row_C = []
                for j in range(columns_B):
                    dot_product = 0
                    for k in range(columns_A):
                        dot_product += matrix_A[i][k] * matrix_B[k][j]
                    row_C.append(dot_product)
                matrix_C.append(row_C)

            print("\t" * 2 + "Matrix Multiplication Result (A x B):")
            print("=" * 50)
            print(*matrix_C, sep="\n")

    elif choice == 3:
        print("=" * 50)
        print("\t" * 4 + "1D Array Insertion")
        print("=" * 50)
        arr = list(
            map(
                int,
                input(
                    "Enter initial 1D array elements separated by spaces: "
                ).split(),
            )
        )
        val = int(input("Enter value to insert: "))
        index = int(input(f"Enter index to insert at (0 to {len(arr)}): "))

        if 0 <= index <= len(arr):
            arr.insert(index, val)
            print("Updated Array After Insertion:", arr)
        else:
            print("Error: Index out of bounds!")

    elif choice == 4:
        print("=" * 50)
        print("\t" * 4 + "1D Array Deletion")
        print("=" * 50)
        arr = list(
            map(
                int,
                input(
                    "Enter initial 1D array elements separated by spaces: "
                ).split(),
            )
        )
        if not arr:
            print("Array is empty.")
        else:
            index = int(input(f"Enter index to delete from (0 to {len(arr) - 1}): "))
            if 0 <= index < len(arr):
                removed = arr.pop(index)
                print(f"Successfully removed element '{removed}' at index {index}.")
                print("Updated Array After Deletion:", arr)
            else:
                print("Error: Index out of bounds!")

    elif choice == 5:
        print("=" * 50)
        print("\t" * 4 + "1D Array Searching")
        print("=" * 50)
        arr = list(
            map(
                int,
                input(
                    "Enter initial 1D array elements separated by spaces: "
                ).split(),
            )
        )
        target = int(input("Enter value to search for: "))
        if target in arr:
            indices = [i for i, x in enumerate(arr) if x == target]
            print(f"Element {target} found at index/indices: {indices}")
        else:
            print(f"Element {target} was not found in the array.")

    elif choice == 6:
        print("=" * 50)
        print("\t" * 4 + "1D Array Updating")
        print("=" * 50)
        arr = list(
            map(
                int,
                input(
                    "Enter initial 1D array elements separated by spaces: "
                ).split(),
            )
        )
        if not arr:
            print("Array is empty.")
        else:
            index = int(input(f"Enter index to update (0 to {len(arr) - 1}): "))
            if 0 <= index < len(arr):
                new_val = int(input(f"Enter new value for index {index}: "))
                old_val = arr[index]
                arr[index] = new_val
                print(f"Successfully updated index {index} from {old_val} to {new_val}.")
                print("Updated Array:", arr)
            else:
                print("Error: Index out of bounds!")

    else:
        print("Invalid choice! Please restart and select an option between 1 and 6.")

except ValueError:
    print("Invalid input. All inputs must be integers only and should match the range!")
