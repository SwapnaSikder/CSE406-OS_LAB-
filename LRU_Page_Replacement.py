def lru_page_replacement(reference_string, num_frames):
    frames = []
    page_faults = 0

    for page in reference_string:
        if page in frames:
            # If page is already in memory, move it to the end (most recently used)
            frames.remove(page)
            frames.append(page)
        else:
            # Page fault occurs
            page_faults += 1
            if len(frames) >= num_frames:
                # Remove the least recently used page (front of the list)
                frames.pop(0)
            # Add the new page as most recently used
            frames.append(page)

    return page_faults

# Reference string and number of frames
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 4

# Output the result
print("Page Faults:", lru_page_replacement(reference_string, num_frames))
