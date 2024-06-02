guild_element = '<div aria-label="Guild: My Guild, Member Count: 12"></div>'
guild_name = guild_element.get_attribute("aria-label").split(', ')[-1].strip()
print(guild_name)  # Output: My Guild
