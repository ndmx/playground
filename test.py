def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    if block_size >= filesize and filesize > 0:
        fullblock_size = 1
    elif filesize%block_size == 0:
        fullblock_size = filesize//block_size
    elif filesize > block_size and (filesize%block_size) != 0:
        fullblock_size = filesize//block_size + 1
    else:
        fullblock_size = 0

    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size

    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return fullblock_size * block_size
	  #filesize//block_size + block_size
    return  fullblock_size * block_size

print(calculate_storage(10))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(8192)) # Should be 8192