print('\n'.join([ ' / '.join([f"{row} * {col} = {row*col}" for col in range(1, n-row+2)]) for row in range(1, n+1)]) if (n:= int(input())) else None)