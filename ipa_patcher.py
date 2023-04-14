import plistlib
import shutil
import os

shutil.move("Enmity.ipa", "Enmity.zip")
print("[*] Unpacking...")
shutil.unpack_archive('Enmity.zip', 'ipa_patcher')
print("[*] Editing Info.plist")
f = open("ipa_patcher/Payload/Discord.app/Info.plist", "rb")
plist = plistlib.load(f)
f.close()
plist["NSFaceIDUsageDescription"] = "K2genmity"
f = open("ipa_patcher/Payload/Discord.app/Info.plist", "wb")
plistlib.dump(plist, f)
f.close()
print("[*] Compressing...")
shutil.make_archive('Enmity_patched', 'zip', 'ipa_patcher')
shutil.move("Enmity_patched.zip", "Enmity.ipa")
print("[*] Cleaning files...")
os.remove("Enmity.zip")
shutil.rmtree("ipa_patcher")
print("[*] Done!")
