include("../manifest.py")

freeze("$(MPY_DIR)/tools", "upip.py")
freeze("$(MPY_DIR)/tools", "upip_utarfile.py")
freeze("$(MPY_DIR)/extmod", "ntptime.py")

freeze("$(MPY_LIB_DIR)/python-ecosys/urequests", "urequests.py")
