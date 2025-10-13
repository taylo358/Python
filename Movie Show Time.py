import csv

def format_movie_table(csv_filename):
    """Reads movie data from a CSV file and outputs a formatted table."""
    try:
        with open(csv_filename, 'r') as file:
            reader = csv.reader(file)
            
            # Initialize variables
            current_title = ""
            current_rating = ""
            showtimes = []
            
            #print(f"{'Title':<44} | {'Rating':>5} | Showtimes")
            #print("-" * 80)
            
            for row in reader:
                if len(row) < 3:
                    continue  # Skip invalid rows
                
                showtime, title, rating = row[0], row[1], row[2]
                
                if title != current_title:
                    # Print the previously accumulated data if it's not the first movie
                    if current_title:
                        print(f"{current_title[:44]:<44} | {current_rating:>5} | {' '.join(showtimes)}")
                    
                    # Reset variables for the new movie
                    current_title = title
                    current_rating = rating
                    showtimes = [showtime]
                else:
                    # Add showtime to the current movie
                    showtimes.append(showtime)
            
            # Print the last movie
            if current_title:
                print(f"{current_title[:44]:<44} | {current_rating:>5} | {' '.join(showtimes)}")
    
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid CSV file.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to execute the program."""
    csv_filename = input()
    format_movie_table(csv_filename)

if __name__ == "__main__":
    main()
