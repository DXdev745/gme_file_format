import struct
import os

def read_gme_archive(archive_filename, output_folder):
    """
    Reads a GME archive and extracts its contents to a folder.
    """
    print(f"Reading GME archive: {archive_filename}")

    if not os.path.exists(output_folder):
        print(f"Error: Output folder '{output_folder}' does not exist.")
        return

    with open(archive_filename, 'rb') as f:
        # --- Read Header (30 bytes) ---
        header_data = f.read(30)
        magic_number, version, num_files, manifest_offset, file_data_offset = \
            struct.unpack('<8s H I Q Q', header_data)

        # Check if this is a valid GME file
        if magic_number != b'GME_ARC\0':
            print(f"Error: Invalid magic number in file header.")
            return

        print(f"File version: {version}")
        print(f"Number of files in archive: {num_files}")
        print("-" * 20)

        # --- Read Manifest ---
        f.seek(manifest_offset)

        for i in range(num_files):
            # Read filename length
            filename_len_data = f.read(2)
            filename_len = struct.unpack('<H', filename_len_data)[0]

            # Read filename
            filename_bytes = f.read(filename_len)
            filename = filename_bytes.decode('utf-8')

            # Read file size and offset
            file_metadata_data = f.read(16)
            file_size, file_offset = struct.unpack('<Q Q', file_metadata_data)

            print(f"Found file: {filename} (Size: {file_size} bytes)")

            # --- Read and Extract File Data ---
            # Save the current position
            current_position = f.tell()

            # Seek to the file's data
            f.seek(file_offset)

            # Read the data
            file_data = f.read(file_size)

            # Write the data to a new file
            output_path = os.path.join(output_folder, filename)
            with open(output_path, 'wb') as out_f:
                out_f.write(file_data)

            print(f"Extracted file to: {output_path}")

            # Return to the previous position to read the next manifest entry
            f.seek(current_position)

    print("\nAll files have been successfully extracted.")


# --- MAIN EXECUTION ---
# Define the archive to read and the folder to extract to
archive_to_read = "archive.gme"
extraction_folder = "extracted_files"

read_gme_archive(archive_to_read, extraction_folder)
