include("$(PORT_DIR)/boards/manifest.py")
include("$(MPY_DIR)/extmod/webrepl/manifest.py")
freeze("$(MPY_DIR)/drivers/lsm6dsox/", "lsm6dsox.py")
include(
    "$(MPY_LIB_DIR)/micropython/bluetooth/aioble/manifest.py",
    client=True,
    central=True,
    l2cap=True,
    security=True,
)
freeze("$(MPY_LIB_DIR)/python-ecosys/urequests", "urequests.py")
