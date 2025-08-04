<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GME File Format Project</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc; /* Tailwind's slate-50 */
            color: #1e293b; /* Tailwind's slate-800 */
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 960px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 0.75rem; /* rounded-xl */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-xl */
        }
        h1 {
            font-size: 2.5rem; /* text-4xl */
            font-weight: 700; /* font-bold */
            color: #1d4ed8; /* Tailwind's blue-700 */
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #3b82f6; /* Tailwind's blue-500 */
        }
        h2 {
            font-size: 2rem; /* text-3xl */
            font-weight: 600; /* font-semibold */
            color: #1d4ed8; /* Tailwind's blue-700 */
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #93c5fd; /* Tailwind's blue-300 */
        }
        h3 {
            font-size: 1.5rem; /* text-2xl */
            font-weight: 600; /* font-semibold */
            color: #1d4ed8; /* Tailwind's blue-700 */
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        p {
            margin-bottom: 1rem;
            font-size: 1.125rem; /* text-lg */
        }
        ul {
            list-style-type: disc;
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }
        li {
            margin-bottom: 0.5rem;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1.5rem;
            font-size: 0.95rem;
        }
        th, td {
            border: 1px solid #cbd5e1; /* Tailwind's slate-300 */
            padding: 0.75rem;
            text-align: left;
        }
        th {
            background-color: #e0f2fe; /* Tailwind's blue-50 */
            font-weight: 600;
            color: #1e40af; /* Tailwind's blue-800 */
        }
        tr:nth-child(even) {
            background-color: #f1f5f9; /* Tailwind's slate-100 */
        }
        pre {
            background-color: #1e293b; /* Tailwind's slate-800 */
            color: #e2e8f0; /* Tailwind's slate-200 */
            padding: 1rem;
            border-radius: 0.5rem; /* rounded-lg */
            overflow-x: auto;
            margin-bottom: 1rem;
            font-family: 'Fira Code', 'Cascadia Code', monospace;
            font-size: 0.9rem;
        }
        code {
            font-family: 'Fira Code', 'Cascadia Code', monospace;
            background-color: #e2e8f0; /* Tailwind's slate-200 */
            padding: 0.2em 0.4em;
            border-radius: 0.25rem;
            color: #1e293b; /* Tailwind's slate-800 */
        }
        pre code {
            background-color: transparent;
            padding: 0;
            border-radius: 0;
            color: inherit;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>GME File Format Project</h1>

        <p>Welcome to the Game Manifest Engine (GME) file format project!</p>

        <p>This repository contains a simple, custom binary container format designed to archive one or more files into a single <code>.gme</code> file. It's similar in concept to a <code>.zip</code> file but with a custom, simple manifest. This format is ideal for packaging game assets like levels, textures, and audio into a single, easily distributable file.</p>

        <h2>File Format Specification</h2>

        <p>The <code>.gme</code> file format is structured as follows:</p>

        <h3>1. File Header (30 bytes)</h3>
        <p>The header is always 30 bytes long and contains core information for the archive.</p>
        <table>
            <thead>
                <tr>
                    <th>Field</th>
                    <th>Data Type</th>
                    <th>Size (Bytes)</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Magic Number</td>
                    <td><code>char[8]</code></td>
                    <td>8</td>
                    <td>A string of <code>GME_ARC\0</code></td>
                </tr>
                <tr>
                    <td>Version</td>
                    <td><code>unsigned short</code></td>
                    <td>2</td>
                    <td>The version number (currently <code>1</code>)</td>
                </tr>
                <tr>
                    <td>Number of Files</td>
                    <td><code>unsigned int</code></td>
                    <td>4</td>
                    <td>The total number of files in the archive</td>
                </tr>
                <tr>
                    <td>Manifest Offset</td>
                    <td><code>unsigned long long</code></td>
                    <td>8</td>
                    <td>The offset to the manifest (table of contents) from the beginning of the file</td>
                </tr>
                <tr>
                    <td>File Data Offset</td>
                    <td><code>unsigned long long</code></td>
                    <td>8</td>
                    <td>The offset to the actual file data section</td>
                </tr>
            </tbody>
        </table>

        <h3>2. File Manifest (Variable Size)</h3>
        <p>This section serves as the table of contents, containing an entry for each file in the archive.</p>
        <p>Each entry provides the necessary information to locate and identify a single file.</p>
        <table>
            <thead>
                <tr>
                    <th>Field</th>
                    <th>Data Type</th>
                    <th>Size (Bytes)</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Filename Length</td>
                    <td><code>unsigned short</code></td>
                    <td>2</td>
                    <td>The length of the filename string</td>
                </tr>
                <tr>
                    <td>Filename</td>
                    <td><code>char[Filename Length]</code></td>
                    <td>Variable</td>
                    <td>The actual filename (e.g., <code>level_1.bin</code>, <code>player_texture.png</code>)</td>
                </tr>
                <tr>
                    <td>File Size</td>
                    <td><code>unsigned long long</code></td>
                    <td>8</td>
                    <td>The size of the file data in bytes</td>
                </tr>
                <tr>
                    <td>File Offset</td>
                    <td><code>unsigned long long</code></td>
                    <td>8</td>
                    <td>The offset of the file data from the start of the <code>.gme</code> file</td>
                </tr>
            </tbody>
        </table>

        <h3>3. File Data (Variable Size)</h3>
        <p>This section contains the raw binary data of all the archived files, stored consecutively. Their sizes and locations are determined by the manifest entries.</p>

        <h2>Tools</h2>
        <ul>
            <li><code>create_gme_archive.py</code>: A Python script that takes a list of input files and archives them into a single <code>.gme</code> file.</li>
            <li><code>read_gme_archive.py</code>: A Python script that reads a <code>.gme</code> archive, extracts its manifest, and reconstructs the original files into a specified output directory.</li>
        </ul>

        <h2>How to Use</h2>

        <h3>1. Create Sample Files (if needed)</h3>
        <p>To create some sample text files for archiving:</p>
        <pre><code>echo "This is the content of the first file." &gt; file1.txt
echo "This is the content of the second file." &gt; file2.txt
echo "This is the third file, it's a bit longer to show different sizes." &gt; file3.txt
</code></pre>

        <h3>2. Create a GME Archive</h3>
        <p>To create an <code>archive.gme</code> file containing <code>file1.txt</code>, <code>file2.txt</code>, and <code>file3.txt</code>:</p>
        <pre><code>python3 create_gme_archive.py
</code></pre>

        <h3>3. Read and Extract from a GME Archive</h3>
        <p>To extract the contents of <code>archive.gme</code> into the <code>extracted_files</code> directory:</p>
        <pre><code>mkdir extracted_files # Create the output directory if it doesn't exist
python3 read_gme_archive.py
</code></pre>
    </div>
</body>
</html>
