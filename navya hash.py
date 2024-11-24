import hashlib

# Name input
name = "Navya"

# Calculate hash value
hash_value = int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16) % 50
print(hash_value)
