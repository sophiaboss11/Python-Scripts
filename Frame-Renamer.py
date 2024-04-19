import os
import shutil

def update_frame_numbers(directory):
    frameNumbers = []
    files_to_rename = []

    # Step 1, 2, 3: Check file extension and process file names
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            try:
                # Extract last four characters and convert to integer
                last_four_digits = int(filename[-8:-4])
                frameNumbers.append(last_four_digits)
                files_to_rename.append(filename)
            except ValueError:
                print(f"Skipping file {filename}: Last four characters are not all digits.")

    if not frameNumbers:
        print("No valid .png files found with numeric suffixes.")
        return

    # Step 4: Compute negativeValue
    negativeValue = abs(min((n for n in frameNumbers if n < 0), default=0))

    # Step 5: Add negativeValue to each element in frameNumbers
    updated_frame_numbers = [n + negativeValue for n in frameNumbers]

    # Sort updated_frame_numbers and files_to_rename together by the updated_frame_numbers, descending
    sorted_items = sorted(zip(updated_frame_numbers, files_to_rename), reverse=True)

    # Step 6: Rename files
    for new_number, filename in sorted_items:
        new_filename = f"{filename[:-8]}{new_number:04d}.png"
        original_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        shutil.move(original_path, new_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

# Example usage:
directory_path = 'D:\Gnomon\Expressions_Scripting\Frame_renamer'
update_frame_numbers(directory_path)
