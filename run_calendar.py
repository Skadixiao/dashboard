#%%
from microsoft import extract_upcoming_event
from micron import extract_micron_upcoming_events
from sandisk import scrape_sandisk_upcoming_events

microsoft = extract_upcoming_event()
micron = extract_micron_upcoming_events()
sandisk = scrape_sandisk_upcoming_events()
# %%
print("\n")
print("Microsoft Upcoming Event:")
print(microsoft["datetime"])
print(microsoft["title"])
print("\n")

print("Micron Upcoming Events:")
for event in micron:
    print(event["datetime"])
    print(event["title"])
    print(event["url"])
print("\n")

print("SanDisk Upcoming Events:")
for event in sandisk:
    print(event["datetime"])
    print(event["title"])
    print(event["url"])
