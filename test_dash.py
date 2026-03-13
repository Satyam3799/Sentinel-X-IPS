from supabase import create_client

# Teri Lovable Cloud Details
URL = "https://irxrhxyyzajpatwfsoud.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlyeHJoeHl5emFqcGF0d2Zzb3VkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMzNzIwMTcsImV4cCI6MjA4ODk0ODAxN30.qu6up56J7LkAKHKgi7YR4PTUTJl8ZWVHwy_OBbG66DY"

supabase = create_client(URL, KEY)

print("--- Sentinel-X: Testing Connection to Lovable Cloud ---")

try:
    # Ek fake attack data bhej rahe hain dashboard par dikhane ke liye
    test_data = {
        "attacker_ip": "101.202.303.404", 
        "attack_type": "Lovable Cloud Handshake", 
        "severity": "Medium", 
        "action_taken": "Logged"
    }
    
    # Supabase/Lovable table mein insert
    response = supabase.table("attacks").insert(test_data).execute()
    print("🚀 SUCCESS! Data Lovable Cloud mein chala gaya.")
    print("Ab apne Lovable Dashboard par jaao aur dekho '101.202.303.404' dikh raha hai ya nahi.")

except Exception as e:
    print(f"❌ Error ho gaya: {e}")