#!/usr/bin/env python3
"""Test script to verify Glowmarkt API connection"""

import os
from glowmarkt import BrightClient

# Get credentials from environment or use defaults
username = os.getenv('GLOWMARKT_USERNAME', 'pete.treadaway@gmail.com')
password = os.getenv('GLOWMARKT_PASSWORD', 'Narlicwes0')

print(f"Testing connection to Glowmarkt API...")
print(f"Username: {username}")

try:
    # Create client and authenticate
    client = BrightClient(username, password)
    print("✓ Authentication successful!")
    
    # Get virtual entities
    entities = client.get_virtual_entities()
    print(f"\n✓ Found {len(entities)} virtual entity/entities")
    
    # Display entities and resources
    for ent in entities:
        print(f"\nEntity: {ent.name}")
        resources = ent.get_resources()
        print(f"  Resources ({len(resources)}):")
        for res in resources:
            print(f"    - {res.name} (classifier: {res.classifier})")
    
    print("\n✓ Connection test successful!")
    
except Exception as e:
    print(f"\n✗ Connection failed: {str(e)}")
    exit(1)
