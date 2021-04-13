# highest-profit_Graney_Sub1

Operations to perform

Part 1

1. Print number of rows in matrix as provided
    I will use the pandas library to handle/ explore/ manipulate the matrix of data in data.csv
    A len() function is used to find the number of rows, and the result is printed
2. Delete rows in matrix which have non-numerical entries in index 4
    I will use the .drop method to delete rows where the 'Profit (in millions)' column is the text string 'N.A.' 
    First I'll make an InvalidIndex of rows where the 'Profit (in millions)' column is the text string 'N.A.'
    Then .drop will delete these indexed rows from the dataframe (matrix) 
3. Print number of rows remaining in matrix after operation 2 
    A len() fuction is used to find the number of rows, this time on my dataframe object, and the result is printed
    
Part 2

4. Convert data.csv as modified in Part 1 to JSON format and write as a second file called data2.json
    Profit values are converted to numerical values 
    df.to_json is used to make this conversion, orient set to records format 
5. Sort matrix by descending order of index 4 values
    df.sort_values is used to sort matrix by index 4 values ('Profit (in millions)')
6. Print first 20 rows of matrix as sorted by operation 5
    df.head() function is used and variable dfTOP20 is created and the result is printed

Part 3

7. Review results
8. Think about strategy to perfom this work using SQL 
