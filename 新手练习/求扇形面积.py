def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"面积为:{sector_area}")
    return sector_area


calculate_sector(160, 30)
