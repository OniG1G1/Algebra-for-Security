from arithmetic.extended import extendedEuclidean

class ExtendedEuclidean:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for the Extended Euclidean Algorithm. Handles a, b flipping.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])

        sign_x = '-' if x.startswith('-') else '+'
        sign_y = '-' if y.startswith('-') else '+'

        # Remove signs for raw digit handling
        x_val = x[1:] if sign_x == '-' else x
        y_val = y[1:] if sign_y == '-' else y
    
        a, b, d = extendedEuclidean(x_val, y_val, radix)

        #a = "-" + a if sign_x == "-" else a
        #b = "-" + b if sign_x == "-" else a
        if sign_x == '-' and a != "0":
            if not a.startswith("-"):
                a = "-" + a
            else:
                a = a[1:]
        if sign_y == '-' and b != "0":
            if not b.startswith("-"):
                b = "-" + b
            else:
                b = b[1:]

        return {
            "answer-a": a,
            "answer-b": b,
            "answer-gcd": d
        }
    