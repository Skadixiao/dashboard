#%%
from microsoft import extract_upcoming_event
from sandisk import scrape_sandisk_upcoming_events
microsoft = extract_upcoming_event()
sandisk = scrape_sandisk_upcoming_events()

# %%
print(microsoft["section"])
print(microsoft["datetime"])
print(microsoft["title"])

print("\n")
for event in sandisk:
    print(event["section"])
    print(event["datetime"])
    print(event["title"])
    print(event["url"])
    print("\n")