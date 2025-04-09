import os
import lzma
from tqdm import tqdm

def xz_files_in_dir(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

folder_path = "/Users/willkatabian/Desktop/DIY Large Language Model/openwebtext/subsets/openwebtext"
output_file_train = "train_split.txt"
output_file_val = "val_split.txt"
vocab_file = "vocab.txt"

files = xz_files_in_dir(folder_path)
total_files = len(files)

# calculate the split indices
split_index = int(total_files * 0.9)  # 90% for training
files_train = files[:split_index]
files_val = files[split_index:]

# process the files for training and validation separately
vocab = set()


# process the training files
with open(output_file_train, "w", encoding="utf-8") as outfile:
        for filename in tqdm(files_train, total=len(files_train)):
            file_path = os.path.join(folder_path, filename)
            with lzma.open(file_path, "rt", encoding="utf-8") as infile:
                text = infile.read()
                outfile.write(text)
                characters = set(text)
                vocab.update(characters)

# process the validation files
with open(output_file_val, "w", encoding="utf-8") as outfile:
        for filename in tqdm(files_val, total=len(files_val)):
            file_path = os.path.join(folder_path, filename)
            with lzma.open(file_path, "rt", encoding="utf-8") as infile:
                text = infile.read()
                outfile.write(text)
                characters = set(text)
                vocab.update(characters)


# write the vocabulary to vocab.txt
with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')