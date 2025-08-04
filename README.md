GME File Format Project
Description
Welcome to the Game Manifest Engine (GME) file format project!

This repository contains a simple, custom binary container format designed to archive one or more files into a single .gme file. It's similar in concept to a .zip file but with a custom, simple manifest. This format is ideal for packaging game assets like levels, textures, and audio into a single, easily distributable file.

This version of the GME format now supports zlib compression and AES-256-CBC encryption for enhanced security and efficiency.

File Format Specification
The .gme file format is structured as follows:

1. File Header (46 bytes)
The header is always 46 bytes long and contains core information for the archive, including a unique salt for encryption key derivation.

Field

Data Type

Size (Bytes)

Description

Magic Number

char[8]

8

A string of GME_ARC\0

Version

unsigned short

2

The version number (currently 1)

Number of Files

unsigned int

4

The total number of files in the archive

Manifest Offset

unsigned long long

8

The offset to the manifest (table of contents) from the beginning of the file

File Data Offset

unsigned long long

8

The offset to the actual file data section

Salt

char[16]

16

Unique 16-byte salt for password-based key derivation (PBKDF2HMAC)

2. File Manifest (Variable Size)
This section serves as the table of contents, containing an entry for each file in the archive. Each entry now includes details about its original size, stored size, compression status, encryption status, and a unique Initialization Vector (IV) for encryption.

Field

Data Type

Size (Bytes)

Description

Filename Length

unsigned short

2

The length of the filename string

Filename

char[Filename Length]

Variable

The actual filename (e.g., level_1.bin, player_texture.png)

Original File Size

unsigned long long

8

The size of the file data before compression/encryption

Stored File Size

unsigned long long

8

The size of the file data after compression/encryption (actual size in archive)

Compression Flag

unsigned char

1

0 for no compression, 1 for zlib compression

Encryption Flag

unsigned char

1

0 for no encryption, 1 for AES-256-CBC encryption

IV (Initialization Vector)

char[16]

16

Unique 16-byte IV for AES-CBC encryption of this file's data

File Offset

unsigned long long

8

The offset of the file data from the start of the .gme file

3. File Data (Variable Size)
This section contains the raw binary data of all the archived files, stored consecutively. Their sizes and locations are determined by the manifest entries. Data here will be compressed and/or encrypted if those flags are set in the manifest.

Tools
create_gme_archive.py: A Python script that takes a list of input files and archives them into a single .gme file. It supports optional zlib compression and AES-256-CBC encryption.

read_gme_archive.py: A Python script that reads a .gme archive, extracts its manifest, and reconstructs the original files into a specified output directory. It automatically detects and handles zlib decompression and AES-256-CBC decryption.

How to Use
0. Prerequisites
Ensure you have Python 3 installed. For encryption, you'll need the cryptography library. It's recommended to use a virtual environment:

# Create a virtual environment (if you haven't already)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the cryptography library
pip install cryptography

1. Create Sample Files (if needed)
To create some sample text files for archiving:

echo "This is the content of the first file." > file1.txt
echo "This is the content of the second file." > file2.txt
echo "This is the third file, it's a bit longer to show different sizes." > file3.txt

2. Create a GME Archive (with Compression and Encryption)
To create an archive_encrypted_compressed.gme file containing file1.txt, file2.txt, and file3.txt with both compression and encryption enabled:

python3 create_gme_archive.py

(The script will prompt you to enter a password for encryption.)

3. Read and Extract from a GME Archive
To extract the contents of archive_encrypted_compressed.gme into the extracted_files directory:

mkdir -p extracted_files # Create the output directory if it doesn't exist
python3 read_gme_archive.py

(The script will prompt you to enter the password used during encryption.)
