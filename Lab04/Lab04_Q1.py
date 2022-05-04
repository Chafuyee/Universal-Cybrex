
def is_valid_score(input):
    try:
        value = int(input)
        if (value < 0) or (value > 100):
            return (False, value)
        else:
            return (True, value)
    except (TypeError):
        return (False, "TypeError")
    except (ValueError):
        return (False, "ValueError")


 	

print(is_valid_score('-1'))

