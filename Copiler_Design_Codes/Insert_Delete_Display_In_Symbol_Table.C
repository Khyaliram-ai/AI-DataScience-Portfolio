#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 256
#define FILE_NAME "database.txt"
#define TEMP_FILE "temp.txt"

// Function declarations
void InsertEntry();
void DisplayEntries();
void DeleteEntry();

int main() {
    int choice;

    while (1) {
        printf("\n--- File Management Menu ---\n");
        printf("1. Insert Entry\n");
        printf("2. Display Entries\n");
        printf("3. Delete Entry\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            printf("Invalid input, Exiting\n");
            break;
        }
        
        getchar(); // Clear newline character from buffer

        switch (choice) {
            case 1:
                InsertEntry();
                break;
            case 2:
                DisplayEntries();
                break;
            case 3:
                DeleteEntry();
                break;
            case 4:
                printf("Exiting system. Goodbye!\n");
                return 0;
            default:
                printf("Invalid choice, please try again.\n");
                break;
        }
    }
    return 0;
}

// 1. INSERT: appends a new line entry to the file
void InsertEntry() {
    char entry[MAX_LENGTH];
    FILE *file = fopen(FILE_NAME, "a");

    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }

    printf("Enter the text to insert: ");
    fgets(entry, sizeof(entry), stdin);

    // Write to file
    fputs(entry, file);
    fclose(file);
    printf("Entry inserted successfully\n");
}

// 2. DISPLAY: Reads and prints all entries in the file
void DisplayEntries() {
    FILE *srcfile = fopen(FILE_NAME, "r");
    char line[MAX_LENGTH];
    int currentline = 1;

    if (srcfile == NULL) {
        printf("No entries found or database file does not exist yet.\n");
        return;
    }

    printf("\n--- Current Symbol Table Entries ---\n");
    while (fgets(line, sizeof(line), srcfile) != NULL) {
        printf("%d. %s", currentline, line);
        currentline++;
    }

    fclose(srcfile);
}

// 3. DELETE: Copies files over to temporary file skipping the target line
void DeleteEntry() {
    FILE *srcfile = fopen(FILE_NAME, "r");
    if (srcfile == NULL) {
        printf("Error: Cannot open database file.\n");
        return;
    }

    FILE *tempfile = fopen(TEMP_FILE, "w");
    if (tempfile == NULL) {
        printf("Error creating temporary file\n");
        fclose(srcfile);
        return;
    }

    int targetline;
    int found = 0;
    char line[MAX_LENGTH];
    int currentline = 1;

    // Show entries so the user knows what to delete
    DisplayEntries();

    printf("\nEnter the line number to delete: ");
    if (scanf("%d", &targetline) != 1) {
        printf("Invalid line format.\n");
        fclose(srcfile);
        fclose(tempfile);
        return;
    }
    getchar(); // Clear trailing newline

    // Read through the source and copy over non-matching file lines
    while (fgets(line, sizeof(line), srcfile) != NULL) {
        if (currentline == targetline) {
            found = 1; // skip writing this line
        } else {
            fputs(line, tempfile);
        }
        currentline++;
    }

    fclose(srcfile);
    fclose(tempfile);

    if (found) {
        remove(FILE_NAME);             // Delete original file
        rename(TEMP_FILE, FILE_NAME);   // Rename temp file to original
        printf("Line %d deleted successfully\n", targetline);
    } else {
        remove(TEMP_FILE);             // Clean up temp file
        printf("Line number %d not found\n", targetline);
    }
}
