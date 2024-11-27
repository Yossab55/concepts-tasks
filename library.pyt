def library_book_borrowing_analysis():
    print("Enter the borrowed books in the format 'Book Title - Days Borrowed' (one per line).")
    print("Type 'done' when you finish entering the data.")
    
    book_records = {}
    
    while True:
        record = input("Enter record: ")
        if record.lower() == "done":
            break
        
        try:
            title, days = record.rsplit(" - ", 1)
            days = int(days)
            if title in book_records:
                book_records[title] += days
            else:
                book_records[title] = days
        except ValueError:
            print("Invalid format. Please enter in 'Book Title - Days Borrowed' format.")
            continue
    
    unique_titles = set(book_records.keys())
    
    most_borrowed = max(book_records.items(), key=lambda x: x[1])
    least_borrowed = min(book_records.items(), key=lambda x: x[1])
    
    total_days = sum(book_records.values())
    average_days = total_days / len(book_records)
    
    sorted_books = sorted(book_records.items(), key=lambda x: x[1], reverse=True)
    
    print("\nResults:")
    print(f"Most Borrowed Book: '{most_borrowed[0]}' with {most_borrowed[1]} days")
    print(f"Least Borrowed Book: '{least_borrowed[0]}' with {least_borrowed[1]} days")
    print(f"Average Borrowing Time: {average_days:.2f} days")
    print(f"Unique Titles of Books Borrowed: {unique_titles}")
    print("Books Sorted by Borrowing Duration (Descending):")
    for title, days in sorted_books:
        print(f"'{title}' - {days} days")

library_book_borrowing_analysis()
