#!/usr/bin/env python3
"""Get usage figures for August 2025"""

import os
import datetime
from glowmarkt import BrightClient

# Get credentials
username = os.getenv('GLOWMARKT_USERNAME', 'pete.treadaway@gmail.com')
password = os.getenv('GLOWMARKT_PASSWORD', 'Narlicwes0')

# Define August 2025 period
t_from = datetime.datetime(2025, 8, 1, 0, 0, 0)
t_to = datetime.datetime(2025, 9, 1, 0, 0, 0)  # End of August
period = "P1D"  # Daily readings

print(f"Getting usage figures for August 2025")
print(f"Period: {t_from.date()} to {t_to.date()}")
print("="*60)

try:
    # Connect to API
    client = BrightClient(username, password)
    entities = client.get_virtual_entities()
    
    for entity in entities:
        print(f"\nEntity: {entity.name}")
        resources = entity.get_resources()
        
        for resource in resources:
            print(f"\n  {resource.name}:")
            print(f"  Classifier: {resource.classifier}")
            
            # Round times to period boundary
            from_rounded = resource.round(t_from, period)
            to_rounded = resource.round(t_to, period)
            
            # Get readings
            readings = resource.get_readings(from_rounded, to_rounded, period)
            
            if readings:
                total = sum(r[1].value for r in readings)
                print(f"  Total for August: {total:.2f} {readings[0][1].unit if readings else ''}")
                print(f"  Daily breakdown:")
                for r in readings:
                    timestamp = r[0].astimezone().replace(tzinfo=None)
                    value = r[1]
                    print(f"    {timestamp.date()}: {value}")
            else:
                print(f"  No readings available")
            
            print()
    
    print("="*60)
    print("✓ Successfully retrieved August 2025 usage")
    
except Exception as e:
    print(f"\n✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    exit(1)
