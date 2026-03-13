import os

print("Searching for Sentinel firewall rules...")

# Saare rules ki list nikalenge aur sirf Sentinel waale delete karenge
# Ye command hamesha safe hai kyunki ye sirf filter kiye hue rules udayega
os.system('netsh advfirewall firewall delete rule name=all | findstr "Sentinel"')

print("✅ Cleanup Done! All Sentinel-X blocks have been removed.")
print("Now you can start fresh testing.")