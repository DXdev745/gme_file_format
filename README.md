GME File Format Project
Welcome to the Game Manifest Engine (GME) file format project!

This repository contains a simple, custom binary container format designed to archive one or more files into a single .gme file. It's similar in concept to a .zip file but with a custom, simple manifest. This format is ideal for packaging game assets like levels, textures, and audio into a single, easily distributable file.

File Format Specification
The .gme file format is structured as follows:

1. File Header (30 bytes)
The header is always 30 bytes long and contains core information for the archive.

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

2. File Manifest (Variable Size)
This section serves as the table of contents, containing an entry for each file in the archive.

Each entry provides the necessary information to locate and identify a single file.

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

File Size

unsigned long long

8

The size of the file data in bytes

File Offset

unsigned long long

8

The offset of the file data from the start of the .gme file

3. File Data (Variable Size)
This section contains the raw binary data of all the archived files, stored consecutively. Their sizes and locations are determined by the manifest entries.

Tools
create_gme_archive.py: A Python script that takes a list of input files and archives them into a single .gme file.

read_gme_archive.py: A Python script that reads a .gme archive, extracts its manifest, and reconstructs the original files into a specified output directory.

How to Use
1. Create Sample Files (if needed)
To create some sample text files for archiving:

echo "This is the content of the first file." > file1.txt
echo "This is the content of the second file." > file2.txt
echo "This is the third file, it's a bit longer to show different sizes." > file3.txt

2. Create a GME Archive
To create an archive.gme file containing file1.txt, file2.txt, and file3.txt:

python3 create_gme_archive.py

3. Read and Extract from a GME Archive
To extract the contents of archive.gme into the extracted_files directory:

mkdir extracted_files # Create the output directory if it doesn't exist
python3 read_gme_archive.py
