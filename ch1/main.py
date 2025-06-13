def get_median_font_size(font_sizes):
    font_sizes.sort()
    if len(font_sizes) % 2 != 0:
        index = int(len(font_sizes) / 2)
        return font_sizes[index]
    else:
        index = int(len(font_sizes) / 2)
        return int((font_sizes[index] + font_sizes[index - 1]) / 2)


print(get_median_font_size([8, 8, 8]))
print(get_median_font_size([8, 8, 8, 4]))
