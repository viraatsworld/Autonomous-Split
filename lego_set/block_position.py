from pxr import UsdGeom, Gf, Usd

stage = omni.usd.get_context().get_stage()
prim_path = "/root/lego_set/Brick_2x2_Purple/Brick_2x2_Purple_Purple_0/Brick_2x2_Purple_Purple_0"

prim = stage.GetPrimAtPath(prim_path)

if prim.IsValid():
    xform = UsdGeom.Xformable(prim)
    world_transform = omni.usd.utils.get_world_transform_matrix(prim)
    translation = world_transform.ExtractTranslation()

    print("Block position:", translation)

