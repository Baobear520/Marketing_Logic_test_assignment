import csv
from pathlib import Path
import numpy as np
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Constants
OUTPUT_FOLDER = "data"
BASE_DIR = Path(__file__).parent
MATRIX_SIZE = 300

def get_file_path(file_name):
    """Returns the full path to the file in the 'data' directory."""
    
    return os.path.join(BASE_DIR, OUTPUT_FOLDER, file_name)

def create_matrix():
    """Creates an empty matrix of fixed size."""
    
    matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=np.int32)
    logging.info(f"Matrix of size {MATRIX_SIZE}x{MATRIX_SIZE} created.")
    return matrix

def data_parsing(matrix, file_name):
    """Parses data from the CSV file and fills the matrix."""
    
    path_to_file = get_file_path(file_name)
    
    
    # Check if the file exists
    if not os.path.exists(path_to_file):
        logging.error(f"File {path_to_file} does not exist.")
        return None

    try:
        with open(path_to_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                cell = row[0]
                id_value, cell_value = map(int, cell.split('|'))
                
                # Calculate row and column indices
                row_index = (id_value - 1) // MATRIX_SIZE
                col_index = (id_value - 1) % MATRIX_SIZE
                
                matrix[row_index, col_index] = cell_value
        logging.info(f"Data successfully parsed from {file_name}.")
        return matrix
    except Exception as e:
        logging.error(f"Error while parsing data: {e}")
        return None

def writing_data(data, file_name):
    """Writes matrix data to a CSV file."""
    
    path_to_file = get_file_path(file_name)
    
    try:
        with open(path_to_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        logging.info(f"Matrix successfully saved to {file_name}.")
    except Exception as e:
        logging.error(f"Error writing data to file {file_name}: {e}")

def main():
    """Main function."""
    
    matrix = create_matrix()
    data = data_parsing(matrix, 'source__300.csv')
    
    if data is not None:
        writing_data(data, 'output.csv')
    

if __name__ == "__main__":
    main()
