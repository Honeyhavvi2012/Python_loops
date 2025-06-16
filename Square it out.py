def find_square_values(start, end):
    
    squares = [i**2 for i in range(start, end + 1)]

    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    
    print("All Squares:", squares)
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)


find_square_values(1, 10)
