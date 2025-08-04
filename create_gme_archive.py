import struct
import os

def create_gme_archive(input_files, output_filename):
    """
    Creates a GME archive from a list of files.
    """
    print(f"Creating GME archive: {output_filename}")

    # We need to gather all the file data first to calculate offsets
    files_data = []
    for filename in input_files:
        try:
            with open(filename, 'rb') as f:
                data = f.read()
                files_data.append({
                    "filename": filename,
                    "size": len(data),
                    "data": data
                })
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Skipping.")
            return

    # Calculate offsets
    num_files = len(files_data)
    manifest_offset = 30  # Header is 30 bytes, so manifest starts at byte 30
    file_data_offset = manifest_offset

    # The manifest size depends on the number of files and filename lengths
    for file_info in files_data:
        filename_bytes = file_info["filename"].encode('utf-8')
        # 2 bytes for length + length of filename + 8 for size + 8 for offset
        file_data_offset += 2 + len(filename_bytes) + 8 + 8

    # Open the output file for writing in binary mode
    with open(output_filename, 'wb') as f:
        # --- Write Header (30 bytes) ---
        magic_number = b'GME_ARC\0'
        version = 1
        header_data = struct.pack('<8s H I Q Q', magic_number, version, num_files, manifest_offset, file_data_offset)
        f.write(header_data)

        # --- Write Manifest ---
        current_file_offset = file_data_offset
        for file_info in files_data:
            filename_bytes = file_info["filename"].encode('utf-8')
            filename_len = len(filename_bytes)

            # Write filename length and the filename itself
            f.write(struct.pack('<H', filename_len))
            f.write(filename_bytes)

            # Write file size and offset
            manifest_entry_data = struct.pack('<Q Q', file_info["size"], current_file_offset)
            f.write(manifest_entry_data)

            # Update the offset for the next file
            current_file_offset += file_info["size"]

        # --- Write File Data ---
        for file_info in files_data:
            f.write(file_info["data"])

    print(f"Successfully created '{output_filename}' containing {num_files} files.")


# --- MAIN EXECUTION ---
# Define the input and output filenames
input_files_list = ["file1.txt", "file2.txt", "file3.txt"]
output_filename = "archive.gme"

# Create the archive
create_gme_archive(input_files_list, output_filename)
