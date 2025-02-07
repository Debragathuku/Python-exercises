def main():
    # Prompt user for input
    names = input("Enter a list of names separated by commas: ").split(',')
    
    # Remove whitespace and convert to a set to remove duplicates
    unique_names = sorted(set(name.strip() for name in names))
    
    # Display the sorted unique list
    print("\nSorted list of unique names:")
    for name in unique_names:
        print(name)
    
    # Print the total count of names entered
    print("\nTotal number of names entered:", len(names))

if __name__ == "__main__":
    main()
