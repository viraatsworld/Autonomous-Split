import omni.replicator.core as rep
prim_paths= [ "/root/lego_set/Plane_2x2_Baby_Grey/Plane_2x2_Baby_Grey_Baby_Grey_0/Plane_2x2_Baby_Grey_Baby_Grey_0","/root/lego_set/Brick_2x2_Purple/Brick_2x2_Purple_Purple_0/Brick_2x2_Purple_Purple_0","/root/lego_set/Brick_2x2_Dark_Yellow/Brick_2x2_Dark_Yellow_Dark_Yellow_0/Brick_2x2_Dark_Yellow_Dark_Yellow_0","/root/lego_set/Brick_2x2_Dark_Yellow/Brick_2x2_Dark_Yellow_Dark_Yellow_0/Brick_2x2_Dark_Yellow_Dark_Yellow_0","/root/lego_set/Brick_2x2_Dark_Yellow/Brick_2x2_Dark_Yellow_Dark_Yellow_0/Brick_2x2_Dark_Yellow_Dark_Yellow_0","/root/lego_set/Brick_2x4_Red/Brick_2x4_Red_Red_0/Brick_2x4_Red_Red_0","/root/lego_set/Plane_2x2_Baby_Violet/Plane_2x2_Baby_Violet_Baby_Violet_0/Plane_2x2_Baby_Violet_Baby_Violet_0","/root/lego_set/Brick_2x4_Black/Brick_2x4_Black_Black_0/Brick_2x4_Black_Black_0","/root/lego_set/Brick_1x2_Yellow/Brick_1x2_Yellow_Yellow_0/Brick_1x2_Yellow_Yellow_0","/root/lego_set/Plane_1x2_Baby_Pink/Plane_1x2_Baby_Pink_Baby_Pink_0/Plane_1x2_Baby_Pink_Baby_Pink_0","/root/lego_set/Plane_2x4_Lime/Plane_2x4_Lime_Lime_0/Plane_2x4_Lime_Lime_0","/root/lego_set/Brick_1x2_Dark_Pink/Brick_1x2_Dark_Pink_Dark_Pink_0/Brick_1x2_Dark_Pink_Dark_Pink_0","/root/lego_set/Plane_2x2_Dark_Turquoise/Plane_2x2_Dark_Turquoise_Dark_Turquoise_0/Plane_2x2_Dark_Turquoise_Dark_Turquoise_0","/root/lego_set/Plane_2x2_Green/Plane_2x2_Green_Green_0/Plane_2x2_Green_Green_0","/root/lego_set/Brick_2x2_Brown/Brick_2x2_Brown_Brown_0/Brick_2x2_Brown_Brown_0","/root/lego_set/Brick_2x4_Dark_Blue/Brick_2x4_Dark_Blue_Dark_Blue_0/Brick_2x4_Dark_Blue_Dark_Blue_0","/root/lego_set/Plane_1x2_Blue/Plane_1x2_Blue_Blue_0/Plane_1x2_Blue_Blue_0","/root/lego_set/Plane_2x4_White/Plane_2x4_White_White_0/Plane_2x4_White_White_0","/root/lego_set/Brick_1x2_Transparent/Brick_1x2_Transparent_Transparent_0/Brick_1x2_Transparent_Transparent_0","/root/lego_set/Plane_2x4_Baby_Turquoise/Plane_2x4_Baby_Turquoise_Baby_Turquoise_0/Plane_2x4_Baby_Turquoise_Baby_Turquoise_0","/root/lego_set/Brick_2x2_Dark_Red/Brick_2x2_Dark_Red_Dark_Red_0/Brick_2x2_Dark_Red_Dark_Red_0","/root/lego_set/Brick_1x2_Violet/Brick_1x2_Violet_Violet_0/Brick_1x2_Violet_Violet_0","/root/lego_set/Plane_1x2_Grey/Plane_1x2_Grey_Grey_0/Plane_1x2_Grey_Grey_0","/root/lego_set/Brick_2x4_Orange/Brick_2x4_Orange_Orange_0/Brick_2x4_Orange_Orange_0","/root/lego_set/Plane_2x4_Baby_Blue/Plane_2x4_Baby_Blue_Baby_Blue_0/Plane_2x4_Baby_Blue_Baby_Blue_0"]
prime_node= [rep.get.prim_at_path(path) for path in prim_paths]

# Define XY boundary and fixed Z
x_range = (-0.1, 0.02)   # adjust as needed
y_range = (-0.1, 0.1)   # adjust as needed
z_fixed= 0.0         # fixed height (like on a table)


with rep.trigger.on_frame():
    for node in prime_node:
        with node:
            rep.modify.pose(
                position=rep.distribution.uniform(
                    (x_range[0], y_range[0], z_fixed),
                    (x_range[1], y_range[1], z_fixed)
                )
            )











