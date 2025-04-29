def fifo_page_replacement(reference_string, num_frames):
    frames = []
    page_faults = 0

    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the first page (FIFO)
                frames.append(page)

    return page_faults

# Reference string and number of frames
reference_string = [1, 3, 0, 3, 5, 6, 3]
num_frames = 3

# Run FIFO and print the result
print(f"Page Faults: {fifo_page_replacement(reference_string, num_frames)}")
